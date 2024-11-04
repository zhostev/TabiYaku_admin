# app/api/v1/recipes/recipes.py

from fastapi import APIRouter, UploadFile, File, Depends
from typing import List

from app.schemas.recipes import (
    RecipeRecognitionResponse,
    RecipeRecognitionErrorResponse,
    RecipeRecognitionOut
)
from app.controllers.recipe import (
    recognize_recipe_controller,
    get_recognition_records_controller
)
from app.utils.auth import get_current_user
from app.models.admin import User  # 从 admin.py 导入 User 模型

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

@router.post(
    "/recognize",
    response_model=RecipeRecognitionResponse,
    responses={
        400: {"model": RecipeRecognitionErrorResponse},
        500: {"model": RecipeRecognitionErrorResponse},
    },
    summary="识别并翻译菜谱图片",
    description="上传日本菜谱的照片，系统将自动识别并翻译为中文。",
)
async def recognize_recipe(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    识别上传的菜谱图片并返回中文翻译结果，同时记录识别记录。
    """
    return await recognize_recipe_controller(file, current_user)

@router.get(
    "/records",
    response_model=List[RecipeRecognitionOut],
    responses={
        401: {"model": RecipeRecognitionErrorResponse},
        500: {"model": RecipeRecognitionErrorResponse},
    },
    summary="获取用户的菜谱识别记录",
    description="获取当前用户的所有菜谱识别记录。",
)
async def get_recognition_records(
    current_user: User = Depends(get_current_user)
):
    """
    获取当前用户的所有菜谱识别记录。
    """
    return await get_recognition_records_controller(current_user)