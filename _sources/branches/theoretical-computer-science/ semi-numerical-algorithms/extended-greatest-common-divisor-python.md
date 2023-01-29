layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$8223
orderid: 100
parentid: bookofproofs$444
title: Extended Greatest Common Divisor (Python)
description: EXTENDED GREATEST COMMON DIVISOR PYTHON ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: 5159+261,common,divisor,extended,greatest,python,gcdext
contributors: bookofproofs

---
Let `\(a,b\in\mathbb{Z}\)` be [positive integers][bookofproofs$1075] `$a,b\in\mathbb Z$` with `\(a\le b\)`. The algorithm `\(\operatorname{gcdext}(a,b)\)` calculates correctly the [greatest common divisor][bookofproofs$1280] `$d$` of `\(a\)` and `\(b\)` and [integers][bookofproofs$844] `$x,y\in\mathbb Z$`  `$x,y\in\mathbb Z$` such that `$$d=ax+by.$$` It requires `\(\mathcal O(\log |b|)\)` (worst case and average case) division operations, which corresponds to `\(\mathcal O(\log^2 |b|)\)` bit operations.

---

def gcdext(a, b):
    if a <= 0:
        NotPositiveException(a)
    if b <= 0:
        NotPositiveException(b)
    x = 0
    y = 1
    u = 1
    v = 0
    q = a // b
    r = a % b
    while r != 0:
        a = b
        b = r
        t = u
        u = x
        x = t - q * x
        t = v
        v = y
        y = t - q * y
        if b != 0:
            q = a // b
            r = a % b
    d = b
    return [d, x, y]

# Usage
print(gcdext(5159, 4823))


1. will output
1. will output
