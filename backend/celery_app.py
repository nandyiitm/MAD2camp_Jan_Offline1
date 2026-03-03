from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    'tasks', 
    broker='redis://localhost:6379/0')

celery_app.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False
)

import time
from mail import send_email

@celery_app.task(name='tasks.create_report')
def create_report(user_email):
    print(f"Creating report for user: {user_email}")
    time.sleep(10)  # Simulate time-consuming task

    send_email("Your report is ready", "Please find your report attached. <a href='http://localhost:5000/static/hello.csv'>Download CSV</a>", user_email) 

    return f"Report created successfully for user: {user_email}"


