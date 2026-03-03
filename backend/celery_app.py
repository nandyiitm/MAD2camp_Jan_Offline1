from datetime import timedelta

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


@celery_app.task(name='tasks.send_daily_reminders')
def send_daily_reminders():
    from models import User
    from app import app
    with app.app_context():
        for user in User.query.all():
            send_email("Daily Reminder", "This is your daily reminder email.", user.email)
    return f"Daily reminders sent to all users."

celery_app.conf.beat_schedule = {
    'daily_reminder': {
        'task': 'tasks.send_daily_reminders',
        # 'schedule': crontab(hour=18, minute=8),  # Every day at 9:00 AM
        'schedule': timedelta(seconds=3),  # For testing, run every 30 seconds
    }
}