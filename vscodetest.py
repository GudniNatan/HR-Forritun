#! "C:\\Users\\Guðni\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe"
number = int(input("Enter a positive integer: "))
count = 0

while number > 0:
    if number %2==0:
        number = number // 2
    elif number %3==0:
        number = number // 3
    else:
        number = number - 1
    count = count + 1

print(count)