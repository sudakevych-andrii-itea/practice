# Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.


class CustomList:
    def __init__(self, *args):
        self.my_custom_list = [*args]

    def __str__(self):
        return f'{self.my_custom_list}'

    def __add__(self, other):
        return CustomList(*self.my_custom_list + other.my_custom_list)

    def get_list(self):
        return self.my_custom_list

    def append(self, value):
        self.my_custom_list = self.my_custom_list + [value]

    def pop(self, index=None):
        if index is not None:
            self.my_custom_list = self.my_custom_list[0:index] + self.my_custom_list[index + 1:len(self.my_custom_list)]
        else:
            self.my_custom_list = self.my_custom_list[0:-1]

    def insert(self, index, element):
        self.my_custom_list = self.my_custom_list[0:index] + \
                              [element] + \
                              self.my_custom_list[index:len(self.my_custom_list)]

    def remove(self, element):
        ind = self.my_custom_list.index(element)
        self.my_custom_list = self.my_custom_list[0:ind] + self.my_custom_list[ind + 1:len(self.my_custom_list)]

    def clear(self):
        self.my_custom_list = []


if __name__ == '__main__':
    list1 = CustomList(1, 2, 3)
    list2 = CustomList(4, 5, 6)

    list1.append(33)
    list2.append(44)

    print(list1, list2)

    list1.pop()
    list2.pop(2)

    print(list1, list2)

    list1.remove(3)
    list2.remove(4)

    print(list1, list2)

    list1.insert(2, 23)
    list2.insert(3, 32)

    print(list1, list2)

    print(list1 + list2)
