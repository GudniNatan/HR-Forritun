import math
bits = input().split()

s, exp, frac = [int(x, 2) for x in bits]

frac /= 2 ** len(bits[2])
bias = 2 ** (len(bits[1])- 1) - 1
V = 0
if "0" in bits[1]:
    if "1" in bits[1]:
        #normalized
        V = ((-1) ** s) * (1 + frac) * (2 ** (exp - bias))
    else:
        #denormalized
        V = ((-1) ** s) * (0 + frac) * (2 ** (1 - bias))
else:
    #special case
    if frac == 0:
        V = math.inf * ((-1) ** s)
    else:
        V = math.nan

print(V)