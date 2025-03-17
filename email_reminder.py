import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials (use environment variables for security)
YOUR_EMAIL = "your_email@gmail.com"  # Replace with your email
YOUR_PASSWORD = "your_app_password"  # Use an App Password, NOT your main password

# Recipient's email
TO_EMAIL = "recipient@example.com"  # Replace with the recipient's email

# Email subject and message
SUBJECT = "Unpaid Salary Reminder"
BODY = """Dear [Recipient],

I hope you’re doing well.  

This is an automated reminder regarding an outstanding payment. Please process it at your earliest convenience to avoid further reminders.  

Best regards,  
[Your Name]  
"""

# Function to send email
def send_email():
    try:
        msg = MIMEMultipart()
        msg["From"] = YOUR_EMAIL
        msg["To"] = TO_EMAIL
        msg["Subject"] = SUBJECT
        msg.attach(MIMEText(BODY, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, TO_EMAIL, msg.as_string())

        print("✅ Reminder email sent successfully.")
    
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Run daily until stopped manually
while True:
    send_email()
    print("⏳ Waiting 24 hours before the next email...")
    time.sleep(86400)  # Wait for 24 hours
