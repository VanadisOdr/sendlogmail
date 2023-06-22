from loguru import logger
from notifiers.logging import NotificationHandler
import os
from dotenv import load_dotenv

load_dotenv()

def notify_mail():  # GOOGLE MAIL TODO: найти более лучший способ отправки уведомлений
    params = {
        "from": os.getenv('MAIL2'),
        "to": os.getenv('ERROR_ADDR_TO'),
        "host": "smtp.mail.ru",
        "port": 465,
        "ssl": True,
        "tls": True,
        "subject": "loguru",
        "username": os.getenv('MAIL2'),
        "password": os.getenv('PASSWORD')
    }
    handler = NotificationHandler(provider='email', defaults=params)
    logger.add(handler, level="ERROR")



notify_mail()

@logger.catch(Exception)
def sym(num1, num2):
    return num1 / num2

try:
    sym(1, 0)
except Exception as err:
    logger.error(err)
