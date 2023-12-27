from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

default_args = {
    'owner': 'klayut',
    'retry': 0,
    'retry_delay': timedelta(minutes=5)
}

def print_txt():
    a= []
    n = 10**3
    for i in range(n):
        a.append('A'*n)
    print(' HI !!!!!!!!')

with DAG(
    default_args=default_args,
    dag_id="print_hi",
    start_date=datetime.now(),
    schedule_interval='@daily' 
) as dag:
    task1 = PythonOperator(
        task_id='version_awscli',
        python_callable=print_txt,
        executor_config={
            "KubernetesExecutor": {
                "limit_memory": "512Mi",
            }
        })
    
    task1