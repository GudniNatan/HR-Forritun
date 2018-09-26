from sys import stdin, stdout
rl = stdin.readline
for case in range(int(rl())):
    nums = [rl() for u in range(int(rl()))]
    ln = "--"
    for n in sorted(nums):
        if len(ln) < len(n) and ln[:-1] == n[:len(ln)-1]:
            stdout.write("NO\n")
            break
        ln = n
    else:
        stdout.write("YES\n")
