class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_cw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_list = []
        for i in self.grades.values():
            grades_list += i
        return f'Средняя оценка за домашние задания: {sum(grades_list) / len(grades_list)}'

    def __str__(self):
        name_p = f'Имя: {self.name}'
        surname_p = f'Фамилия: {self.surname}'
        courses_in_progress_p = ','.join(self.courses_in_progress)
        finished_courses_p = ','.join(self.finished_courses)
        return f' {name_p} \n {surname_p} \n {self.grades_average()} \n {f"Курсы в процессе изучения: {courses_in_progress_p}"} ' \
               f"\n Завершенные курсы: {finished_courses_p}"

    def __lt__(self, other):
        return self.grades_average() < other.grades_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def grades_average(self):
        grades_list = []
        for i in self.grades.values():
            grades_list += i
        return f'Средняя оценка за лекции {sum(grades_list) / len(grades_list)}'

    def __str__(self):
        name_p = f'Имя: {self.name}'
        surname_p = f'Фамилия: {self.surname}'
        return f' {name_p} \n {surname_p} \n {self.grades_average()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_p = f'Имя: {self.name}'
        surname_p = f'Фамилия: {self.surname}'
        return f' {name_p} \n {surname_p}'


def grade_average_hw_all_students(students_list, course):
    grades_list = []
    for student in students_list:
        if isinstance(student, Student):
            grades_list += student.grades[course]
    return f"Средняя оценка всех студентов по курсу {course} равна {sum(grades_list) / len(grades_list)} "


def grade_average_hw_all_lecturer(lecturers_list, course):
    grades_list = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            grades_list += lecturer.grades[course]
    return f"Средняя оценка всех лекторов читающих курс {course} равна {sum(grades_list) / len(grades_list)} "

one_lecturer = Lecturer('Ivan', 'Petrov')
one_lecturer.grades['Python'] = [10,10,10]
one_lecturer.grades['Git'] = [9, 9, 9]
print(one_lecturer)

one_student = Student('Alex', 'Ometov', 'male')
two_student = Student('Nastya', 'Ometova', 'female')
three_student = Student('Sergei', 'Ometov', 'male')

one_student.finished_courses = 'Git'
one_student.courses_in_progress = 'Python'
one_student.grades['Python'] = [10,10,10]
one_student.grades['Git'] = [9, 9, 9]

three_student.finished_courses = 'Git'
three_student.courses_in_progress = 'Python'
three_student.grades['Python'] = [10,10,10]
three_student.grades['Git'] = [9, 9, 9]

two_student.finished_courses = 'Git'
two_student.courses_in_progress = 'Python'
two_student.grades['Python'] = [10,10,10]
two_student.grades['Git'] = [9, 1, 9]

all_students = [one_student, two_student, three_student]

print(grade_average_hw_all_students(all_students, 'Git'))

one_lecturer = Lecturer('Alex', 'Ometov')
two_lecturer = Lecturer('Nastya', 'Ometova')
three_lecturer = Lecturer('Sergei', 'Ometov')

one_lecturer.grades['Python'] = [10,1,10]
one_lecturer.grades['Git'] = [9, 1, 9]
two_lecturer.grades['Python'] = [10,10,10]
two_lecturer.grades['Git'] = [9, 1, 9]
three_lecturer.grades['Python'] = [10,10,10]
three_lecturer.grades['Git'] = [9, 1, 9]

all_lecturer = [one_lecturer, two_lecturer, three_lecturer]
print(grade_average_hw_all_lecturer(all_lecturer, 'Python'))

best_reviewer = Reviewer('Alex', 'Ometov')
best_reviewer.courses_attached = 'Python'
print(best_reviewer)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
best_student.grades['Git'] = [10, 1, 10, 10]
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 6)
best_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

first_lecturer = Lecturer('Nastya', 'Ometova')
first_lecturer.courses_attached = 'Python'
best_student.rate_cw(first_lecturer, 'Python', 5)
best_student.rate_cw(first_lecturer, 'Python', 7)
best_student.rate_cw(first_lecturer, 'Git', 10)
print(first_lecturer)

print(one_student > two_student)

