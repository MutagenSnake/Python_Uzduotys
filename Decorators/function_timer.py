import requests  # importuojame requests
from time import time  # importuojame time modulį

def function_timer(function):
    def wrapper(*args, **kwargs):
        zero_time = time()
        result = function(*args, **kwargs)
        final_time = time()
        total_time= final_time - zero_time
        print(total_time)
        print(f'"{function.__name__}" with parameters: {args, kwargs} runtime is {total_time} seconds.')
        return result
    return wrapper


@ function_timer
def print_status():
    r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
    print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)

@ function_timer
def find_prime_numbers(first, last):
    for number in range(first, last):
        for tester_number in range(2, number):
            if number%tester_number == 0:
                break
        else:
            print(number)


# print_status()
find_prime_numbers(1000,10000)