n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
prime = True
test = 2
while test < n:
    if n % test == 0:
        prime = False
        break
    test += 1 

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")