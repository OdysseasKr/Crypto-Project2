#!/usr/bin/env python3
from random import randint
from fast import fast

def f(x):
    return x**2 - x - 1354363

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


prime = 0
composite = 0
fout = open("results.txt", "w")
for i in range(100):
    x = randint(1,10000)
    fout.write(str(x) + "\t\t")
    x = abs(f(x))
    fout.write(str(x) + "\t\t")
    res = fermatTest(x, 10)
    if (res):
        prime += 1
    else:
        composite += 1
    fout.write(str(res) + "\n")

print("Primes:\t" + str(prime))
print("Composites:\t" + str(composite))

b = ""
for i in range(0,1024):
