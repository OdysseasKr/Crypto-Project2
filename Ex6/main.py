#!/usr/bin/env python3
import math
import cmath
import fast
from continuedFrac import *

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
    """
    Checks if a is an integer
    """
    a = complex(a)
    tmp = False
    if (a.imag != 0):
        return False

    if (a.real == int(a.real)):
        return True

    return False

def wiener(N, e):
    """
    Wiener attack on RSA. Returns d
    """
    a = contFraction(e,N)
    fi = [0]
    n = len(a)
    Ns = [0]
    Ds = [0]
    for i in range(1,n):
        (Ni,Di) = revContFraction(a[1:i+1])
        Ns = Ns + [Ni]
        Ds = Ds + [Di]
        tmp = (e*Ds[i] - 1)/Ns[i]
        fi += [tmp]

    for i in range(1,n):
        if isInt(fi[i]):
            (x1, x2) = quadratic(1, -N+fi[i]-1, N)
            if isInt(x1) and isInt(x2):
                return Ds[i]

def decrypt(C, d, N):
    """
    Decrypts array of integers C, using d and N of RSA
    """
    f = open("message.txt","w")
    M = []
    for c in C:
        m = fast.fast(c,d,N)
        f.write(str(chr(m)))


C=[47406263192693509,51065178201172223,30260565235128704,82385963334404268,
8169156663927929,47406263192693509,178275977336696442,134434295894803806,
112111571835512307,119391151761050882,30260565235128704,82385963334404268,
134434295894803806,47406263192693509,45815320972560202,174632229312041248,
30260565235128704,47406263192693509,119391151761050882,57208077766585306,
134434295894803806,47406263192693509,119391151761050882,47406263192693509,
112111571835512307,52882851026072507,119391151761050882,57208077766585306,
119391151761050882,112111571835512307,8169156663927929,134434295894803806,
57208077766585306,47406263192693509,185582105275050932,174632229312041248,
134434295894803806,82385963334404268,172565386393443624,106356501893546401,
8169156663927929,47406263192693509,10361059720610816,134434295894803806,
119391151761050882,172565386393443624,47406263192693509,8169156663927929,
52882851026072507,119391151761050882,8169156663927929,47406263192693509,
45815320972560202,174632229312041248,30260565235128704,47406263192693509,
52882851026072507,119391151761050882,111523408212481879,134434295894803806,
47406263192693509,112111571835512307,52882851026072507,119391151761050882,
57208077766585306,119391151761050882,112111571835512307,8169156663927929,
134434295894803806,57208077766585306]

(N,e)=(194749497518847283, 50736902528669041)


d = wiener(N,e)
print(d)
decrypt(C, d, N)
