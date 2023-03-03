from loguru import logger


logger.add('debug.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10:00', compression='zip')


def sym(num1, num2):
    return num1 / num2


try:
    sym(1, 0)
except Exception as err:
    logger.error(err)
