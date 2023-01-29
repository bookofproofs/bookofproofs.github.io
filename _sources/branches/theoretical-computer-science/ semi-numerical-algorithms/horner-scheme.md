layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$1358
orderid: 800
parentid: bookofproofs$156
title: Horner Scheme
description: HORNER SCHEME &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1356,bookofproofs$1357
keywords: horner,scheme,x^2 + 3,horner scheme
contributors: bookofproofs

---
Let `\(F\)` be the [field][bookofproofs$557]. We consider a [polynomial over the field][bookofproofs$487].
.
`\[p:=\cases{
F\to F\\
x\to p(x):=a_nx^n + \ldots + a_1x + a_0,\\
}\]`

where `\(a_0,a_1,\ldots,a_n\in F\)` and assume that `\(p\)` is a polynomial of degree `\(n\)`, i.e. `\(a_n\neq 0\)`. **Horner scheme** is an algorithm for calculating the value `\(p(x_0)\)` at a specific value `\(x\in F\)`.  The algorithm `\(\mathtt{horner}(n,x,a)\)` requires `\(\mathcal O(n)\)` (worst case and average case) multiplication and addition operations.

---

def horner(n,a,x):
    h = a[n]
    for i in range(n-1, -1, -1):
        h = h*x + a[i]

    return h

# Usage for x^3 + 2*x^2 + 3*x + 4, calculation of the polynom value for x=1:
a = [4, 3, 2, 1]
n = len(a)-1
x = 1
print(horner(n,a,x))

1. will output
1. will output
