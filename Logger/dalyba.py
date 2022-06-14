import logging

# logging.basicConfig(filename='uzduotis.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logger2 = logging.getLogger(__name__) # Pavadins pagal moduli
file_handler = logging.FileHandler("uzduotis_dalyba.log")
logger2.addHandler(file_handler)

logger2.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger2.addHandler(stream_handler)

def return_division_result(a, b):
    try:
        logger2.info(f'Skaicius {a} padalintas is {b} yra lygu {a/b}')
        return a / b
    except ZeroDivisionError:
        logger2.error(f'Dalyba is nulio negalima')

# return_division_result(10,2)
# return_division_result(10,0)

print("Kodel dalyba.py pasileidzia?")