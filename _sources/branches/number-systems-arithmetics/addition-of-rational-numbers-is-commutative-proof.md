layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1470
orderid: 50
parentid: bookofproofs$1469
title: 
description:  Proof of ADDITION OF RATIONAL NUMBERS IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,commutative,numbers,rational,proof
contributors: bookofproofs

---


---

Let `\(x,y\in\mathbb Q\)` be rational numbers, which [by definition][bookofproofs$1033] means that each rational number is an equivalence class of ordered pairs of integers represented by some integers `\(a,b,c,d\in\mathbb Z\)`, with `\(b\neq 0,d\neq 0\)`[^1]:

`\[\begin{array}{cc}x:=\frac ab,&y:=\frac cd.\end{array}\]`

In order to show the law 
`\[x+y=y+x\]`
we replace the symbols `\(x,y\)` by their representatives `\(\frac ab,\frac cd\)`, and use the following mathematical definitions and concepts:
* [definition of adding rational numbers][bookofproofs$1446],
* [commutativity law for multiplying integers][bookofproofs$1448], and
* [commutativity law for adding integers][bookofproofs$1460].
`\[\begin{array}{rcll}
x+y&=&\frac ab+\frac cd&\text{by definition of rational numbers}\\
&=&\frac {ad + cb}{bd}& \text{by definition of adding rational numbers}\\
&=&\frac {ad + cb}{db}& \text{by commutativity of multiplying integers}\\
&=&\frac {cb + ad}{db}& \text{by commutativity of adding integers}\\
&=&\frac cd+\frac ab&\text{by definition of adding rational numbers}\\
&=&y+x&\text{by definition of rational numbers}
\end{array}\]`

[^1]: Note that the symbol "`\(0\)`" denotes the zero defined for integers, and not the zero defined for rational numbers.
