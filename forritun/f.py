class Pet(object):

   def __init__(self, name):

       self.__name = name

 

   def get_name(self):

       return self.__name

 

   def __str__(self):

       return "My pet {}".format(self.get_name())

 

class Dog(Pet):

   def __str__(self):

       return "My dog {}.".format(self.get_name())

 

d = Dog("Fido")

print(d)