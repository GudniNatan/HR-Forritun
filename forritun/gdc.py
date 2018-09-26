def gcd(a, b):
    y = min(a, b)
    x = max(a, b)
    while y != 0:
        y, x = x % y, y
    return x
        
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(12, 18))
print(lcm(12, 18))