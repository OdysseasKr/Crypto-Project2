#!/usr/bin/env python3
import math
from fast import fast

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

print(shanks(43, 4, 3))
