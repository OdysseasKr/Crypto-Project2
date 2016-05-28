#! /usr/bin/env python

"""Cracking the Rabin TDF."""

import CRT as f

p = 5
q = 11
c = 14  # c = y

# solve x^2 = 14 mod 5
for i in range(c):
    if ((i ** 2) % p == c % p):
        x1 = i
        break
# solve x^2 = 14 mod 11
for i in range(c):
    if ((i ** 2) % q == c % q):
        x2 = i
        break

m1 = p
m2 = q
n1 = x1
n2 = x2
n3 = -x1
n4 = -x2

x = []
x.append(f.calculate(m1, m2, n1, n2))
x.append(f.calculate(m1, m2, n3, n2))
x.append(f.calculate(m1, m2, n1, n4))
x.append(f.calculate(m1, m2, n3, n4))

print "Answers:", x

# the exercise declares that m < 20
for i in x:
    if (i < 20):
        print i, "is the correct answer"
