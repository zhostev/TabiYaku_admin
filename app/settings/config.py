import os
import typing
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str  
    # Metadata settings
    VERSION: str = "0.1.0"
    APP_TITLE: str = "TabiYaku Admin"
    PROJECT_NAME: str = "TabiYaku Admin"
    APP_DESCRIPTION: str = "Description"

    # CORS settings
    CORS_ORIGINS: typing.List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: typing.List = ["*"]
    CORS_ALLOW_HEADERS: typing.List = ["*"]

    # Application settings
    DEBUG: bool = True

    # Directory settings
    PROJECT_ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR: str = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT: str = os.path.join(BASE_DIR, "app/logs")

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Database configuration
    TORTOISE_ORM: dict = {
        "connections": {
            # SQLite configuration
            # "sqlite": {
            #     "engine": "tortoise.backends.sqlite",
            #     "credentials": {"file_path": f"{BASE_DIR}/db.sqlite3"},
            # },
            # MySQL/MariaDB configuration
            # Install with: pip install tortoise-orm[asyncmy]
            "mysql": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": os.getenv("MYSQL_HOST", "rm-2zev5u696jj316m801o.mysql.rds.aliyuncs.com"),    # Database host address
                    "port": int(os.getenv("MYSQL_PORT", 3306)),       # Database port
                    "user": os.getenv("MYSQL_USER", "halo_4cSd4J"),  # Database username
                    "password": os.getenv("MYSQL_PASSWORD", "Moshou99"),  # Database password
                    "database": os.getenv("MYSQL_DATABASE", "TakuYabi"),  # Database name
                },
            },
            # # PostgreSQL configuration
            # # Install with: pip install tortoise-orm[asyncpg]
            # "postgres": {
            #     "engine": "tortoise.backends.asyncpg",
            #     "credentials": {
            #         "host": os.getenv("POSTGRES_HOST", "localhost"),    # Database host address
            #         "port": int(os.getenv("POSTGRES_PORT", 5432)),      # Database port
            #         "user": os.getenv("POSTGRES_USER", "yourusername"), # Database username
            #         "password": os.getenv("POSTGRES_PASSWORD", "yourpassword"),  # Database password
            #         "database": os.getenv("POSTGRES_DATABASE", "yourdatabase"),  # Database name
            #     },
            # },
        },
        "apps": {
            "models": {
                "models": ["app.models", "aerich.models"],
                "default_connection": "mysql",  # Change to "mysql" or "postgres" as needed
            },
        },
        "use_tz": False,  # Whether to use timezone-aware datetimes
        "timezone": "Asia/Shanghai",  # Timezone setting
    }

    # Date and time format
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # Configuration for loading .env file
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()