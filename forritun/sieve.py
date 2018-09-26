import time

from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi or len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

def sieve(n):
    not_prime = set()
    prime = set([2])
    for i in range(3, n+1, 2):
        if i not in not_prime:
            prime.add(i)
            if i * i < n + 1:
                a = set(range(i*i, n+1, i))
                not_prime = not_prime.union(a)
    return prime

def sieve2(n):
    A = [True for x in range(0, n + 1)]
    for i in range(2, int(n ** 0.5 + 1)):
        if A[i]:
            for j in range(i * i, n+1, i):
                A[j] = False
    prime = list([2])
    for b in range(3, n, 2):
        if A[b]:
            prime.append(b)
    return prime

def sieve3(n):
    A = [True for x in range(0, n // 2)]
    for i in range(1, int(n ** 0.5 // 2)):
        if A[i]:
            m = i + i + 1
            for j in range((m * m) >> 1, len(A), m):
                A[j] = False
    primes = list([2])
    for i in range(1, len(A)):
        if A[i]:
            primes.append(i + i + 1)
    return primes

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


#print(len(sieve(1000000)))

import itertools

start_time = time.time()

x = primes2(1000000)
time = time.time() - start_time
print("--- %s seconds ---" % time)
print(len(x))