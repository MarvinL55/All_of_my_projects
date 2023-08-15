import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.critical("Critical error! Critical error")

logging.disable(logging.CRITICAL)

logging.critical("Critical error! Critical error")

logging.error("ERROR ERROR")