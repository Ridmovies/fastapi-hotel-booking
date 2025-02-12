from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # postgresql
    DATABASE_URL: str

    # REDIS
    REDIS_HOST: str
    REDIS_PORT: int

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Path
    IMAGE_RESIZED_PATH: str = "src/static/images/small"
    IMAGE_PATH: str = "src/static/images"


settings = Config()