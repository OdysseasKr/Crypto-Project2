#!/usr/bin/env python3

"""Modular inverse."""


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
