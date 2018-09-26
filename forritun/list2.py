def to_list(string):
    delimeter = " "
    if string.count(delimeter) == 0:
        delimeter = ","
    return string.split(delimeter)
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)


