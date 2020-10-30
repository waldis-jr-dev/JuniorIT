import random
import string


class Human:
    def __init__(self, height: [float, int], weight: [float, int], date_of_birth: str, eyes_color: str):
        self.height = height
        self.weight = weight
        self.date_of_birth = date_of_birth
        self.eyes_color = eyes_color

    def change_height(self, new_height):
        self.height = new_height

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_birthday_date(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def change_eyes_color(self, new_eyes_color):
        self.eyes_color = new_eyes_color

    def __lt__(self, other):
        return self.height + self.weight < other.height + other.weight

    def __gt__(self, other):
        return self.height + self.weight > other.height + other.weight

    def __eq__(self, other):
        return self.height + self.weight == other.height + other.weight


class Student(Human):
    def __init__(self, height: [float, int], weight: [float, int], date_of_birth: str, eyes_color: str, course: int,
                 specialization: str):
        super().__init__(height, weight, date_of_birth, eyes_color)
        self.course = course
        self.specialization = specialization

    def write_term_paper(self, lines: int, characters: int):
        with open('term_paper.txt', 'w') as file:
            for _ in range(lines):
                for _ in range(characters):
                    line = ''.join([random.choice(string.digits + string.ascii_letters + string.punctuation)])
                file.write(line + '\n')
            file.write(f'\nDate of birth: {self.date_of_birth}\n'
                       f'Course: {self.course}\n'
                       f'Specialization: {self.specialization}')

    def change_study_date(self, new_course):
        self.course = new_course

    def change_specialization(self, new_specialization):
        self.specialization = new_specialization


jon = Human(170, 60, '10.10.2000', 'green')
mike = Human(155.5, 49.9, '12.08.2010', 'yellow')
mia = Human(165, 65, '01.05.2004', 'black')

print(jon < mike)

student_jon = Student(170, 60, '10.10.2000', 'green', 4, 'Software')
student_mike = Student(155.5, 49.9, '12.08.2010', 'yellow', 2, 'Engineer')
student_mia = Student(165, 65, '01.05.2004', 'black', 5, 'IT')

student_jon.write_term_paper(5, 16)
print(student_jon == student_mia)
