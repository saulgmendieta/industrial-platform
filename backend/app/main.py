from fastapi import FastAPI
from sqlalchemy import text
from app.db import base 
from app.core.logging import setup_logging
from app.core.config import settings
from app.db.session import engine
import logging

app = FastAPI(title="Industrial Monitoring API")
setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)
logger.info("Starting application")

@app.get("/health", tags=["health"])
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"status": "ok"}