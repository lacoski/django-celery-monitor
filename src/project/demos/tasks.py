from celery import shared_task, task
import time

@task
def add(x, y):
    return x + y

@task
def sleep_task():
    time.sleep(10)
    return True