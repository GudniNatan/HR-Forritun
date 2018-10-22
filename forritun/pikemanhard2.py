from queue import PriorityQueue

n, t = map(int, input().split())

problems = list()
a,b,c,t0 = map(int, input().split())

problems.append(t0)
problem_set = set(problems)

priorityQueue = PriorityQueue(n)
for i in range(1, n):
    last = problems[i-1]
    l = (a * last + b) % c + 1
    if l in problem_set:
        """index = problems.index(l)
        n2 = n-len(problems)
        bit = problems[index:]
        times = n2 // len(bit)
        leftover = n2 % len(bit)
        s = bit[:leftover]
        bit *= times"""

        index = problems.index(l)
        #front = problems[:index]
        #bit = problems[index:]
        repeat = len(problems) - index
        times = (n - index) // repeat
        leftover = (n - index) % repeat
        #back = problems[index:leftover]
        #bit *= times
        #problems = front + bit + back
        #problems.extend(bit)
        #problems.extend(s)
        for j, pro in enumerate(problems):
            if j < index:
                priorityQueue.put_nowait((pro, 1))
            elif j > leftover - index:
                priorityQueue.put_nowait((pro, times + 1))
            else:
                priorityQueue.put_nowait((pro, times))
        break
    problems.append(l)
    problem_set.add(l)
else:
    for pro in problems:
        priorityQueue.put_nowait((pro, 1))

print('wow')
time = 0
penalty = 0
solved = 0
"""
for problem in sorted(problems):
    time += problem
    if time > t:
        break
    penalty += time
    solved += 1
"""
timeLeft = t
while priorityQueue.qsize() > 0:
    element, times = priorityQueue.get_nowait()
    times = min(times, timeLeft // element)
    timeLeft -= element * times
    solved += 1
    penalty += (t - timeLeft)
    if timeLeft < element:
        break

print(solved, penalty % 1000000007)