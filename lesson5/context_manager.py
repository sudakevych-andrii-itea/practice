# Написать свой контекстный менеджер для работы с файлами.

import os


class ContextManager:
    counter = 0

    def __init__(self):
        self.file_name = os.path.basename(__file__)
        self.new_file_name = f'{self.file_name[:-3]}_copy_{self.__class__.counter + 1}.py'

    def __enter__(self):
        self.open_file = open(self.file_name, 'r')
        self.create_file = open(self.new_file_name, 'w')
        return self.open_file, self.create_file

    def __exit__(self, *args):
        self.open_file.close()
        self.create_file.close()


if __name__ == '__main__':
    with ContextManager() as file:
        file[1].write(file[0].read())
