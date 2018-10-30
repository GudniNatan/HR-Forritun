import itertools

"""import itertools

count = 0
n = 5
for i in itertools.product(range(40), repeat=n):
    last1 = 30
    last2 = 30
    for number in i:
        if number < 30:
            if last1 < 30:
                if last2 < 30:
                    break
        last2 = last1
        last1 = number
    else:
        count += 1
print(count)

"""
"""
import itertools

n = 3
count = 0
for i in itertools.product("01", repeat=n):
    if "010" not in "".join(i):
        count += 1
print(count)
"""
"""
last = "0"
count = 0
n = 10
for i in itertools.product("01", repeat=n):
    if i[1] != last:
        print()
        last = i[1]
    if "010" in "".join(i):
        count += 1
        continue
    if i[-1] == "1":
        continue
    if i[-2] == "1" and i[-3] == "1":
        continue
    print("".join(i), end=" ")
print(2 ** n - count)
"""

tvf = [1] * 25
vf = [2] * 20
tf = [3] * 10

staff = tvf + vf + tf
count = 0
print(staff)
count = 0
total = 0
for i in itertools.combinations(staff, 4):
    total += 1
    if 1 in i:
        if 2 in i:
            if 3 not in i:
                count += 1
        elif 3 in i:
            count += 1
    elif 2 in i:
        if 3 in i:
            count += 1

print(total)
print(count)
print(count / total)