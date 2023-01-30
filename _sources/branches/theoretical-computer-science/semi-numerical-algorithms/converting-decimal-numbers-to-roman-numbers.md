layout: algorithm
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$6208
orderid: 50
parentid: bookofproofs$242
title: Converting Decimal Numbers to Roman Numbers
description: CONVERTING DECIMAL NUMBERS TO ROMAN NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357
keywords: converting,decimal,numbers,roman
contributors: bookofproofs

---
An algorithm converting a [natural number][bookofproofs$718] in its decimal representation into a roman number is given in the following:

---

def getDigit(x, e, f, z):
    digit = ""
    if x == 9:
        digit += e + z
    elif x &gt; 4:
        digit += f
        for k in range(x, 5, -1):
            digit += e
    else:
        if x == 4:
            digit += e + f
        else:
            for k in range(x, 0, -1):
                digit += e
    return digit

def dec2roman(x):
    ''' convert decimal number into roman number '''
    r = ""
    while x &gt; 999:
        x -= 1000
        r += "M"
    r += getDigit(x // 100, 'C', 'D', 'M')
    r += getDigit(x // 10 - 10*(x // 100), 'X', 'L', 'C')
    r += getDigit(x % 10, "I", "V", "X")
    return r

# usage
x = 751
r = dec2roman(x)
print(str(x) + " = " + r)

1. will output
1. will output
