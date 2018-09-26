from sys import stdin, stdout
cases = int(stdin.readline())
for i in range(cases):
    stdin.readline()
    n = int(stdin.readline())
    s = 0
    for j in range(n):
        s += int(stdin.readline())
    stdout.write("NO\n" if s % n else "YES\n")