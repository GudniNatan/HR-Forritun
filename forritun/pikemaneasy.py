n, t = map(int, input().split())

problems = list()
a,b,c,t0 = map(int, input().split())

problems.append((t0,0))
pset = set()

times = 0
extra = 0

for i in range(1, n):
    last = problems[i-1]
    l = (a * last[0] + b) % c + 1
    if l in pset:
        times = n // i
        extra = n % i
        break
    problems.append((l, i))
    pset.add(l)

print(problems)
time = 0
penalty = 0
solved = 0
for p in sorted(problems):
    problem = p[0]
    index = p[1]

    thistimes = times
    if index <= extra:
        thistimes += 1

    time += problem * thistimes
    penalty += time * thistimes
    solved += thistimes
    if time > t:
        break

print(solved, penalty % 1000000007)