from fastapi import FastAPI

app = FastAPI(
    title="Industrial Monitoring API",
    version="0.1.0",
    description="Backend service for an industrial monitoring platform"
)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}