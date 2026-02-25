# Airflow Learning Pipeline (Local Deployment)

This project deploys Apache Airflow locally with Docker Compose and includes one beginner ETL DAG.

## Prerequisites

- Docker Desktop (with Docker Compose)
- At least 4 GB RAM available to Docker

## Project structure

- `docker-compose.yaml` - Airflow + Postgres services
- `.env` - Airflow runtime user id
- `dags/learning_pipeline.py` - sample ETL DAG

## Deploy and run

From this folder (`airflow-learning`):

```powershell
docker compose up airflow-init
docker compose up -d
```

Open Airflow UI:

- URL: `http://localhost:8080`
- Username: `admin`
- Password: `admin`

## Run the example DAG

1. In Airflow UI, find `learning_etl_pipeline`
2. Turn it on
3. Click **Trigger DAG**
4. Open task logs for `load` to see output

Expected log line:

```text
Loaded metric -> average=4.80
```

## Stop and clean up

```powershell
docker compose down
docker compose down -v
```

- `down` keeps database volume
- `down -v` removes all local Airflow metadata data

## Notes

- This uses `LocalExecutor` for easier learning on one machine.
- You can add new DAG files under `dags/` and Airflow will auto-discover them.
