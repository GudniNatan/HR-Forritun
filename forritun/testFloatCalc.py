from decodeFloat import decode
from encodeFloat import encode
from math import isnan

k = 10
x = 10

print(2 * (2 ** k) * (2 ** x), "iterations")
for s in range(2):
    for e in range(2 ** k):
        for f in range(2 ** x):
            formatString = "{} {} {}".format(
                "{}", "{:0" + str(k) + "b}", "{:0" + str(x) + "b}")
            bitstring = formatString.format(s, e, f)
            number = decode(bitstring)
            if not isnan(number):
                encoded = encode(number, k=k, x=x)
                assert encoded == bitstring
