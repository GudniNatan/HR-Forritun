import itertools


for length in range(100):
    x = 0
    for i in range(2 ** length):
        bitstring = "{0:06b}".format(i)
        if "101" in bitstring:
            x += 1

    print(2 ** length - x)
    print(2 ** length - 2 ** (length ** 0.5))
    print()
        