layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$6635
orderid: 400
parentid: bookofproofs$1105
title: Division of Real Numbers
description: DIVISION OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: real number,real numbers,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers][bookofproofs$1105], which by definition means that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all [rational Cauchy sequences][bookofproofs$1485], which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`. In the following, let `$(y_n)_{n\in\mathbb N}$` be not a [zero sequence][bookofproofs$1524], i.e. `$(y_n)_{n\in\mathbb N}\not\in I.$`

The  **division of real numbers**, written `\(x\div y\)`, is defined as the [product][bookofproofs$1532] of the first real number `\(x\)` with the [inverse of the second real number with respect to multiplication][bookofproofs$42] `\((y^{-1})\)`, formally

`\[x\div y:=((x_n)_{n\in\mathbb N} + I)\cdot ((y_n^{-1})_{n\in\mathbb N} + I):=(x_n\cdot y_n^{-1})_{n\in\mathbb N} + I=x+(y^{-1}),\]`

where `$(y_n^{-1})_{n\in\mathbb N}$` denotes a [rational Cauchy sequence][bookofproofs$1485] such that `$|y_n|\neq 0$` for sufficiently large indices `$n$`, which is ensured by the assumptions that `$(y_n)_{n\in\mathbb N}$` be not a [zero sequence][bookofproofs$1524].


The result of the division is called **quotient** or **ratio**. The number `$x$` is called the **dividend** (or the **numerator**) and the number `$y$` is called the **divisor** (or the **denominator**).
