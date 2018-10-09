from math import sqrt, floor
import itertools
from operator import mul
from functools import reduce

def primes2(n):
    ''' Input n>=6, Returns a list of primes, 2 <= p < n '''
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def reduce_n(a, x):
    factors = list()
    index = -1
    while len(a):
        if x % a[index] == 0:
            x //= a[index]
            factors.append(a[index])
            if x == 1:
                return factors
        else:
            index -= 1
            try:
                a[index]
            except:
                break
    return list(sorted(factors + [x]))

def divisors(n):
    divs = [0]
    if n%2 == 0:
        divs.extend([2-1,n//2-1])
    for i in range(3,int(sqrt(n))+1):
        if n%i == 0:
            divs.extend([i-1,n//i-1])
    divs.extend([n-1])
    return list(set(divs))

n = int(input())
div = sorted(divisors(n))
print(" ".join(map(str,div)))

