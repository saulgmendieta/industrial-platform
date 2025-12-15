from fastapi import FastAPI
from sqlalchemy import text
from app.db import base 

from app.db.session import engine

app = FastAPI(title="Industrial Monitoring API")


@app.get("/health", tags=["health"])
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"status": "ok"}