
base = 30
s = [0, 0, 0, 0, 0, 0]
count = 0
for i in range(base ** len(s)):
    s[-1] += 1
    for j in range(1, len(s)):
        if s[-j] % base != s[-j]:
            s[-j] = s[-j] % base
            s[-j-1] += 1
        else:
            break
    if 5 in s and 6 in s:
        count += 1
    if i % base ** 4 == 0:
        print("{:.2f}% done".format((i / base ** len(s)) * 100))

print()
print(count)
