num1 = int(input("First number: "))  # Do not change this line
num2 = int(input("Second number: "))  # Do not change this line
num3 = int(input("Third number: "))  # Do not change this line

# Fill in the missing code below
maxn = num1
if num1 <= num2 >= num3:
    maxn = num2
elif num1 <= num3 >= num2:
    maxn = num3

print("The maximum is: ", maxn)  # Do not change this line