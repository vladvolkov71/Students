# Домашнее задание № 1 к занятиям по ООП

## Общая архитектура
1. Все определения классов, функции и полевые испытания реализованы в одном файле Students.py

### Общая информация
1. Общая схема наследования:
      - Students
      - Mentor -> Reviewer
      - Mentor -> Lecturer
   
2. Для всех классов переопределены магические методы сравнения и вывода информации в соответствии с заданием.

### Краткие характеристики классов

#### Класс Student

Класс студентов. В нем определяются аргументы и методы для студентов:  
Инициализация - вводятся имя, фамилия и пол студента. Кроме того создаются:
- список активных курсов (courses_in_progress),
- множество законченных курсов (finished_courses),
- словарь из списков оценок за ДЗ по каждому активному курсу,
- словарь средних оценок за ДЗ по каждому курсу.  
Методы:
- add_courses - позволяет добавить учебные курсы, на которых учится студент
- rate_lect - позволяет студентам выставлять оценки лекторам. При выставлении каждой оценки пересчитывается средний балл.

#### Класс Mentor

Родительский класс для всех преподавателей. В него входят лекторы и ревьюверы.  
При инициализации вводятся имя, фамилия.  
Кроме того, содержит аргумент courses_attached, который содержит список курсов, с которыми работает преподаватель.
#### Класс Reviewer

Класс ревьюверов, оценивающих домашнее задание. Дочерний класс от Mentor.  
Содержит следующие аргументы и методы:
При инициализации, от родительского класса передаются имя, фамилия и список курсов.  
Содержит метод rate_st, который позволяет выставлять оценки студентам. При выставлении каждой оценки пересчитывается средний балл по каждому предмету и в случае превышения количества оценок 10 и среднем балле выше 5, курс считается пройденным и попадает в множество пройденных курсов студента.

#### Класс Lecturer

Класс лекторов. Читают лекции (ведут факультативы ;-)). Дочерний класс от Mentor.
При инициализации, от родительского класса передаются имя, фамилия и список курсов.
Содержат два аргумента-словаря: 
- grades_lect - содержит оценки по каждому курсу
- s_grades_lect - содержит средние оценки по каждому курсу

#### Дополнительные функции

Реализованы две отдельные функции:
- s_rate_st - для вычисления среднего балла по предмету и у студентов,
- s_rate_lect - для вычисления среднего балла по предмету у лекторов.

#### Полевые испытания

1. Инициализация 2 студентов. Добавление списка активных курсов.
2. Инициализация 2 лекторов. Добавление списка активных курсов.
3. Инициализация 2 ревьюверов. Добавление списка активных курсов.
4. Внесение данных оценок лекторов по всем предметам и всем студентам (используется генератор случайных чисел).
5. Внесение данных оценок студентам по всем предметам и всем ревьюверам (используется генератор случайных чисел).
6. Вывод всех оценок лекторов
7. Вывод всех оценок студентов
8. Вывод всех классов (через переопределенный __str__) в соответствии с заданием
9. Сравнение студентов по средней оценке за дз по ВСЕМ предметам.
10. Сравнение лекторов по средней оценке за лекции по ВСЕМ предметам.  

З.Ы. Список оцениваемых курсов у преподавателей и студентов совпадают.
З.З.Ы Файл requirements.txt сгенерирован и прилагается. 

