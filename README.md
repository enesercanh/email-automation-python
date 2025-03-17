# Automated Email Reminder Bot

This Python script sends automated daily email reminders using Gmail's SMTP server. It is useful for sending payment reminders or any other scheduled notifications.

## Features
- Sends daily email reminders automatically.
- Uses Gmail's SMTP server with SSL encryption.
- Customizable email sender, recipient, subject, and body.
- Runs indefinitely until manually stopped.

## Requirements
- Python 3.x
- A Gmail account (App Password recommended)

## Setup Instructions

### 1. Enable App Passwords in Gmail
To use this script securely, enable **App Passwords** in your Gmail account:
1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification** if not already enabled.
3. Under "Signing in to Google," select **App Passwords**.
4. Create an App Password and copy it for use in this script.

### 2. Install Required Libraries
Ensure you have Python installed. The required libraries (`smtplib`, `email`, and `time`) come with Python by default, so no additional installation is needed.

### 3. Configure the Script
Edit the script to replace the placeholders with your actual email credentials and recipient's email:
```python
YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_app_password"
TO_EMAIL = "recipient@example.com"
```
- **YOUR_EMAIL**: Your Gmail address.
- **YOUR_PASSWORD**: Your generated App Password.
- **TO_EMAIL**: The recipient's email.

### 4. Run the Script
Execute the script using:
```bash
python email_reminder_bot.py
```
The script will send an email every 24 hours until manually stopped.

## Security Recommendations
- **DO NOT** use your main Gmail password in the script. Always use an App Password.
- Consider storing credentials in environment variables instead of hardcoding them.
- Use a secure email provider if handling sensitive data.

## Disclaimer
This script is intended for personal and ethical use. Ensure compliance with local email regulations and avoid spamming recipients.

