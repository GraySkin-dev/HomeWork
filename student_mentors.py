class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def rate_lesson(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        message = f"""\nИмя: {self.name}\nФамилия: {self.surname}\n"""\
            f"""Средняя оценка за домашние задания: """\
            f"""{calculate_average(self.grades)}\n"""\
            f"""Курсы в процессе изучения: {self.courses_in_progress}\n"""\
            f"""Завершенные курсы: {self.finished_courses}\n"""
        return message
 
    def __eq__(self, other):
        if isinstance(other, Student):
            return (calculate_average(self.grades) == 
                    calculate_average(other.grades))
        else:
            return 'Ошибка'
 
    def __lt__(self, other):
        if isinstance(other, Student):
            return (calculate_average(self.grades) < 
                    calculate_average(other.grades))
        else:
            return 'Ошибка'
 
    def __le__(self, other):
        if isinstance(other, Student):
            return (calculate_average(self.grades) <= 
                    calculate_average(other.grades))
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
        self.grades = {}
 
    def __str__(self):
        message = f"""\nИмя: {self.name}\nФамилия: {self.surname}\n"""\
            f"""Средняя оценка за лекции: """\
            f"""{calculate_average(self.grades)}\n"""
        return message
 
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return (calculate_average(self.grades) == 
                    calculate_average(other.grades))
        else:
            return 'Ошибка'
 
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return (calculate_average(self.grades) < 
                    calculate_average(other.grades))
        else:
            return 'Ошибка'
 
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return (calculate_average(self.grades) <= 
                    calculate_average(other.grades))
        else:
            return 'Ошибка'
 
class Reviewer(Mentor):
 
    def __init__(self, name, surname):
        super().__init__(name, surname)
 
    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Student) and
            course in self.courses_attached and
                course in lecturer.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        message = f"""\nИмя: {self.name}\nФамилия: {self.surname}\n"""
        return message
 
 
def calculate_average(grades: dict):
    all_grades = []
    for course_grades in grades.values():
        all_grades += course_grades
    if len(all_grades) > 0:
        average = sum(all_grades) / len(all_grades)
    else:
        average = 0
    return average
 
def course_average_lecturers(lecturers: list[Lecturer], course):
    all_grades = []
    for lecturer in lecturers:
        for course_key, grades in lecturer.grades.items():
            if course_key == course: all_grades += grades
    average = sum(all_grades) / len(all_grades)
    return average
 
def course_average_students(students: list[Student], course):
    all_grades = []
    for student in students:
        for course_key, grades in student.grades.items():
            if course_key == course: all_grades += grades
    average = sum(all_grades) / len(all_grades)
    return average
 
students = [Student('StName1', 'StSurname1', 'male'), 
                Student('StName2', 'StSurname2', 'female'), 
                Student('StName3', 'StSurname3', 'female')]
lecturers = [Lecturer('LeName1', 'LeSurname1'),
                Lecturer('LeName2', 'LeSurname2'),
                Lecturer('LeName3', 'LeSurname3')]
reviewers = [Reviewer('ReName1', 'ReSurname1'),
                Reviewer('ReName2', 'ReSurname2')]
 
students[0].courses_in_progress += ['C#', 'DHTML']
students[1].courses_in_progress += ['Python', 'Java']
students[2].courses_in_progress += ['Python', 'DHTML']
 
reviewers[0].courses_attached += ['Python', 'Java', 'C#', 'DHTML']
reviewers[1].courses_attached += ['Python', 'Java', 'C#', 'DHTML']
 
lecturers[0].courses_attached += ['Python', 'Java']
lecturers[1].courses_attached += ['C#', 'DHTML']
lecturers[2].courses_attached += ['DHTML', 'Python']
 
reviewers[0].rate_hw(students[0], 'C#', 10)
reviewers[1].rate_hw(students[0], 'C#', 4)
reviewers[0].rate_hw(students[0], 'DHTML', 10)
reviewers[1].rate_hw(students[0], 'DHTML', 6)
reviewers[0].rate_hw(students[1], 'Python', 10)
reviewers[1].rate_hw(students[1], 'Python', 8)
reviewers[0].rate_hw(students[1], 'Java', 10)
reviewers[1].rate_hw(students[1], 'Java', 10)
reviewers[0].rate_hw(students[2], 'Python', 10)
reviewers[1].rate_hw(students[2], 'Python', 2)
reviewers[0].rate_hw(students[2], 'DHTML', 4)
reviewers[1].rate_hw(students[2], 'DHTML', 4)
 
students[0].rate_lesson(lecturers[1], 'C#', 9)
students[0].rate_lesson(lecturers[1], 'C#', 10)
students[0].rate_lesson(lecturers[1], 'DHTML', 8)
students[0].rate_lesson(lecturers[1], 'DHTML', 9)
students[0].rate_lesson(lecturers[2], 'DHTML', 7)
students[0].rate_lesson(lecturers[2], 'DHTML', 7)
students[1].rate_lesson(lecturers[0], 'Python', 8)
students[1].rate_lesson(lecturers[0], 'Python', 9)
students[1].rate_lesson(lecturers[2], 'Python', 6)
students[1].rate_lesson(lecturers[2], 'Python', 7)
students[1].rate_lesson(lecturers[0], 'Java', 8)
students[1].rate_lesson(lecturers[0], 'Java', 10)
students[2].rate_lesson(lecturers[0], 'Python', 5)
students[2].rate_lesson(lecturers[0], 'Python', 5)
students[2].rate_lesson(lecturers[2], 'Python', 5)
students[2].rate_lesson(lecturers[2], 'Python', 5)
students[2].rate_lesson(lecturers[1], 'DHTML', 5)
students[2].rate_lesson(lecturers[1], 'DHTML', 5)
students[2].rate_lesson(lecturers[2], 'DHTML', 5)
students[2].rate_lesson(lecturers[2], 'DHTML', 5)

for student in students: print(student, 'Словарь: ', student.grades)
for lecturer in lecturers: print(lecturer, 'Словарь: ', lecturer.grades)
for reviewer in reviewers: print(reviewer)
print(students[0] == students[1])
print(students[2] > students[1])
print(students[0] >= students[2])
print(lecturers[0] == lecturers[1])
print(lecturers[1] > lecturers[2])
print(lecturers[2] >= lecturers[0])
print()
print(f'Среднее у лекторов по Java: ' + 
        f'{course_average_lecturers(lecturers, 'Java')}')
print(f'Среднее у лекторов по Python: ' + 
        f'{course_average_lecturers(lecturers, 'Python')}')
print(f'Среднее у студентов по DHTML: ' + 
        f'{course_average_students(students, 'DHTML')}')
print(f'Среднее у студентов по C#: ' + 
        f'{course_average_students(students, 'C#')}')