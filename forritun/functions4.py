# is_prime function definition goes here
def is_prime(num):
    if num == 2 or num == 3:
        return True
    top = round(num ** 0.5) + 2
    for i in range(2, top):
        if num % i == 0:
            return False
    return True
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
if is_prime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")