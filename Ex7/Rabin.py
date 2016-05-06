#! /usr/bin/env python

"""Cracking the Rabin TDF."""

import CRT as f

p = 5
q = 11
c = 14  # c = y

x2a = c % p  # x^2 = 14 mod 5 = 4
x2b = c % q  # x^2 = 14 mod 11 = 3
x1 = x2a ** (0.5)  # +- 2
x2 = x2b ** (0.5)  # +- sqr(3)
x3 = -x1
x4 = -x2

m1 = p
m2 = q
n1 = x1
n2 = x2
n3 = x3
n4 = x4

x = []
x.append(f.calculate(m1, m2, n1, n2))
x.append(f.calculate(m1, m2, -n1, n2))
x.append(f.calculate(m1, m2, n1, -n2))
x.append(f.calculate(m1, m2, -n1, -n2))

print "Answers:", x

# the exercise declares that m < 20
for i in x:
    if (i < 20):
        print i, "is the answer"
