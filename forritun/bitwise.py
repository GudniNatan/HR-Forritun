def getByte(x, n):
    x = x >> (n << 3)
    print(n << 3)
    print(bin(x))
    return x & 0xFF


def sign(x):
    is_negative = x >> 31
    is_positive = int(not is_negative)
    shifted = is_positive << 1
    signNumber = shifted + ~0
    return signNumber & (~1 >> int(not not x))


def anyEvenBit(x):
    y = x << 1
    print(bin(y ^ x))
    return not (y ^ x)


def upperBits(n):
    """
    tmin = ~((1 << 31) - 1)
    n = n + ~(1 << int(not not n)) + 2
    print(n)
    print(int(not n))
    upper = (tmin >> n) << int(not n)"""
    allBits = ~0
    shift = 33 + ~n
    upper = allBits << shift
    return upper


def rempwr2(x, n):
    modulo = (1 << n) + ~0
    tmin = 1 << 31
    modulo = modulo | 


print(upperBits(20))
