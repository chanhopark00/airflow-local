'''
- 함수 내부 연산의 결과에 의해 조건부로 task를 선택하여 진행 (의존성 컨트롤)
'''
# 1. 모듈 가져오기
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

# 2. DAG 정의
with DAG() as dag:
    # 3. task 정의
    task_extract    = PythonOperator()
    task_trasform   = PythonOperator()
    task_load       = PythonOperator()

    # 4. 의존성 정의 -> 시나리오별 준비 
    task_extract >> task_trasform >> task_load