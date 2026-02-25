'''
Question:

Share your initial thoughts on what this code is intended to do.

You mentioned the code defines an ETL pipeline using Apache Airflow and connects to a SQL database.

Can you walk me through what each of the three main functions, extract, transform, and load, are doing in this pipeline?

Please describe the purpose of each step and how data flows between them.

Please continue walking me through what each step does in this pipeline, starting with the extract function, then transform, and finally load.

Let me know what you think is happening in each, and how data moves from one to the next.

Now looking closer at the transform function, how confident are you that the data is being processed as intended, 
particularly considering how the select statement is returning data?

What kind of structure do you think the variable data has at this point, and how does that affect the result of d.upper for each element?

Now, considering how cursor dot fetchall returns a list of tuples, what do you expect will happen in the 
transform function when it does d dot upper for each d in data?

Do you see any issues with how the code processes that structure?

Thank you for your answer.

Given that each element in data is a tuple, what do you think would happen if you tried to call upper directly on the tuple?

How might you adjust the code so that only the string data values are transformed to uppercase, 
while preserving the associated IDs for loading later?

I can see your screen clearly.

Picking up from where you left off, you mentioned using a dictionary.

How would you modify the transform logic so that each tuple’s string value gets uppercased but its ID is preserved?

What would your processed data structure look like before passing it to the load step?

For example, describe how you would change the transform function so that it produces a data structure where each ID is linked to its uppercased data value.

What format would you use to make this clear for the next step, and how would you pass it along to the load function?

You could create a processed list where each element is a tuple or dictionary containing the ID and the uppercased data value, for example as pairs like (d[0], d[1].upper()) for each d in data.

Now, after transforming the data this way, how would you pass your processed results from the transform function to the load function in this Airflow pipeline?

What mechanism ensures the load step receives the transformed output?'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from datetime import datetime

def extract(**kwargs):
    pg = PostgresHook(postgres_conn_id='postgres_local')  # fetch raw records for the execution date
    conn = pg.get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, data FROM raw_table WHERE date = %s', kwargs['ds'])
    kwargs['ti'].xcom_push(key='raw', value=cursor.fetchall())

def transform(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract', key='raw')
    processed = [d.upper() for d in data]  # supposed to uppercase the data

def load(**kwargs):
    container = WasbHook(wasb_conn_id='azure_blob').get_conn()  # upload transformed data to Azure Blob
    blob_client = container.get_blob_client('data', 'processed.json')
    blob_client.upload_blob(processed)

with DAG('etl_pipeline', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract)
    transform = PythonOperator(task_id='transform', python_callable=transform)
    load = PythonOperator(task_id='load', python_callable=load)
    extract >> transform >> load


'''
Airflow = Apache Airflow is an open-source platform to programmatically author, 
schedule, and monitor workflows. It allows you to define complex data pipelines as code and manage their execution.
'''