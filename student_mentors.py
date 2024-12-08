class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
 
class Mentor:
 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
 
 
class Lecturer(Mentor):
 
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
 
 
class Reviewer(Mentor):
 
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
 
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Student) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lesson(cool_lecturer, 'Python', 9)
best_student.rate_lesson(cool_lecturer, 'Python', 9)
best_student.rate_lesson(cool_lecturer, 'Python', 9)
 
print(best_student.grades)
print(cool_lecturer.grades)