m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(max(n, m) // 2 + 1, 1, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        break
