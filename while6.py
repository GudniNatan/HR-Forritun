num = 10
while num < 100:
    cab = num * num
    if cab % 100 == num and cab < 1000:
        print(num)
    num += 1
