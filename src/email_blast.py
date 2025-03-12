# Module for actual sending function
import smtplib

# Email functions we need
from email.message import EmailMessage
import datetime
import os

# In-house functions
import formatter
from user import User

user1 = User('Josh', 'Nijjar', 600, 'BBC Business', ['ANET', 'MSFT', 'FTNT'], 'GU151NA',
             'joshnijjar@gmail.com')


def format_email(user):
    """Sends a user's daily brief to them"""

    emailer = 'joshnijjar@gmail.com'

    brief = formatter.plain_text_formatter(user)
    html_brief = formatter.html_formatter(user)
    

    message = EmailMessage()
    message['Subject'] = f"Your Daily Brief for: {datetime.date.today()}"
    message['from'] = emailer
    message['to'] = user.email
    message.set_content(brief)
    message.add_alternative(html_brief, subtype='html')

    return message

def send_email(message, user):
    emailer = 'joshnijjar@gmail.com'
    emailer_password = os.environ.get('GOOGLE_APP_PASS')

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(emailer, emailer_password)
        server.sendmail(emailer, user.email, message.as_string())
        server.quit()
        print(f"Email sent successfully")
    except Exception as e:
        print(f'Failed to send email: {e}')

send_email(format_email(user1), user1)













