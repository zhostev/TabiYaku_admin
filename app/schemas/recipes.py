# app/schemas/recipes.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RecipeRecognitionResponse(BaseModel):
    recipe: str
    message: str = "识别成功"

class RecipeRecognitionErrorResponse(BaseModel):
    detail: str

class RecipeRecognitionCreate(BaseModel):
    image: bytes  # 前端将图片以字节形式传输

class RecipeRecognitionOut(BaseModel):
    id: int
    recipe: str
    created_at: datetime

    class Config:
        from_attributes = True

class RecipeRecognitionList(BaseModel):
    recognitions: List[RecipeRecognitionOut]