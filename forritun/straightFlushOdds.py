from math import factorial
def C(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))


print(40 / C(52, 5))