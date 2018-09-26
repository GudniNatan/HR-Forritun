from sys import stdin, stdout

n = int(stdin.readline())
lastPrice = 501
money = 100
stocks = 0
prices = [int(input()) for x in range(n)]
for i in range(len(prices) - 2, 0, -1):
    if prices[i-1] >= prices[i] >= prices[i + 1] or prices[i-1] <= prices[i] <= prices[i+1]:
        prices.pop(i)
print(prices)
for i in range(len(prices)):
    price = prices[i]
    if price < lastPrice:
        if stocks:
            money += lastPrice * stocks
            stocks = 0
        stocks = money // price
        money = money % price
    elif price > lastPrice:
        if stocks == 0:
            stocks = money // lastPrice
            money = money % lastPrice
        money += price * stocks
        stocks = 0
    lastPrice = price
print(money)
