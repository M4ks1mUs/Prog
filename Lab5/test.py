import threading

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

log([3, 1, 5])
log('Hello')
log(32)
log('Привет')
print("Основной поток свободен!")