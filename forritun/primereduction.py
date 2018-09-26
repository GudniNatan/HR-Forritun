from sys import stdin, stdout
import time
from random import randint
from math import sqrt

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def reduce_n(a, x):
    #factors = list()
    index = 0
    total = 0
    i = int(sqrt(x))
    try:
        while i >= a[index]:
            if x % a[index] == 0:
                x //= a[index]
                if x == 1:
                    return total
                total += a[index]
                i = int(sqrt(x)) 
            else:
                index += 1
    except:
        pass
    return total + x

max_n = 1000000000
nums = [4, 2001] + [randint(2, max_n) for i in range(20)]
start_time = time.time()

calculated = dict()

primes = primes2(int(max_n ** 0.5))
rl = stdin.readline
w = stdout.write
n = nums.pop()#int(rl())
start = n
out = list()
while n != 4:
    x = reduce_n(primes, n)
    c = 1
    while x != n:
        if x in calculated.keys():
            el = calculated[x]
            x = el[0]
            c += el[1]
            break
        n = x
        x = reduce_n(primes, n)
        c += 1
    else:
        calculated[reduce_n(primes, n)] = [x, c]
        print(calculated)
    out.append("%d %d\n" % (x, c))
    n = nums.pop()#int(rl())
    start = n

w("".join(out))
time = time.time() - start_time
print("--- %s seconds ---" % time)