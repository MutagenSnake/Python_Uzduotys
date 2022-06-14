import math
import logging
from dalyba import return_division_result

# logging.basicConfig(filename='uzduotis.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__) # Pavadins pagal moduli
file_handler = logging.FileHandler("uzduotis.log")
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def return_sum(*args):
    logger.info(f'Skaiciu {args} suma lygi: {sum(args)}')
    return sum(args)

def return_square_root(number):
    try:
        logger.info(f'Skaiciaus {number} saknis lygi: {math.sqrt(number)}')
        return math.sqrt(number)
    except TypeError:
        logger.error(f'Saknis traukiama tik is skaiciu')

def return_length(sentence):
    logger.info(f'Sakinio "{sentence}" ilgis yra {len(sentence)} simboliai')
    return len(sentence)

return_sum(1,2,3,4,5)
return_square_root(25)
return_length("Darbas turi baigtis iki 17:00")

return_division_result(10,2)
