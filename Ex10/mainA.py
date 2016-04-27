#!/usr/bin/env python3
from random import randint
from fast import fast

def fermatTest(n, k):
    """
    Fermat primality test
    n: The number to test
    k: Number of times to repeat the test
    Returns: True if prime else False
    """
    for i in range(k):
        a = randint(2, n-2)
        if fast(a,n-1,n) != 1:
            return False

    return True

upperLimit = 0
lowerLimit = 2**1024
for i in range(1025):
    upperLimit += 2**i

found = False
f = open("prime.txt", "w")
while not found:
    a = randint(lowerLimit, upperLimit)
    if fermatTest(a, 10):
        f.write(str(a))
        found = True
