d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below
# if d1 in range(1, 7) and d2 in range(1, 7):
if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    if d1 + d2 in (7 ,11):
        print('Winner')
    elif d1 + d2 in (2, 3, 12):
        print('Loser')
    else:
        print(d1 + d2)
else:
    print("Invalid input")