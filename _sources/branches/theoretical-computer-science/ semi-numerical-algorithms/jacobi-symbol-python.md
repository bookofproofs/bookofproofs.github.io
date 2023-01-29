layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$8217
orderid: 400
parentid: bookofproofs$444
title: Jacobi Symbol (Python)
description: JACOBI SYMBOL PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: jacobi,python,symbol,jacobi symbol python,jacobi symbol,jacobi python
contributors: bookofproofs

---
Let `$a\in\mathbb Z$` be an [integer][bookofproofs$844], `$b > 0$` be an [odd][bookofproofs$8130] and [positive integer][bookofproofs$1075]. If `$|a|\le b,$` the following algorithm calculates correctly the [Jacobi symbol][bookofproofs$8214] `$\left(\frac ab\right)$` in the time `$\mathcal O(\log^2(b)),$` which corresponds to `\(\mathcal O(\log^3 |b|)\)` bit operations.

---

class NotOddException(Exception):
    def __init__(self, x):
        print(str(x) + " is not odd")


class NotPositiveException(Exception):
    def __init__(self, x):
        print(str(x) + " is not > 0")



class JacobiSymbol:
    """Calculates the JacobiSymbol (a|b)

    Keyword arguments:
    a -- integer
    b -- positive odd integer
    """

    def __init__(self, a, b):
        if b < 0:
            raise NotPositiveException(b)
        self.a = a
        self.b = b
        if (b % 2) == 0:
            raise NotOddException(b)
        self.a = a
        self.b = b
        if gcd(self.a, self.b) != 1:
            self.notCoPrime = True
        else:
            self.notCoPrime = False

    @staticmethod
    def __supplementary2__(x):
        if x % 8 == 1 or x % 8 == 7:
            return 1
        else:
            return -1

    @staticmethod
    def __supplementary1__(x, y):
        if x % 4 == 1 or y % 4 == 1:
            return 1
        else:
            return -1

    def calculate(self):
        if self.notCoPrime:
            return 0
        elif self.a == 1:
            return 1
        elif self.a == 2:
            return self.__supplementary2__(self.b)
        elif self.a % 2 == 0:
            return JacobiSymbol(self.a // 2, self.b).calculate() * JacobiSymbol(2, self.b).calculate()
        else:
            return JacobiSymbol(self.b % self.a, self.a).calculate() * self.__supplementary1__(self.a, self.b)



# Usage
b=21
for i in range(0, b):
    print("(" + str(i), "|", str(b) + ")=" + str(JacobiSymbol(i, b).calculate()))

''' will output
(0 | 21)=0
(1 | 21)=1
(2 | 21)=-1
(3 | 21)=0
(4 | 21)=1
(5 | 21)=1
(6 | 21)=0
(7 | 21)=0
(8 | 21)=-1
(9 | 21)=0
(10 | 21)=-1
(11 | 21)=-1
(12 | 21)=0
(13 | 21)=-1
(14 | 21)=0
(15 | 21)=0
(16 | 21)=1
(17 | 21)=1
(18 | 21)=0
(19 | 21)=-1
(20 | 21)=1
'''
