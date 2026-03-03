import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@gmail.com'

def send_email(subject, body, to_email):
    mail = MIMEMultipart()
    mail['Subject'] = subject
    mail['From'] = FROM_EMAIL
    mail['To'] = to_email

    # Add body to email
    mail.attach(MIMEText(body, 'html'))  # Use 'html' for HTML content

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(mail)
    print("Email sent successfully!")



def send_daily_reminders():
    from app import app
    from models import User
    
    with app.app_context():
        users = User.query.all()
        for user in users:
            send_email("Daily Reminder", "This is your daily reminder email.", user.email)

if __name__ == "__main__":
    print('mail.py is running directly...')
    send_daily_reminders()
else:
    print('mail.py is imported as a module...')