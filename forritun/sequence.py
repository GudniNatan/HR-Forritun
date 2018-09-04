n = int(input("Enter the length of the sequence: ")) # Do not change this line

lasta = 1
lastb = 0
a = 1
b = 1
c = 0

for i in range(n):
    c = lastb
    lastb = b
    b = lasta
    lasta = a
    a += b + a
    print(a)
