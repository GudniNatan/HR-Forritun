year = int(input("Input a year: "))  # Do not change this line

# Fill in the missing code below
leapYear = False
if year % 400 == 0:
    leapYear = True
elif year % 4 == 0:
    leapYear = True
    if year % 100 == 0:
        leapYear = False
print(leapYear)