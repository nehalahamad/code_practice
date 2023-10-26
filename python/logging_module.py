import logging

logging.basicConfig(level=logging.INFO, filename='log_1.log', filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ------------------------------------------
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# ------------------------------------------
# x = 15
# logging.info(f'the value of x is: ')
# ------------------------------------------

logger = logging.getLogger(__name__)
try:
    1/0
except Exception as e:
    logger.exception(e)
# ------------------------------------------


