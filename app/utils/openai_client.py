# app/utils/openai_client.py

import os
import openai
import base64
from typing import Any, Dict

from loguru import logger

# 设置 OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def encode_image(image_file: bytes) -> str:
    """将图片文件编码为 base64 字符串"""
    return base64.b64encode(image_file).decode("utf-8")

def recognize_recipe(image_bytes: bytes) -> str:
    """
    使用 OpenAI 的 GPT-4 模型识别菜谱图片并翻译为中文。
    
    :param image_bytes: 图片的字节内容
    :return: 翻译后的中文菜谱文本
    """
    try:
        base64_image = encode_image(image_bytes)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that can recognize and translate recipe images from Japanese to Chinese."},
                {"role": "user", "content": f"请根据以下图片内容生成中文菜谱：<img src='data:image/png;base64,{base64_image}' />"}
            ],
            temperature=0.0,
        )
        recipe_text = response.choices[0].message.content.strip()
        return recipe_text
    except Exception as e:
        logger.error(f"Error in recognize_recipe: {e}")
        raise e