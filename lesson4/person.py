from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    def __init__(self, surname, date_of_birth):
        self.surname = surname
        self.date_of_birth = date_of_birth

    @abstractmethod
    def get_info(self):
        pass

    def get_age(self):
        date_of_birth = self.date_of_birth.split('-')
        print(date_of_birth)
        return int((date.today() - date(1990, 7, 3)).days / 365)


class Enrollee(Person):
    def __init__(self, surname, date_of_birth, faculty):
        super().__init__(surname, date_of_birth)
        self.faculty = faculty

    def get_info(self):
        return f'Surname: {self.surname}. ' \
               f'Date of birth: {self.date_of_birth}. ' \
               f'Faculty: {self.faculty}'


class Student(Person):
    def __init__(self, surname, date_of_birth, faculty, course):
        super().__init__(surname, date_of_birth)
        self.faculty = faculty
        self.course = course

    def get_info(self):
        return f'Surname: {self.surname}. ' \
               f'Date of birth: {self.date_of_birth}. ' \
               f'Faculty: {self.faculty}. Course: {self.course}'


class Teacher(Person):
    def __init__(self, surname, date_of_birth, faculty, position, experience):
        super().__init__(surname, date_of_birth)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def get_info(self):
        return f'Surname: {self.surname}. ' \
               f'Date of birth: {self.date_of_birth}. ' \
               f'Faculty: {self.faculty}.' \
               f'Position: {self.position}. Experience: {self.experience}'


enrollee = Enrollee('sdf', '1920-4-13', 'fac')
print(enrollee.get_info())
print(enrollee.get_age())
