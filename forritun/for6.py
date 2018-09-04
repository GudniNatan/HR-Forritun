top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(2, top_num, 2):
    factorsum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            factorsum += j
    if factorsum == i:
        print(i)