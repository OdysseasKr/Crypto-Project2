#!/usr/bin/env python3
import math
import cmath
import fast
from continuedFrac import contFraction
from continuedFrac import revContFraction

def quadratic(a,b,c):
    """
    Solves a quadratic equation
    """
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return (sol1, sol2)

def isInt(a):
    tmp = False
    try:
        tmp = (int(a) == a)
    except:
        pass
    return tmp

def wiener(N, e):
    a = contFraction(e/N)
    print("Finished")
    (Ns, Ds) = revContFraction(a)
    print("Finished2")
    fi = [0]
    n = len(a)
    print(n)
    for i in range(1,n):
        tmp = (e*Ds[i] - 1)/Ns[i]
        fi += [tmp]

    for i in range(1,n):
        if i%10 == 0:
            print(i)
        if isInt(fi[i]):
            (x1, x2) = quadratic(1, -N+fi[i]-1, N)
            if isInt(x1.real) and isInt(x2.real):
                return Ds[i]

def decrypt(C, d, N):
    f = open("message.txt","w")
    M = []
    for c in C:
        m = fast.fast(c,d,N)
        f.write(str(unichr(m)))

#a = [0, 4, 2, 2, 1, 13, 15, 1, 1, 1, 1, 3, 2]
#print(revContFraction(a))
#(N,e)=(194749497518847283, 50736902528669041)
#print(wiener(N, e))
