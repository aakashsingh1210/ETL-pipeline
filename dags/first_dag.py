from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.insert(1, "/home/uslsz344/Desktop/practise/assignment_test/code")
index=1

from structurized.main import main as main1
from operation.main import main as main2





with DAG(
    
    dag_id="assignment_test",
    description="optimising the assignment test",
    start_date=datetime(2022,10,17),
    schedule_interval=None,
    catchup=False,
) as dag:
    task1=PythonOperator(
        task_id="test_task1",
        python_callable=main1,    #calling main function inside dag
        op_kwargs={'index':index,},
    )
    task2=PythonOperator(
        task_id="test_task2",
        python_callable=main2,     #calling main function inside dag
        op_kwargs={'index':index,},
    )

    task1>>task2