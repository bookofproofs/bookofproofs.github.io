layout: part
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$125
orderid: 200
parentid: bookofproofs$195
title: Rational Numbers
description: RATIONAL NUMBERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: numbers,rational,rational numbers,rational number
contributors: bookofproofs


---


---

### A motivation for the set of rational numbers `\(\mathbb Q\)`

The set of [integers][bookofproofs$118] `\(\mathbb Z=\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}\)` can be extended to the set of all **rational numbers** by introducing the ratios `\[\mathbb Q=\left\{q:=\frac xy, x\in \mathbb Z, y\in \mathbb Z\setminus\{0\}\right\}.\]` The major motivation for this extension is the solvability of the equation
`\[ax=b,~~~~~~~(b\in \mathbb Z, a\in \mathbb Z\setminus\{0\})~~~~~~~~~~~~~~~~~~( * )\]`
which cannot be always solved by an integer for any two given initial integers `\(b\in \mathbb Z, a\in \mathbb Z\setminus\{0\}\)`. For instance, while `\(-3x=15\)` has the integer solution `\(-5\in\mathbb Z\)`, there is no integer solution of the equation `\(-2x=15\)`. The main reason for the (in general) missing solutions to the equation `\(( * )\)` is the algebraic structure of integers together with addition and multiplication `\((\mathbb Z,+,\cdot)\)`, which turns out to be a [ring][bookofproofs$683]. Since, in general, the elements of a every ring do not have a multiplicative inverse, the equation `\(( * )\)` cannot be solved by `\[ax=b\Longleftrightarrow a^{-1}ax=a^{-1}b\Longleftrightarrow x=a^{-1}b,\]` 
since the multiplicative inverse `\(a^{-1}\)` of `\(a\in\mathbb Z\)` simply does not exist in `\(\mathbb Z\)`.

However, `\((\mathbb Z, + ,\cdot)\)` is a special kind of a ring, called an [integral domain][bookofproofs$892]. Following the [construction of fields from integral domains][bookofproofs$888], the integral domain `\((\mathbb Z,+ ,\cdot)\)` is [extended to the field][bookofproofs$1033] `\((\mathbb Q, +, \cdot)\)`, 
which turns out to be the smallest "extended" algebraic structure, in which the equation `\(( * )\)` becomes solvable, regardless which initial integers `\(b\in \mathbb Z, a\in \mathbb Z\setminus\{0\}\)` we choose. The solvability of `\(( * )\)` is then ensured by the existence of uniquely defined multiplicative inverse elements `\[q^{-1}=a^{-1}b=\frac 1ab=\frac ba\in \mathbb Q.\]`
