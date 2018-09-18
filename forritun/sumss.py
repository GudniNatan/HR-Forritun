"""from math import floor
total = 0
for i in range(2, 3 + 1):
    for j in range(0, 2 + 1):
        total += floor((i + 3) / (3 * j - 2))
print(total)


from math import log2, ceil
total = 0
for i in range(0, 2 + 1):
    total += ceil(log2((i + 1) / 2))
print(total)

"""
"""
total = 0
for i in range(1, 100 + 1):
    a = set()
    for j in range(i + 1, i * 2):
        a.add(j)

    total += len(a)
print(total)
"""

print(len([x for x in range(16, 128)]))
print([x for x in range(16, 128)])