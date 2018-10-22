n, t = map(int, input().split())

problems = list()
a, b, c, t0 = map(int, input().split())

problems.append(t0)
problem_set = set(problems)

for i in range(1, n):
    last = problems[i-1]
    l = (a * last + b) % c + 1
    if l in problems:
        s = problems[:n % i]
        problems *= n // i
        problems.extend(s)
        break
    problems.append(l)

time = 0
penalty = 0
solved = 0
for problem in sorted(problems):
    time += problem
    if time > t:
        break
    penalty += time
    solved += 1

print(solved, penalty % 1000000007)
