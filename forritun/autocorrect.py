n, m = list(map(int, input().split()))

aclist = list()
for i in range(n):
    aclist.append(input())

aclist.sort()
print(aclist)
acweight = list()
acweight.append([aclist[0], 2])
for i in range(1, len(aclist)):
    last = aclist[i-1]
    current = aclist[i]
    if len(last) < len(current):
        for c in range(len(last)):
            if last[c] != current[c]:
                acweight.append([current, 2 + c])
                break
        else:
            acweight.append([current, 2 + acweight[-1][1]])
    else:
        acweight.append([current, 2])

print(acweight)