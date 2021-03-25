from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


default_args = {
    'retry':5,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email_on_retry': True,
    'email': 'admin@amadous.com'
}

def _downloading_data_form_S3():
    print("downloading data from S3")

def _checking_data_informatica():
    print('checking data informatica')

def _processing_data_emr_spark():
    print("processing data")

def _writing_data_to_Teradata():
    print("writing data to Teradata")

with DAG(dag_id='amadeus', default_args=default_args, schedule_interval="*/10 * * * *",
    start_date=datetime(2021, 1, 1), catchup=True, max_active_runs=2) as dag:
    
    downloading_data_form_S3 = PythonOperator(
        task_id = 'downloading_data_form_S3',
        python_callable=_downloading_data_form_S3,
    )
    
    checking_data_informatica = PythonOperator(
        task_id='checking_data_informatica',
        python_callable=_checking_data_informatica
    )

    writing_data_to_Teradata = PythonOperator(
        task_id='writing_data_to_Teradata',
        python_callable=_writing_data_to_Teradata
    )

    processing_data_emr_spark = PythonOperator(
        task_id='processing_data_emr_spark',
        python_callable=_processing_data_emr_spark
    )

    downloading_data_form_S3 >> [ checking_data_informatica, processing_data_emr_spark ] >> writing_data_to_Teradata