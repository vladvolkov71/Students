class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_stud = {}
        self.s_grades_stud = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.s_grades_stud}\n"
                f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {','.join(self.finished_courses)}")

    def rate_lect(self, lect, course, grade):
        if isinstance(lect,
                      Lecturer) and course in self.courses_in_progress and course in lect.courses_attached and 1 <= grade <= 10:
            if course in lect.grades_lect:
                lect.grades_lect[course].append(grade)
            else:
                lect.grades_lect[course] = [grade]
            lect.s_grades_lect[course] = s_rate_lect(lect, course)
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
        self.s_grades_lect = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
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

        if len(student.grades_stud[course]) == 10:
            student.add_courses(course)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


def s_rate_st(s, c):
    return sum([i for i in s.grades_stud[c]]) / len(s.grades_stud[c])


def s_rate_lect(l, c):
    return sum([j for j in l.grades_lect[c]]) / len(l.grades_lect[c])


# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания.
# __________3____________


student1 = Student('Ruoy', 'Eman', 'female')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Введение в программирование']

student2 = Student('Mac', 'Duck', 'male')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Введение в программирование']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Nic', 'Name')
reviewer2.courses_attached += ['Введение в программирование']

lecturer1 = Lecturer('Ivan', 'Petrov')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Введение в программирование']

lecturer2 = Lecturer('Dmitry', 'Ivanov')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Введение в программирование']

reviewer1.rate_st(student1, 'Python', 7)
reviewer1.rate_st(student1, 'Python', 9)
reviewer1.rate_st(student1, 'Python', 7)
reviewer1.rate_st(student1, 'Python', 5)
reviewer1.rate_st(student1, 'Python', 3)
reviewer1.rate_st(student1, 'Python', 7)
reviewer1.rate_st(student1, 'Python', 7)
reviewer1.rate_st(student1, 'Python', 10)
reviewer1.rate_st(student1, 'Python', 6)
reviewer1.rate_st(student1, 'Python', 7)
reviewer1.rate_st(student1, 'Python', 15)

reviewer2.rate_st(student1, 'Введение в программирование', 7)
reviewer2.rate_st(student1, 'Введение в программирование', 5)
reviewer2.rate_st(student1, 'Введение в программирование', 7)
reviewer2.rate_st(student1, 'Введение в программирование', 5)
reviewer2.rate_st(student1, 'Введение в программирование', 2)
reviewer2.rate_st(student2, 'Введение в программирование', 7)
reviewer2.rate_st(student2, 'Введение в программирование', 9)
reviewer2.rate_st(student2, 'Введение в программирование', 10)

student1.rate_lect(lecturer1, 'Python', 10)
student1.rate_lect(lecturer1, 'Python', 7)
student1.rate_lect(lecturer1, 'Python', 10)
student1.rate_lect(lecturer1, 'Python', 9)
student1.rate_lect(lecturer1, 'Python', 10)
student1.rate_lect(lecturer1, 'Python', 9)
student1.rate_lect(lecturer1, 'Python', 3)
student1.rate_lect(lecturer1, 'Python', 9)
student1.rate_lect(lecturer1, 'Python', 15)

student2.rate_lect(lecturer2, 'Введение в программирование', 10)
student2.rate_lect(lecturer2, 'Введение в программирование', 7)
student2.rate_lect(lecturer2, 'Введение в программирование', 10)
student2.rate_lect(lecturer2, 'Введение в программирование', 9)
student2.rate_lect(lecturer2, 'Введение в программирование', 10)
student2.rate_lect(lecturer2, 'Введение в программирование', 9)
student2.rate_lect(lecturer2, 'Введение в программирование', 3)
student2.rate_lect(lecturer2, 'Введение в программирование', 9)
student2.rate_lect(lecturer2, 'Введение в программирование', 15)

print(lecturer1.grades_lect)
print(lecturer2.grades_lect)
print(student1.grades_stud)
print(student2.grades_stud)
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
