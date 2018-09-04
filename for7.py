top_num = int(input("Input a number between 0 and 999: "))

for i in range(0, top_num):
    if i < 10:
        print(i)
    elif i < 100:
        a = i // 10
        b = i % 10
        if a ** 2 + b ** 2 == i:
            print(i)
    else:
        a = i // 100
        b = ( i % 100 ) // 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i)