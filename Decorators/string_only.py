def string_only(func):
    def wrapper(*args, **kwargs):
        for item in args:
            if type(item) != str:
                return 'Found something besides strings'
        return func(*args, **kwargs)
    return wrapper

@string_only
def tester(*args):
    string_list = []
    for item in args:
        string_list.append(item)
    return string_list

print(tester('one','two','three'))