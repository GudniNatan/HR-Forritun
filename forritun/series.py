value = int(input("Initial value: "))
step = int(input("Step: "))
total = 0

while total < 100:
    print(value, end=' ')
    total += value
    value += step

print("\nSum of series:", total)
