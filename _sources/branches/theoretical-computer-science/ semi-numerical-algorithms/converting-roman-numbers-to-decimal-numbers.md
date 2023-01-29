layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$6209
orderid: 100
parentid: bookofproofs$242
title: Converting Roman Numbers to Decimal Numbers
description: CONVERTING ROMAN NUMBERS TO DECIMAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357
keywords: converting,decimal,numbers,roman
contributors: bookofproofs

---
In order to convert a roman number into the decimal representation of a [natural number][bookofproofs$718] `\(x &gt; 0\)`, the following algorithm can be used:

---

def roman2dec(z):
    ''' convert roman number into decimal number '''
    lastD = 0
    value = 0
    for i in range (0, len(z)):
        digit = z[i].upper()
        if digit == 'M':
            nextD = 1000
        elif digit == "D":
            nextD = 500
        elif digit == "C":
            nextD = 100
        elif digit == "L":
            nextD = 50
        elif digit == "X":
            nextD = 10
        elif digit == "V":
            nextD = 5
        elif digit == "I":
            nextD = 1
        else:
           raise Exception("Wrong roman digit: "+digit)

        if lastD &lt; nextD:
            value -= lastD
        else:
            value += lastD

        lastD = nextD

    value += lastD
    return value


x = "DCCXLIX"
r = roman2dec(x)
print(x + " = " + str(r))

1. will output
1. will output
