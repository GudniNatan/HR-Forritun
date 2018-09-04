age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
price = 30.0

if age >= 65:
    price /= 2
elif age <= 5:
    price = 0.0

print(price)