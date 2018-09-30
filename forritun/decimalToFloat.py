from math import log2

k, x = list(map(int, input("How many bits in [exp frac]").split()))
number = float(input("Input decimal float"))
bias = 2 ** (k-1) - 1

s = 0 if abs(number) == number else 1
number = abs(number)

a = number
E = 0
while a < 1:
    a *= 2
    E -= 1
if a == number:
    print("dont work right now")
frac = a - 1
while int(frac) != frac:
    frac *= 2
frac = bin(int(frac))[2:]
while len(frac) < x:
    frac += "0"

e = E + bias
print(e)
exp = bin(e)[2:]
while len(exp) < k:
    exp = "0" + exp
print(s, exp, frac)