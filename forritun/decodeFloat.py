from math import nan, inf


def decode(bitstring):
    bits = bitstring.split()
    s, exp, frac = [int(x, 2) for x in bits]
    frac /= 2 ** len(bits[2])
    bias = 2 ** (len(bits[1]) - 1) - 1
    V = None
    if "0" in bits[1]:
        if "1" in bits[1]:
            # normalized
            V = ((-1) ** s) * (1 + frac) * (2 ** (exp - bias))
        else:
            # denormalized
            V = ((-1) ** s) * (0 + frac) * (2 ** (1 - bias))
    else:
        # special case
        if frac == 0:
            V = inf * ((-1) ** s)
        else:
            V = nan
    return V


def main():
    bitstring = input()
    V = decode(bitstring)
    print('Floating point:', V)
    try:
        print('Fraction:', "{}/{}".format(*V.as_integer_ratio()))
    except (ValueError, OverflowError):
        print('Special case: no fraction')

if __name__ == '__main__':
    main()
