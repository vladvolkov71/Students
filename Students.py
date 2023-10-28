from functools import total_ordering
from random import randint


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = set()
        self.courses_in_progress = []
        self.grades_stud = {}
        self.s_grades_stud = {}

    def __eq__(self, other):
        if isinstance(other, Student):
            return sum(self.s_grades_stud.values()) / len(self.s_grades_stud) == sum(
                other.s_grades_stud.values()) / len(other.s_grades_stud)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return sum(self.s_grades_stud.values()) / len(self.s_grades_stud) < sum(other.s_grades_stud.values()) / len(
                other.s_grades_stud)
        return NotImplemented

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def __str__(self):
        return (f"Студент:\n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.s_grades_stud}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(sorted(self.finished_courses))}\n")

    def rate_lect(self, lect, course, grade):
        if isinstance(lect,
                      Lecturer) and course in self.courses_in_progress and course in lect.courses_attached and 1 <= grade <= 10:
            if course in lect.grades_lect:
                lect.grades_lect[course].append(grade)
            else:
                lect.grades_lect[course] = [grade]
            lect.s_grades_lect[course] = s_rate_lec(lect, course)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}
        self.s_grades_lect = {}

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return sum(self.s_grades_lect.values()) / len(self.s_grades_lect) == sum(
                other.s_grades_lect.values()) / len(other.s_grades_lect)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return sum(self.s_grades_lect.values()) / len(self.s_grades_lect) < sum(other.s_grades_lect.values()) / len(
                other.s_grades_lect)
        return NotImplemented

    def __str__(self):
        return (f"Лектор:\n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.s_grades_lect}\n")


class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades_stud:
                student.grades_stud[course] += [grade]
            else:
                student.grades_stud[course] = [grade]
            student.s_grades_stud[course] = s_rate_st(student, course)
        else:
            return 'Ошибка'

        if len(student.grades_stud[course]) >= 10 and s_rate_st(student, course) >= 5:
            student.finished_courses.add(course)

    def __str__(self):
        return (f"Ревьювер:\n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


def s_rate_st(st, c):
    return round(sum([_ for _ in st.grades_stud[c]]) / len(st.grades_stud[c]), 2)


def s_rate_lec(lec, c):
    return round(sum([_ for _ in lec.grades_lect[c]]) / len(lec.grades_lect[c]), 2)


# Инициализация студентов.
student1 = Student('Елена', 'Иванова', 'жен.')
student1.courses_in_progress += ['Python', 'Введение в программирование']

student2 = Student('Коля', 'Маслов', 'муж.')
student2.courses_in_progress += ['Python', 'Введение в программирование']

# Инициализация лекторов.
lecturer1 = Lecturer('Жуль', 'Верн')
lecturer1.courses_attached += ['Python', 'Введение в программирование', 'За 80 дней вокруг света (факультатив)']

lecturer2 = Lecturer('Томас', 'де Торквемада')
lecturer2.courses_attached += ['Введение в программирование', 'Python', 'Методы инквизиции (факультатив)']

# Инициализация ревьюверов.
reviewer1 = Reviewer('Иван', 'Петров')
reviewer1.courses_attached += ['Python', 'Введение в программирование']

reviewer2 = Reviewer('Дмитрий', 'Иванов')
reviewer2.courses_attached += ['Python', 'Введение в программирование']

# Внесение данных оценок лекторов.
for number in range(11):
    for cour in lecturer1.courses_attached:
        student1.rate_lect(lecturer1, cour, randint(1, 10))
        student2.rate_lect(lecturer1, cour, randint(1, 10))
    for cour in lecturer2.courses_attached:
        student1.rate_lect(lecturer2, cour, randint(1, 10))
        student2.rate_lect(lecturer2, cour, randint(1, 10))

# Внесение данных оценок студентов.
for number in range(11):
    for cour in reviewer1.courses_attached:
        reviewer1.rate_st(student1, cour, randint(1, 10))
        reviewer1.rate_st(student2, cour, randint(1, 10))
    for cour in reviewer2.courses_attached:
        reviewer2.rate_st(student1, cour, randint(1, 10))
        reviewer2.rate_st(student2, cour, randint(1, 10))

# Вывод всех оценок лекторов
print(f"Оценки лектора {lecturer1.surname} за лекции курсам:\n"
      f"{lecturer1.grades_lect}")
print(f"Оценки лектора {lecturer2.surname} за лекции курсам:\n"
      f"{lecturer2.grades_lect}")
# Вывод всех оценок студентов
print(f"Оценки студента {student1.surname} за лекции курсам:\n"
      f"{student1.grades_stud}")
print(f"Оценки студента {student2.surname} за лекции курсам:\n"
      f"{student2.grades_stud}")

# Вывод всех классов
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
# Сравнение студентов по средней оценке за дз по всем предметам.
print("Сравнение студентов:\n"
      f"{student1.name} {student1.surname} < {student2.name} {student2.surname} - {student1 < student2}\n"
      f"{student1.name} {student1.surname} == {student2.name} {student2.surname} - {student1 == student2}\n"
      f"{student1.name} {student1.surname} > {student2.name} {student2.surname} - {student1 > student2}\n")

# Сравнение лекторов по средней оценке за лекции по всем предметам.
print("Сравнение преподавателей:\n",
      f"{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} - {lecturer1 < lecturer2}\n"
      f"{lecturer1.name} {lecturer1.surname} == {lecturer2.name} {lecturer2.surname} - {lecturer1 == lecturer2}\n"
      f"{lecturer1.name} {lecturer1.surname} > {lecturer2.name} {lecturer2.surname} - {lecturer1 > lecturer2}\n")
