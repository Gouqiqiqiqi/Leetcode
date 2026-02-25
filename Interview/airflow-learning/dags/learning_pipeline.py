from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract() -> dict[str, int]:
    records = [3, 7, 1, 9, 4]
    return {"count": len(records), "sum": sum(records)}


def transform(ti) -> dict[str, float]:
    extracted = ti.xcom_pull(task_ids="extract")
    average = extracted["sum"] / extracted["count"]
    return {"average": average}


def load(ti) -> None:
    transformed = ti.xcom_pull(task_ids="transform")
    print(f"Loaded metric -> average={transformed['average']:.2f}")


with DAG(
    dag_id="learning_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["learning", "example"],
) as dag:
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
