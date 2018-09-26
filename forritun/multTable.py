"""
MAX = 10
for i in range(1, MAX + 1):
    for j in range(1, MAX + 1):
        print("{:>5}".format(i * j), end="")
    print()
"""
MAX = 10
i = 1
j = 1
while j < MAX + 1:
    print("{:>5}".format(i * j), end="")
    i += 1
    if i > MAX:
        i = 1
        j += 1
        print()
