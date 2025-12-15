# 1. Imagen base
FROM python:3.11-slim

# 2. Avoid .pyc files and force immediate logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Work directory
WORKDIR /app

# 4. Install system dependencies (min)
RUN apt-get update \
    && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy project definition
COPY pyproject.toml .

# 6. Install Python dependencies
RUN pip install --upgrade pip \
    && pip install . \
    && pip install alembic

# 7. Code copy
COPY app ./app

# 8. startup command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
