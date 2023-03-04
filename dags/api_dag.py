# import json
# from datetime import datetime
# from airflow.models import DAG
# from airflow.providers.http.sensors.http import HttpSensor
# from airflow.providers.http.operators.http import SimpleHttpOperator
# from airflow.operators.python import PythonOperator

# with DAG(
#     dag_id='api-dag',
#     schedule_interval='@daily',
#     start_date=datetime(2023,1,6),
#     catchup=False
    
# ) as dag:
#     task_is_api_active=HttpSensor(
#         task_id='is_api_active',
#         http_conn_id='api_post_demo',
#         endpoint='posts/'
#     )
#     task_get_post=SimpleHttpOperator(
#         task_id='get_post',
#         http_conn_id='api_post_demo',
#         endpoint='posts/',
#         method='GET',
#         response_filter=lambda response:json.loads(response.txt),
#         log_response=True
        
#     )