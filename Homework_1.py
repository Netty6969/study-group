class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {avg_grade:.1f}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}"
    
    # Методы сравнения студентов
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def get_average_grade(self): # расчет средней оценки лектора
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {avg_grade:.1f}"
          
        # методы сравнения лекторов
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    # Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    def get_average_hw_grade(students, course):
        total_sum = 0
        count = 0
        for student in students:
            if course in student.grades:
                total_sum += sum(student.grades[course])
                count += len(student.grades[course])
        return total_sum / count if count > 0 else 0

    # Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    def get_average_lecture_grade(lecturers, course):
        total_sum = 0
        count = 0
        for lecturer in lecturers:
            if course in lecturer.grades:
                total_sum += sum(lecturer.grades[course])
                count += len(lecturer.grades[course])
        return total_sum / count if count > 0 else 0
