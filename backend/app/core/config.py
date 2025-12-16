from pydantic_settings import BaseSettings
import logging
logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    APP_NAME: str = "Industrial Backend"
    LOG_LEVEL: str = "INFO"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
logger.info("Configuration loaded successfully")