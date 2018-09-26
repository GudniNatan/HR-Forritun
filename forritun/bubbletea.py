n = int(input())
teas = [int(x) for x in input().split()]
m = int(input())
toppings = [int(x) for x in input().split()]
pairings = list()
lowestPrice = 1000000001
for i in range(n):
    pair = [int(x) - 1 for x in input().split()[1:]]
    for j in pair:
        lowestPrice = min(teas[i] + toppings[j], lowestPrice)
    pairings.append(pair)
x = int(input())
print(max(x // lowestPrice - 1, 0))