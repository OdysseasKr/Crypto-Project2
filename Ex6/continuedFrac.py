#!/usr/bin/env python3
import math
import cmath
import fast
import decimal

def contFraction(x):
    """
    Computes a0,a1,a2.... using continued fractions
    """
    decimal.getcontext().prec = 100
    x = decimal.Decimal(x)
    a = []
    a += [math.floor(x)]
    x = x - a[0]
    while x>10**(-6):
        frac = decimal.Decimal(1)/decimal.Decimal(x)
        tmp = decimal.Decimal(math.floor(frac))
        a += [int(tmp)]
        x = frac - tmp
    return a

def revContFraction(a):
    """
    Computes convergent fractions
    """
    k = len(a) - 1
    Ns = [1]
    Ds = [a[k]]
    i = 0
    k -= 1
    while k >= 0:
        N = Ds[0]
        D = Ns[0]
        N += a[k] * D
        Ns = [N] + Ns
        Ds = [D] + Ds
        k -= 1
    return (Ns, Ds)

#a = contFraction(123454/546542)
#print(revContFraction(a))
