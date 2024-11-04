# app/models/recipes.py

from tortoise import fields
from app.models.base import BaseModel, TimestampMixin
from app.models.admin import User  # 从 admin.py 导入 User 模型

class RecipeRecognition(BaseModel, TimestampMixin):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='recipe_recognitions', description="进行识别的用户")
    image = fields.BinaryField(description="上传的菜谱图片")
    recognized_text = fields.TextField(description="识别并翻译后的中文菜谱文本")
    created_at = fields.DatetimeField(auto_now_add=True, description="记录创建时间")

    class Meta:
        table = "recipe_recognitions"

    def __str__(self):
        return f"RecipeRecognition(id={self.id}, user_id={self.user}, created_at={self.created_at})"