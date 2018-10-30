# class Pair goes here
class Pair:
    def __init__(self, value_1=0, value_2=0,):
        self.__value_1 = value_1
        self.__value_2 = value_2

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.__value_1, self.__value_2)

    def __add__(self, other):
        new_value_1 = self.__value_1 + other.__value_1
        new_value_2 = self.__value_2 + other.__value_2
        return Pair(new_value_1, new_value_2)