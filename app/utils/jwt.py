# app/utils/jwt.py

import jwt
from typing import Dict, Any
from app.schemas.login import JWTPayload
from app.settings.config import settings
from jwt import PyJWTError

def create_access_token(*, data: JWTPayload) -> str:
    """
    创建 JWT 访问令牌

    :param data: JWTPayload 模型
    :return: 编码后的 JWT 字符串
    """
    payload = data.model_dump().copy()
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_jwt_token(token: str) -> Dict[str, Any]:
    """
    解码 JWT 访问令牌

    :param token: JWT 字符串
    :return: 解码后的载荷
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except PyJWTError:
        raise