#! /usr/bin/env python

"""Chinese Remainder Theorem."""

import math
import modinverse as f


def calculate(m1, m2, m3, n1, n2, n3):
    """Calculate CRT."""
    M = m1 * m2 * m3  # 3876

    M1 = M / m1  # 228

    M2 = M / m2  # 323

    M3 = M / m3  # 204

    # ui * Mi = 1 mod mi
    u1 = f.modinverse(M1, m1)  # 5

    u2 = f.modinverse(M2, m2)  # 11

    u3 = f.modinverse(M3, m3)  # 15

    x = (n1 * u1 * M1) + (n2 * u2 * M2) + (n3 * u3 * M3)  # 82017

    # answer = x mod M
    answer = x % M  # 621

    return answer


def checkCRT(m1, m2, m3):
    """Check if the numbers are primes one another."""
    if gcd(m1, m2)[0] == 1:
        if gcd(m1, m3)[0] == 1:
            if gcd(m2, m3)[0] == 1:
                return True
    return False


def gcd(x, y):
    """Compute the gcd of (x,y) using extended Euclidean algorithm."""
    (a, b, u, v, g, w) = (1, 0, 0, 1, x, y)
    while w > 0:
        q = math.floor(g/w)
        t = w
        w = g % t
        g = t
        if w == 0:
            break
        U = a - q*u
        V = b - q*v
        a = u
        b = v
        u = U
        v = V
    return (g, U, V)


m1 = 17
m2 = 12
m3 = 19
n1 = 9
n2 = 9
n3 = 13

if checkCRT(m1, m2, m3):
    answer = calculate(m1, m2, m3, n1, n2, n3)
    if (0 < answer < 1000):
        print answer, "is an acceptable answer (0 < x < 1000)"
    else:
        print answer, "is NOT acceptable because it is out of boundaries"
