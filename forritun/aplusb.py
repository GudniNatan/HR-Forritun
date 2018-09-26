from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi or len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end


n = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0

for i in range(len(a)):
    ai = a[i]
    for j in range(i + 1, len(a)):
        aj = a[j]
        index = binary_search(a, ai + aj)
        if index not in [-1, i, j]:
            count += 2

print(count)

