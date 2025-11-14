from functools import wraps


def check_arguments(*types):
    def check(func):
        @wraps(func)
        def wrapper(*args):
            if len(types) > len(args):
                raise TypeError
            for i in range(len(types)):
                if not isinstance(args[i], types[i]):
                    raise TypeError
            func(*args)
        return wrapper
    return check


@check_arguments(int, str)
def hello(n, s):
    print(n, s)


@check_arguments(int)
def some_name(a):
    "Some doc."
    print(a)


print(some_name.__name__)
print(some_name.__doc__)

hello(1, 'sdws')
