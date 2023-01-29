layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1292
orderid: 50
parentid: bookofproofs$1291
title: 
description:  Proof of GENERATING THE GREATEST COMMON DIVISOR KNOWING CO-PRIME NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: common,divisor,generating,greatest,knowing,numbers,prime,proof
contributors: bookofproofs

---


---

* By hypothesis, `\(c > 0\)` is a [common divisor][bookofproofs$1280] of two [integers][bookofproofs$844] `\(a\)` and `\(b\)` and the integers `\(\frac ac\)` and `\(\frac bc\)` are [co-prime][bookofproofs$8093].
* This means that `\(\gcd\left(\frac ac,\frac bc\right)=1\)`. 
* Therefore, at least one of the integers `\(\frac ac\)` and `\(\frac bc\)`, and so at least one of the integers `\(a\)` and `\(b\)` must be different from zero. 
* Set `\(d:=\gcd(a,b)\)`, and we have `$d\neq 0.$`
* From the [definition of the greatest common divisor][bookofproofs$1280] we have that `\(c\mid d\)`. Thus, `\(\frac dc\)` is an integer. 
* Now, from the [multiplication of rational numbers][bookofproofs$1033] it follows that
`\[\frac dc \frac ad=\frac ac,\quad\frac dc \frac bd=\frac bc,\]`
which means that
`\[\frac dc\mid \frac ac,\quad  \frac dc\mid \frac bc.\]`
* Because `\(\gcd\left(\frac ac,\frac bc\right)=1\)`, `\(d > 0\)`, `\(c > 0\)`, any divisor of `\(\gcd\left(\frac ac,\frac bc\right)\)` must divide `\(1\)`. 
* This is only true for `$\frac dc=1,$` which means that `\(c=d=\gcd(a,b)\)`.
