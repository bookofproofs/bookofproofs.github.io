layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1477
orderid: 50
parentid: bookofproofs$1476
title: 
description:  Proof of MULTIPLICATION OF RATIONAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: associative,multiplication,numbers,rational,proof
contributors: bookofproofs

---


---

Let `\(x,y,z\in\mathbb Q\)` be rational numbers, which by definition means that each rational number is an equivalence class of ordered pairs of integers represented by some integers `\(a,b,c,d,e,f\in\mathbb Z\)`, with `\(b\neq 0,d\neq 0,f\neq 0\)`[^1]:

`\[\begin{array}{ccc}x:=\frac ab,&y:=\frac cd,&z:=\frac ef.\end{array}\]`

In order to show the law 
`\[(x\cdot y)\cdot z=x\cdot (y\cdot z)\]`
we use the following mathematical definitions and concepts:
* [definition of rational numbers][bookofproofs$1033].
* [definition of multiplying rational numbers][bookofproofs$1475], and
* [associativity law for multiplying integers][bookofproofs$1450].
`\[\begin{array}{rcll}
(x\cdot y)\cdot z&=&\left(\frac ab\cdot \frac cd\right)\cdot \frac ef&\text{by definition of rational numbers}\\
&=&\frac {ac}{bd}\cdot \frac ef& \text{by definition of multiplying rational numbers}\\
&=&\frac {(ac)e}{(bd)f}& \text{by definition of multiplying rational numbers}\\
&=&\frac {a(ce)}{b(df)}& \text{by associativity of multiplying integers}\\
&=&\frac ab\cdot \frac{ce}{df}& \text{by definition of multiplying rational numbers}\\
&=&\frac ab\cdot \left(\frac cd\cdot \frac ef\right)& \text{by definition of multiplying rational numbers}\\
&=&x\cdot(y\cdot z)&\text{by definition of rational numbers}
\end{array}\]`

[^1]: Note that the symbol "`\(0\)`" denotes the zero defined for integers, and not the zero defined for rational numbers.
