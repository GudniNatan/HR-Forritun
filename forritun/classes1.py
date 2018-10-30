# class Student goes here
class Student():

    def __init__(self):
        self.__score = 10

    def add_score(self):
        self.__score += 10

    def decrease_score(self):
        self.__score -= 10

    def __str__(self):
        return str(self.__score)


a = Student()