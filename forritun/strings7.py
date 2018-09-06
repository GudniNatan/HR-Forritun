my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
original_int = my_int
bstr = ""
while my_int > 0:
    bstr = str(my_int % 2) + bstr
    my_int //= 2
print("The binary of", original_int, "is", bstr or "0")