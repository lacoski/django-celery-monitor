python3.6 -m venv env

django-admin startproject mysite

python3 manage.py runserver

celery -A project worker -l info


from demos.tasks import add, sleep_task
run = sleep_task.s()
run_task = run.apply_async()

run1 = add.s(2,2)
run_task1 = run1.apply_async()

celery -A project worker -l info
celery -A project flower