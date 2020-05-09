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
        date_of_birth = [int(i) for i in self.date_of_birth.split('-')]
        return int((date.today() - date(*date_of_birth)).days / 365)


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


def create_person(class_name, current_list, *args):
    current_list.append(class_name(*args))


def get_persons_info(persons_list):
    for person in persons_list:
        print(person.get_info())


def get_person_by_age(persons_list, first_age, last_age):
    for person in persons_list:
        if person.get_age() in range(first_age, last_age):
            print(person.get_info())


if __name__ == '__main__':
    person_list = []

    create_person(Enrollee, person_list, 'enrollee1', '1990-5-21', 'faculty1')
    create_person(Enrollee, person_list, 'enrollee2', '1989-5-21', 'faculty1')
    create_person(Enrollee, person_list, 'enrollee3', '2007-5-21', 'faculty2')
    create_person(Student, person_list, 'student1', '2010-12-1', 'faculty1', 'course1')
    create_person(Student, person_list, 'student2', '2010-8-1', 'faculty2', 'course2')
    create_person(Teacher, person_list, 'teacher1', '1980-5-2', 'faculty1', 'position1', '5')

    get_persons_info(person_list)

    get_person_by_age(person_list, 20, 35)
