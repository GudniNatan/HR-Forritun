from sys import stdin, stdout
cases = int(stdin.readline())
snowflakes = [False for i in range(500000)]
all = list()
for a in range(cases):
    for i in set(all):
        snowflakes[i] = False
    maxtotal = 0
    row = list()
    all = list()
    n = int(stdin.readline())
    for j in range(n):
        inp = int(stdin.readline())
        if snowflakes[inp] == False:
            snowflakes[inp] = True
            row.append(inp)
            all.append(inp)
        else:
            maxtotal = max(maxtotal, len(row))
            row.append(inp)
            for i in range(len(row)):
                if row[i] == inp:
                    row = row[i + 1:]
                    break
                snowflakes[row[i]] = False
print(max(maxtotal, len(row)))