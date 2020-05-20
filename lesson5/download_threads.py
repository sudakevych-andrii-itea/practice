# Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё созданный декоратор. Создать список из 10
# ссылок, по которым будет происходить скачивание. Создать список
# потоков, отдельный поток, на каждую из ссылок. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.

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


def thread_decorator(thread_name, is_daemon):
    def inner_thread_decorator(func):
        def wrapper(index, *args):
            threads_list = []
            t = Thread(target=func, args=(index, *args), daemon=is_daemon)
            t.setName(f'{thread_name}-{index + 1}')
            threads_list.append(t)
            t.start()
        return wrapper
    return inner_thread_decorator


@thread_decorator(f'image-thread', False)
def download_image(index, link):
    print(f'thread-{index + 1} started with link {link} \n')
    image = requests.get(link)
    image_format = link[-3:len(link)]
    open(f'./python{index + 1}.{image_format}', 'wb').write(image.content)
    print(f'thread-{index + 1} finished')


for ind, item in enumerate(links_list):
    download_image(ind, item)
