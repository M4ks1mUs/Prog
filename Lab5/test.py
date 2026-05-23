import threading
from functools import wraps

def decorator(_func=None, *, repeat=1):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(repeat):
                result = func(*args, **kwargs)
            return result
        return wrapper
    
    if _func is not None and callable(_func):
        return actual_decorator(_func)
    
    return actual_decorator

def run_async(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

def create_file_logger(filename):
    file = open(filename, 'a', encoding='utf-8')
    @run_async
    def logger(value):
        file.write(f"{value}\n")
        file.flush()
        return f"Записано: {value}"
    return logger

log = create_file_logger("Lab5/text.txt")


@decorator
def hello(name):
    log(f'Hello, {name}')

@decorator(repeat=3)
def bye(name):
    log(f"Bye, {name}")

hello("Alice")
bye("Bob")


@decorator(repeat=1)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

log(factorial(5))