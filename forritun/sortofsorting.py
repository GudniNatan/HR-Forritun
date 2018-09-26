from sys import stdin, stdout

n = int(stdin.readline())
while n != 0:
    l = list()
    for i in range(n):
        l.append(stdin.readline())

    l.sort(key=lambda s: s[:2])
    stdout.write("".join(l))
    n = int(stdin.readline())
    if n != 0:
        stdout.write("\n")
