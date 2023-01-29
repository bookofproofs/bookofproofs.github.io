layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$503
orderid: 50
parentid: bookofproofs$444
title: Greatest Common Divisor (Python)
description: GREATEST COMMON DIVISOR PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: common,divisor,greatest,python
contributors: bookofproofs

---
Let `\(a,b\in\mathbb{Z}\)` and `\(a\le b\)`. The algorithm `\(\gcd(a,b)\)` calculates correctly the [greatest common divisor][bookofproofs$1280] of `\(a\)` and `\(b\)` and requires `\(\mathcal O(\log |b|)\)` (worst case and average case) division operations, which corresponds to `\(\mathcal O(\log^2 |b|)\)` bit operations.

---

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    r = b
    while r > 0:
        r = a % b
        a = b
        b = r
    d=a
    return d


# Usage
print(gcd(5159, 4823))

1. will output
1. will output
