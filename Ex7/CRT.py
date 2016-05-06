#! /usr/bin/env python

"""Chinese Remainder Theorem."""


def calculate(m1, m2, n1, n2):
    """Calculate CRT."""
    M = m1 * m2  # 55

    M1 = M / m1  # 11

    M2 = M / m2  # 5

    # ui * Mi = 1 mod mi
    u1 = modinverse(M1, m1)  # 1

    u2 = modinverse(M2, m2)  # 9

    x = (n1 * u1 * M1) + (n2 * u2 * M2)

    #  x = res mod M
    result = modinverse(x, M)

    return result


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
