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
        message = f"""Имя: {self.name}\nФамилия: {self.surname}\n"""\
            f"""Средняя оценка за домашние задания: {calculate_average(self.grades)}\n"""\
            f"""Курсы в процессе изучения: {self.courses_in_progress}\n"""\
            f"""Завершенные курсы: {self.finished_courses}\n"""
        return message
 
    def __eq__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) == calculate_average(other.grades)
        else:
            return 'Ошибка'
 
    def __lt__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) < calculate_average(other.grades)
        else:
            return 'Ошибка'
 
    def __le__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) <= calculate_average(other.grades)
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
        message = f"""Имя: {self.name}\nФамилия: {self.surname}\n"""\
            f"""Средняя оценка за лекции: {calculate_average(self.grades)}\n"""
        return message
 
    def __eq__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) == calculate_average(other.grades)
        else:
            return 'Ошибка'
 
    def __lt__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) < calculate_average(other.grades)
        else:
            return 'Ошибка'
 
    def __le__(self, other):
        if isinstance(other, Student):
            return calculate_average(self.grades) <= calculate_average(other.grades)
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
        message = f"""Имя: {self.name}\nФамилия: {self.surname}\n"""
        return message
 
 
def calculate_average(grades: dict):
    all_grades = []
    for course_grades in grades.values():
        all_grades += course_grades
    if len(all_grades) > 0:
        average = sum(all_grades)/len(all_grades)
    else:
        average = 0
    return average
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['java']
 
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['java']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'java', 8)
cool_reviewer.rate_hw(best_student, 'java', 8)
cool_reviewer.rate_hw(best_student, 'java', 8)
 
best_student.rate_lesson(cool_lecturer, 'Python', 9)
best_student.rate_lesson(cool_lecturer, 'Python', 9)
best_student.rate_lesson(cool_lecturer, 'Python', 9)
 
print(best_student)
print(cool_lecturer)
print(cool_reviewer)