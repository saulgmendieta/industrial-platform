# Industrial Platform

A containerized backend platform designed to explore modern system architecture
for industrial-style data ingestion and monitoring.

## Project Scope
This project focuses on:
- Clean backend architecture with FastAPI
- Explicit data contracts between producers and consumers
- Containerized local development using Docker
- Separation between ingestion, business logic, and persistence

The project is intentionally developed in incremental stages to reflect
real-world system design practices.

Backend service built with FastAPI, designed with clean architecture,
environment-based configuration, and container-ready logging.

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker / Docker Compose


## Architecture
app/
├── api/        # HTTP layer
├── services/   # Business logic
├── db/         # Persistence
└── core/       # Config & logging

## Local Development

The project uses Docker Compose for local orchestration.

```bash
docker-compose up --build