import time

def delay_three_seconds(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        print('Delay works!')
        return func(*args, **kwargs)
    return wrapper



@delay_three_seconds
def tester(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(tester(1,2,3))