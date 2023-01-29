layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1529
orderid: 50
parentid: bookofproofs$1475
title: 
description:  Proof of MULTIPLICATION OF RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: numbers,rational,rational numbers,rational number,definition of rational number,definition of rational numbers,is -1 a rational number,is zero a rational number,define rational number,rational numbers def,rational numbers definition,rational number definition,rational numbers meaning,proof,proof
contributors: bookofproofs

---


---

Note that since [the products of integers][bookofproofs$891] `\(ac\)` and `\(bd\)` are also integers, it follows from the [definition of rational numbers][bookofproofs$1033] that for the rational numbers `\(x,y \in \mathbb Q\)` with `\(x:=\frac ab\)`, `\(y:=\frac cd\)` for some integers `\(a,b,c,d\in\mathbb Z\)` with `\(b\neq 0\)` and `\(d\neq 0\)`, also the number `\[x\cdot y=\frac{ac}{bd} \]`
is a rational number. It remains to be shown that the definition of multiplication of rational numbers is well-defined, i.e. it does not depend on the specific representatives of `\(x\)` and `\(y\)`. Assume we have different representatives `\[x=\frac{a_1}{b_1}=\frac{a_2}{b_2},~y=\frac{c_1}{d_1}=\frac{c_2}{d_2}.\quad\quad( * )\]` 
It follows from the definition of rational numbers that `\(a_1=\frac{a_2b_1}{b_2}\)` and `\(c_1=\frac{c_2d_1}{d_2}.\)` Therefore, we have [by virtue of commutativity of multiplying integers ][bookofproofs$1448] and because [integer one is neutral with respect to the multiplication of integers][bookofproofs$1454] that 
`\[\begin{array}{rcll}
x\cdot y&=&\frac{a_1}{b_1}\cdot\frac{c_1}{d_1}&\text{by definition of rational numbers}\\
&=&\frac{\frac{a_2b_1}{b_2}}{b_1}\cdot\frac{\frac{c_2d_1}{d_2}}{d_1}&\text{according to }(*)\\
&=&\frac{\frac{a_2b_1}{b_2}}{1}\cdot \frac 1{b_1}\cdot\frac{\frac{c_2d_1}{d_2}}{1}\cdot \frac 1{d_2}&\text{by definition of multiplying rational numbers}\\
&=&\frac{a_2b_1\cdot 1}{1\cdot b_2\cdot b_1}\cdot\frac{c_2d_1\cdot 1}{1\cdot d_2\cdot d_1}&\text{by definition of multiplying rational numbers}\\
&=&\frac{a_2\cdot 1}{b_2}\cdot\frac{b_1}{b_1}\cdot\frac{c_2\cdot 1}{d_2}\cdot\frac{d_1}{d_1}&\text{by commutativity of multiplying integers}\\
&=&\frac{a_2}{b_2}\cdot\frac{b_1}{b_1}\cdot\frac{c_2}{d_2}\cdot\frac{d_1}{d_1}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&\frac{a_2\cdot 1}{b_2\cdot 1}\cdot\frac{c_2\cdot 1}{d_2\cdot 1}&\text{by definition of rational numbers}\\
&=&\frac{a_2}{b_2}\cdot\frac{c_2}{d_2}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
\end{array}\]`
