from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import os

default_args = {
    'owner': 'klayut',
    'retry': 0,
    'retry_delay': timedelta(minutes=5)
}

def print_txt():
    print(' HI !!!!!!!!')

with DAG(
    default_args=default_args,
    dag_id="version_awscli_v01",
    start_date=datetime.now(),
    schedule_interval='@daily' 
) as dag:
    task1 = PythonOperator(
        task_id='version_awscli',
        python_callable=print_txt)
    
    task1  