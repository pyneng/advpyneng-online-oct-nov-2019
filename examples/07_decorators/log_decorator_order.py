from functools import wraps


def log(func):
    print(f'log: Декорируем функцию {func.__name__} с помощью log')
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'>>> log: Вызываю функцию {func.__name__}')
        result = func(*args, **kwargs)
        print(f'<<< log: получили результат функции {func.__name__}')
        return result
    return inner


def log_args(func):
    print(f'log_args: Декорируем функцию {func.__name__} с помощью log_args')
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'>>> log_args: Аргументы функции {func.__name__} {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'<<< log_args: получили результат функции {func.__name__}')
        return result
    return inner

@log_args
@log
def upper(string):
    return string.upper()


def lower(string):
    return string.lower()

def capitalize(string):
    return string.capitalize()
