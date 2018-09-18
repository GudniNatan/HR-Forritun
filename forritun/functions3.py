# The function definition goes here
def in_range(num):
    return 1 < num < 555

num = int(input("Enter a number: "))

# You call the function here
if in_range(num):
    print(num, "is in range.")
else:
    print(num, "is outside the range!")