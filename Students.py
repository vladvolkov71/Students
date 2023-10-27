class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_end = []
        self.courses_in_progress = []
        self.grades_stud = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания:\n"
                f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {','.join(self.courses_end)}")

    def rate_lect(self, lect, course, grade):
        if isinstance(lect, Lecturer) and course in self.courses_in_progress and course in lect.courses_attached:
            if course in lect.grades_lect:
                lect.grades_lect[course] += [grade]
            else:
                lect.grades_lect[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции:\n")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_stud:
                student.grades_stud[course] += [grade]
            else:
                student.grades_stud[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания.
# __________3____________
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
# 1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);
# 2. для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 5)

best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 6)

print(cool_lecturer.grades_lect)
print(best_student.grades_stud)
print(best_student)
print(cool_lecturer)
print(cool_lecturer)
