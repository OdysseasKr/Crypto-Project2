#! /usr/bin/env python

"""Chinese Remainder Theorem."""


def calculate(m1, m2, m3, n1, n2, n3):
    """Calculate CRT."""
    M = m1 * m2 * m3  #

    M1 = M / m1  #

    M2 = M / m2  #

    M3 = M / m3  #

    # ui * Mi = 1 mod mi
    u1 = modinverse(M1, m1)  #

    u2 = modinverse(M2, m2)  #

    u3 = modinverse(M3, m3)  #

    x = (n1 * u1 * M1) + (n2 * u2 * M2) + (n3 * u3 * M3)  #

    # answer = x mod M
    answer = x % M  #

    return answer


def modinverse(a, m):
    """calculate."""
    x = 0
    y = 1
    u = 1
    v = 0
    e = m
    f = a
    while f > 1:
        q = int(e/f)
        r = e % f
        c = x - q*u
        d = y-q*v
        x = u
        y = v
        u = c
        v = d
        e = f
        f = r
    u = (u+m) % m
    return u
