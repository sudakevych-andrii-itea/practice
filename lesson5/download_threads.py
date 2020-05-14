import time

import requests
from threading import Thread

links_list = [
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
    'https://andreyex.ru/wp-content/uploads/2020/02/Kak-udalit-fajly-i-katalogi-v-Python.jpg',
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
    'https://udemy-images.udemy.com/course/750x422/507888_17b7_2.jpg',
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
    'https://media.proglib.io/wp-uploads/2018/09/ciwlCWa.png',
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
    'https://s3.tproger.ru/uploads/2018/04/python-dictionary-880x308.png',
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
    'https://media.proglib.io/wp-uploads/2019/04/Python.jpg',
]

threads_list = []


def thread_decorator(thread_name, is_daemon):
    def inner_thread_decorator(func):
        def wrapper(*args):
            print(f'{thread_name}{args[0] + 1} started')
            t = Thread(target=func, args=args, daemon=is_daemon)
            threads_list.append(t)
            t.start()
            print(f'{thread_name}{args[0] + 1} finished')
        return wrapper
    return inner_thread_decorator


@thread_decorator(f'thread', False)
def download_image(index, link):
    image = requests.get(link)
    image_format = link[-3:len(link)]
    open(f'img/python{index + 1}.{image_format}', 'wb').write(image.content)


for ind, item in enumerate(links_list):
    download_image(ind, item)
