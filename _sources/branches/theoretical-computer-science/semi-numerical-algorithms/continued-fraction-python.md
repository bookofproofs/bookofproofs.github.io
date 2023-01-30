layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$8247
orderid: 300
parentid: bookofproofs$444
title: Continued Fraction (Python)
description: CONTINUED FRACTION PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8186
keywords: continued,fraction,python,continued fraction python,python continued fraction,continued fractions python,python fraction,continued fraction algorithm python,continued fraction algorithm,fraction continue python,continued fraction,continued fractions algorithm
contributors: bookofproofs

---
The [continued fraction][bookofproofs$8188] of a [real number][bookofproofs$1105] `$x\in\mathbb R$` can be computed by the following algorithm.[^1]


[^1]: Because floating point arithmetic IEEE-754 “double precision”, python doubles contain 53 bits of precision. Therefore, the algorithm not always computes the write values of the continued fraction. The algorithm also limits the computation to 20 values of the continued fraction, since some continued fractions are not finite.

---

import math

def contFrac(x, k):
    cf = []
    q = math.floor(x)
    cf.append(q)
    x = x - q
    i = 0
    while x != 0 and i < k:
        q = math.floor(1 / x)
        cf.append(q)
        x = 1 / x - q
        i = i + 1
    return cf

# Usage
print(contFrac(math.sqrt(2)))

1. will output 
1. will output 
