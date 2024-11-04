# app/controllers/recipe.py

from fastapi import UploadFile, HTTPException, Depends
from typing import Union, List

from app.schemas.recipes import RecipeRecognitionResponse, RecipeRecognitionOut
from app.utils.openai_client import recognize_recipe
from app.models.recipes import RecipeRecognition
from app.models.admin import User  # 从 admin.py 导入 User 模型
from app.utils.auth import get_current_user

async def recognize_recipe_controller(
    file: UploadFile,
    current_user: User
) -> RecipeRecognitionResponse:
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="不支持的文件类型。请上传 JPEG 或 PNG 图片。")

    try:
        image_bytes = await file.read()
        recipe_text = recognize_recipe(image_bytes)
        
        # 创建识别记录
        recognition = await RecipeRecognition.create(
            user=current_user,
            image=image_bytes,
            recognized_text=recipe_text
        )
        
        return RecipeRecognitionResponse(recipe=recipe_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail="菜谱识别失败。") from e

async def get_recognition_records_controller(
    current_user: User
) -> List[RecipeRecognitionOut]:
    recognitions = await RecipeRecognition.filter(user=current_user).order_by('-created_at').all()
    return recognitions