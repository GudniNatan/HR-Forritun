import itertools

count = 0
for perm in itertools.permutations(range(26), 6):
    if 1 in perm and 2 in perm:
        count += 1
        last = None
        for item in perm:
            if item == 2 and last == 1:
                break
            last = item
        else:
            count -= 1


print(count)