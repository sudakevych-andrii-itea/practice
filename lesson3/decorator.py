import random


def outer_decorator(iters):

    def inner_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            func_name = func.__name__
            result = []
            start = time.time()
            for i in range(iters):
                result.append(func(*args, **kwargs))
            end = time.time()
            exec_time = round((end - start) * 1000)
            return f'Function {func_name} completed {iters} times in {exec_time}ms.\nWith result: {result}'

        return wrapper

    return inner_decorator


@outer_decorator(5)
def create_random_lists(rand_range, count):
    return [random.randrange(rand_range) for _ in range(count)]


if __name__ == '__main__':
    print(create_random_lists(100, 1000))
