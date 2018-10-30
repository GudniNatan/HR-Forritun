class Student(object):
    def __init__(self, student_id, grades):
        self.student_id = student_id
        float_grades = list()
        for grade in grades:
            try:
                float_grades.append(float(grade))
            except:
                pass
        self.grades = float_grades

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(
            self.student_id, self.grades)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")

main()
