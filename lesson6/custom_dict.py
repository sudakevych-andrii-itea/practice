# Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.


class CustomDict:
    def __init__(self, **kwargs):
        self.my_custom_dict = {**kwargs}

    def __str__(self):
        return f'{self.my_custom_dict}'

    def __add__(self, other):
        return CustomDict(**self.my_custom_dict, **other.my_custom_dict)

    def get(self, key):
        if key in [*self.my_custom_dict]:
            return self.my_custom_dict[key]
        return None

    def keys(self):
        return [*self.my_custom_dict]

    def values(self):
        return [self.my_custom_dict[k] for k in self.keys()]

    def items(self):
        return [(k, self.my_custom_dict[k]) for k in self.keys()]

    def clear(self):
        self.my_custom_dict = {}


if __name__ == '__main__':
    dict1 = CustomDict(country='Ukraine', capital='Kiev')
    dict2 = CustomDict(name='Bob', age=45)

    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())

    print(dict1 + dict2)
