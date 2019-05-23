import logging

LOG_FORMAT = "%(asctime)s======%(levelname)s+++++++%(message)s"

logging.basicConfig(filename='log.log', level=logging.DEBUG, format=LOG_FORMAT)


logging.debug('this is a debug log')
logging.warning('this is a warning log')
logging.error('this is a error log')
logging.info('this is a info log')
logging.critical('this is a critical log')
