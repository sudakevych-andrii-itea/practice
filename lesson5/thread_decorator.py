# Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.

from threading import Thread


def thread_decorator(thread_name, is_daemon):
    def inner_thread_decorator(func):
        def wrapper(*args):
            t = Thread(target=func, args=args, daemon=is_daemon)
            t.setName(thread_name)
            t.start()
        return wrapper
    return inner_thread_decorator


@thread_decorator('thread1', False)
def some_func(name):
    print(f'Thread started')
    print(f'Hello, {name}')
    print(f'Thread finished')


some_func('Andrii')
