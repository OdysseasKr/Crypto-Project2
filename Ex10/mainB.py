#!/usr/bin/env python3
import math
from fast import fast

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

        inters = list(set(L1).intersection(L2))
        if len(inters) != 0:
            B = inters[0]
            quotient = L1.index(B)
            reminder = L2.index(B)
            return A*quotient - reminder

# ==================================================================
def f(x,a,b,p,g,y):
    m = p - 1
    if 0 <= x and x < m/3:
        return ((g * x) % p, (a + 1)%m, b)
    if m/3 <= x and x < 2*m/3:
        return ((x * x) % p, (2*a) %m , (2*b)%m )

    return ((y * x) % p, a, (b+1) % m)

def polard(p, y, g):
    print("i\tx\ta\tb\tX\tA\tB")
    m = p - 1
    a,b,x = 0,0,1
    X,A,B = x,a,b

    for i in range(p):
        (x,a,b) = f(x,a,b,p,g,y)
        (X,A,B) = f(X,A,B,p,g,y)
        (X,A,B) = f(X,A,B,p,g,y)

        print(str(i)+"\t"+str(x)+"\t"+str(a)+"\t"+str(b)+"\t"+str(X)+"\t"+str(A)+"\t"+str(B))
        if x == X and b!=B:
            tmp = (abs(A - a)/abs(b - B))# % p
            return tmp
# ==================================================================

print("3^x = 2 (mod 43)")
print(shanks(43, 2, 3))

print("3^x = 4 (mod 43)")
print(shanks(43, 4, 3))

print("3^x = 5 (mod 43)")
print(shanks(43, 5, 3))
