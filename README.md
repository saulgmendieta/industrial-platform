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

## Tech Stack
- Python 3.11
- FastAPI
- Docker
- PostgreSQL (planned)

## Local Development

The project uses Docker Compose for local orchestration.

```bash
docker-compose up --build