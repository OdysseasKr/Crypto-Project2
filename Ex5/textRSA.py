#! /usr/bin/enfromv python

"""Cracking the textbook RSA."""

import fast as f
import modinverse as m
import math


def factorization(N):
    """Find the two primes of N."""
    p = math.floor(math.sqrt(N))  # p is the square root of N (as integer)

    if (p % 2 == 0):
        p = p - 1  # if p is even subtract one and make it odd

    # find the first odd number that perfectly divides N
    while(p > 0):
        if (N % p == 0):
            break
        else:
            p = p - 2

    # q will be the result of the division N/p
    q = N / p
    return p, q


def decrypt(C, d, N):
    """Decrypt cipher with d block by block and convert them to ASCII."""
    message = []
    for c in C:
        msg = f.fast(c, d, N)
        message.append(str(unichr(msg)))
    return message


N = 11413
e = 19
# the cipher
C = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278, 4674, 909, 9958, 792, 909, 4132, 3143, 9958, 3203, 5343, 792, 3143, 4443]

p, q = factorization(N)

# the factorization of N
fN = (p - 1) * (q - 1)

# solve e * d = 1 mod fN for d
d = int(m.modinverse(e, fN))

message = ''.join(decrypt(C, d, N))
print "The message is: ", message
