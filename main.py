from loguru import logger
import notifiers
from dotenv import load_dotenv
import os


logger.add('debug.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10:00', compression='zip')



@logger.catch(Exception)
def sym(num1, num2):
    return num1 / num2


try:
    sym(1, 0)
except Exception as err:
    logger.error(err)

load_dotenv()


params_mail = {
    "from": os.getenv('MAIL2'),
    "to": os.getenv('MAIL'),
    "host": "smtp.mail.ru",
    "port": 465,
    "ssl": True,
    "tls": True,
    "subject": "loguru",
    "username": os.getenv('MAIL2'),
    "password": os.getenv('PASSWORD'),
}
# Send a single notification

notifiers.get_notifier("email").notify(message='The app is running!',attachments=['C:/Users/olegg/PycharmProjects/sendlogmail/debug.log'], raise_on_errors=True, **params_mail)

from notifiers.logging import NotificationHandler
handler = NotificationHandler(provider='email', defaults=params_mail, )
logger.add(handler, level="ERROR")