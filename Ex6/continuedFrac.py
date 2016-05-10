#!/usr/bin/env python3
import math
import cmath
import fast
import decimal

def contFraction(x,y):
    """
    Input: x / y
    Computes a0,a1,a2.... using continued fractions
    """
    i = 0
    a = [x//y]
    x = x - y * a[0]
    while x > 0:
        i += 1
        a = a + [y//x]
        tmp = x
        x = y
        y = tmp
        x = x - y * a[i]

    if (a[0] != 0):
        a = [0] + a
    return a


def revContFraction(a):
    """
    Computes one convergent fraction
    """
    N = 1
    D = a[len(a)-1]

    for i in range(len(a)-2, -1, -1):
        N += D * a[i]
        tmp = N
        N = D
        D = tmp
    return (N,D)
