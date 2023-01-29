layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1677
orderid: 50
parentid: bookofproofs$1649
title: 
description:  Proof of EXISTENCE OF INVERSE RATIONAL NUMBERS WITH RESPECT TO MULTIPLICATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: existence,inverse,multiplication,numbers,rational,respect,proof
contributors: bookofproofs

---


---

By the [definition of rational numbers][bookofproofs$1033], a rational number `\(x\in\mathbb Q\)` can be represented by a pair of integers `\(a,b\in\mathbb Z\)`:
`\[x:=\frac ab,\quad a,b\in\mathbb Z,~b\neq 0.\]`

Let `\(x\neq 0\)`, i.e. let `\(x\)` not be the [rational zero][bookofproofs$1473]. Therefore, the integer `\(a\)` does not equal the [integer number zero][bookofproofs$1452] `\(0_{\in\mathbb Z}\)`. It is now obvious that we can use the integers `\(a,b\)` to define a new rational number

`\[y:=\frac ba,\quad a,b\in\mathbb Z,~a\neq 0.\]`

We will show that `\(x^{-1}=y\)`, i.e. that `\(y\)` is an inverse with respect to the [multiplication of rational numbers][bookofproofs$1475] of the rational number `\(x\)`. We will do so applying the  [commutativity of multiplying real numbers][bookofproofs$1448], and the [existence of the rational number one][bookofproofs$1482]:

`\[\begin{array}{rcll}
x \cdot y&=&\frac ab\cdot\frac ba&\text{by definition of rational numbers}\\
&=&\frac {ab}{ba}&\text{by definition of multiplying rational numbers}\\
&=&\frac {ab}{ab}&\text{by commutativity of multiplying integers numbers}\\
&=&1&\text{by the definition of rational one and because from }(a\neq 0\text{ and }b\neq 0)\text{ it follows } ab\neq 0.
\end{array}
\]`

The last conclusion `\[\text{[From }(a\neq 0\text{ and }b\neq 0)\text{ it follows } ab\neq 0\text{"}\]` is a consequence of the fact that [integers form an integral domain][bookofproofs$892]. This completes the proof.
