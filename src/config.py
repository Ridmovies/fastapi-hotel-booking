from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    MODE: Literal["DEV", "TEST", "PROD"]

    # postgresql
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    # REDIS
    REDIS_HOST: str
    REDIS_PORT: int

    # JWT
    JWT_TRANSPORT: Literal["COOKIE", "BEARER"] = "COOKIE"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Path
    IMAGE_RESIZED_PATH: str = "src/static/images/small"
    IMAGE_PATH: str = "src/static/images"

    # SMTP EMAIL
    turn_on_email_notification: bool = False
    SMTP_USER: str
    SMTP_PASS: str
    SMTP_HOST: str
    SMTP_PORT: int


settings = Config()