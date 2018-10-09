def getPermutation(iterable, index):
    factoradic = list()
    pool = list(iterable)
    n = len(iterable)
    for i in range(1, n+1):
        factoradic.insert(0, index % i)
        index //= i
    return tuple(pool.pop(x) for x in factoradic)

while True:
    try:
        n, k = map(int, input().split())
        it = range(1, n+1)
        print(" ".join(map(str, getPermutation(it, k))))
    except EOFError:
        break