def hexInt(string):
    try:
        return int(string.strip(), base=16)
    except ValueError:
        return 0

a,b,d,c = list(map(hexInt, input().split(",")))

print(hex(a+b+c*(d or 1)))