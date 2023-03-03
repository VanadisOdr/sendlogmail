import notifiers
from dotenv import load_dotenv
import os
from loguru import logger


load_dotenv()

params_mail = {
        "from": os.getenv('MAIL2'),
        "to": os.getenv('MAIL'),
        "host": "smtp.mail.ru",
        "port": 578,
        "subject": "loguru",
        "username": os.getenv('MAIL2'),
        "password": os.getenv('PASSWORD')
}
# Send a single notification

notifiers.get_notifier("email").notify(message="The application is running!", **params_mail)

from notifiers.logging import NotificationHandler
handler = NotificationHandler(provider='email', defaults=params_mail)
logger.add(handler, level="ERROR")