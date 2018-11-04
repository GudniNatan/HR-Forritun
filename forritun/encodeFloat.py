from math import log2, nan, inf, atan2, pi


def encode(number, k, x):
    bias = 2 ** (k-1) - 1

    s = 0 if abs(number) == number else 1
    s = 1 if atan2(number, number) == -pi else s  # Check if negative 0
    number = abs(number)

    if number == inf:
        return "{} {} {}".format(s, ("1" * k), ("0" * x))
    if (2 ** bias) * number < 2:
        # denormalized
        E = 1 - bias
        frac = (number * (2 ** (-E)))
        e = 0
    else:
        # normalized
        E = int(log2(number) // 1)
        frac = (number * (2 ** (-E))) - 1
        e = E + bias

    frac = int(frac * (2 ** x))
    formatString = "{} {} {}".format(
            "{}", "{:0" + str(k) + "b}", "{:0" + str(x) + "b}")
    return formatString.format(s, e, frac)


def main():
    the_input = input("Input float or integer ratio (a/b): ")
    try:
        number = float(the_input)
    except ValueError:
        a, b = the_input.split("/")
        number = int(a) / int(b)
    k = int(input("How many bits in exp: "))
    x = int(input("How many bits in frac: "))
    print(encode(number, k, x))


if __name__ == '__main__':
    main()
