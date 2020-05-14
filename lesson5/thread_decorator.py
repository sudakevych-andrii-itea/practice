from threading import Thread


def thread_decorator(thread_name, is_daemon):
    def inner_thread_decorator(func):
        def wrapper(*args):
            print(f'{thread_name} started')
            t = Thread(target=func, args=args, daemon=is_daemon)
            t.start()
            print(f'{thread_name} finished')
        return wrapper
    return inner_thread_decorator


@thread_decorator('thread1', True)
def some_func(name):
    print(f'Hello, {name}')


some_func('Andrii')
