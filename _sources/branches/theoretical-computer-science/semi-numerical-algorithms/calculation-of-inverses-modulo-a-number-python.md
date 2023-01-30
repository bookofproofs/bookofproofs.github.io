layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$8224
orderid: 200
parentid: bookofproofs$444
title: Calculation of Inverses Modulo a Number (Python)
description: CALCULATION OF INVERSES MODULO A NUMBER PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: calculation,inverses,modulo,number,python,invmod python,python invmod,inverse modulo python
contributors: bookofproofs

---
Let `\(a,b\in\mathbb{Z}\)` be [positive integers][bookofproofs$1075] `$a,b\in\mathbb Z$` with `\(a\le b\)` which are [co-prime][bookofproofs$8093]. The algorithm `\(\operatorname{invmod}(a,b)\)` calculates correctly the [multiplicative inverse][bookofproofs$670] `$a^{-1}$` in the [ring of congruences][bookofproofs$8156] `$\mathbb Z_b,$` i.e. for which `$$a\cdot a^{-1}\equiv 1\mod b.$$` In particular, if `$b=p$` is a [prime number][bookofproofs$8156], this is the unique inverse of `$a$` modulo `$b$` in the [field of congruences][bookofproofs$8161] `$\mathbb Z_p.$`

The algorithm requires `\(\mathcal O(\log |b|)\)` (worst case and average case) division operations, which corresponds to `\(\mathcal O(\log^2 |b|)\)` bit operations.

---

def invmod(a, b):
    res = gcdext(a, b)
    if res[^0] != 1:
        raise NotCoPrimeException(a, b)
    else:
        if res[^1] < 0:
            res[^1] = res[^1] + (abs(res[^1]) // b + 1) * b
        return res[^1]


# Usage
print(invmod(16, 21))


1. will output
1. will output
