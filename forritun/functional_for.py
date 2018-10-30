def function_for(function, iterable):
    for i in iterable:
        function(i)


def function_while(function):
    # function needs to return boolean false to quit
    while not function():
        pass

def cool():
    a = 0
    
    def main():

        def getValidInput():
            nonlocal a
            string = input("Enter number: ")
            try:
                a = int(string)
                return True
            except ValueError:
                return False

        function_while(getValidInput)
        print(a)

    main()
cool()
