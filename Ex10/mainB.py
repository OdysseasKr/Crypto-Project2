#!/usr/bin/env python3
import math
from fast import fast
from modinverse import modinverse

# =================================================================
def shanks(p, y, g):
    L1 = []
    L2 = []
    A = math.floor(math.sqrt(p))
    for i in range(0, A+1):
        L1 += [g**(A*i) % p]
        L2 += [y * (g**i) % p]
        if L1[i] == L2[i]:
            return i*(A-1)

        print(L1)
        print(L2)
        inters = list(set(L1).intersection(L2))
        print(inters)
        if len(inters) != 0:
            B = inters[0]
            quotient = L1.index(B)
            reminder = L2.index(B)
            return A*quotient - reminder

# ==================================================================
# DRAZIWTIS POLARD
def f(x,a,b,p,g,y):
    m = p - 1
    if 0 <= x and x < m/3:
        return ((g * x) % p, (a + 1)%m, b)
    if m/3 <= x and x < 2*m/3:
        return ((x * x) % p, (2*a) %m , (2*b)%m )

    return ((y * x) % p, a, (b+1) % m)

def polard(p, y, g):
    print("i\tx\ta\tb\tX\tA\tB")
    m = p -1
    a,b,x = 0,0,1
    X,A,B = x,a,b

    for i in range(p):
        (x,a,b) = f(x,a,b,p,g,y)
        (X,A,B) = f(X,A,B,p,g,y)
        (X,A,B) = f(X,A,B,p,g,y)

        print(str(i)+"\t"+str(x)+"\t"+str(a)+"\t"+str(b)+"\t"+str(X)+"\t"+str(A)+"\t"+str(B))
        if x == X and b!=B:
            #print((g**a) * (y ** b) % p)
            #print((g**A) * (y ** B) % p)

            #lalala = modinverse(abs(b-B),m)
            #tmp = ((A - a)/(b - B))# % p

            #tmp = abs(A-a) * lalala % m
            #print(tmp)
            #print(findDat(a - A, B - b, p))
            return x

def findDat(A, B, p):
    i = 1
    while True:
        if (i*B % p) == A:
            return i
        else:
            i += 1

# ==================================================================

# g^x = y (mod N)
g = 3
y = 4
N = 43

print(shanks(N, y, g))
print(polard(N, y, g))
"""
a,b,x = 0,0,1
m = 42
for i in range(50):
    (x,a,b) = f(x,a,b,43,3,5)
    print(str(i)+"\t"+str(x)+"\t"+str(a)+"\t"+str(b))
    if (x == 26):
        print((g**a) * (y**b) % m)
"""
