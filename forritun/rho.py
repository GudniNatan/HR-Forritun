from random import randint
def gcd(a, b):
    y = min(a, b)
    x = max(a, b)
    while y != 0:
        y, x = x % y, y
    return x

def rho(N):
    a = 2
    b = 2
    f = lambda x: x*x + randint(1, x)
    while ( b != a ):
        #a runs once
        a = f(a)
        # b runs twice as fast.
        b = f(f(b))
        p = gcd( abs(b - a) , N)
        if ( p > 1):
            return "Found factor: p"

    return "Failed. :-("

while True:
    print(rho(8))