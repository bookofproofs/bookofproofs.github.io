layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$360
orderid: 200
parentid: bookofproofs$156
title: Complex Numbers
description: COMPLEX NUMBERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex numbers algorithm
contributors: bookofproofs

---
The programming language Python has a built-in type for [complex numbers][bookofproofs$1690]. A separate algorithm implementing all common arithmetical operations is not needed. In Python, the [imaginary unit][bookofproofs$1160] `\(i\)` is denoted with the letter `\(j\)`.

---

# usage

z1 = complex(3, 4)
z2 = complex(-2, 5)

print(z1)
print(z2)
print(z2.conjugate())
print(z2.real)
print(z2.imag)
print("-----------")

print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
print(z1 / z2)
print(abs(z2))

''' will output
(3+4j)
(-2+5j)
(-2-5j)
-2.0
5.0
-----------
(1+9j)
(5-1j)
(-26+7j)
(0.48275862068965514-0.793103448275862j)
5.385164807134504
'''
