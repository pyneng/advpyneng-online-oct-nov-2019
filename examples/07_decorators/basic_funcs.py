from functools import wraps

def log(func):
    print(f'log: Декорирую функцию {func} с помощью log')
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__}')
        return func(*args, **kwargs)
    return inner

def log_args(func):
    print(f'log_args: Декорирую функцию {func} с помощью log_args')
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'Аргументы args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return inner

@log_args
@log
def upper(string):
    "Конвертируем строку в upper"
    return string.upper()
#upper = log_args(log(upper))


@log
def lower(string):
    return string.lower()
#lower = log(lower)


@log
def capitalize(string):
    return string.capitalize()
