#! /usr/bin/env python

"""Crack the textbook RSA with CRT. Same exponent problem."""

import CRT

N = [391, 55, 87]
e = [3, 3, 3]
c = [208, 38, 32]

msg = CRT.calculate(N[0], N[1], N[2], c[0], c[1], c[2])
print msg ** (1./3.)
