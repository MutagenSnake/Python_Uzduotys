def two_max_decorator(func):
    def wrapper(*args, **kwargs):
        if len(args) > 2:                    #Kodėl neveikia kai:  if len(args) or len(kwargs) > 2:
            return 'Must be no more than two arguments'
        return func(*args, *kwargs)
    return wrapper

@two_max_decorator
def tester(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(tester(1,2,3))