layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1468
orderid: 50
parentid: bookofproofs$1447
title: 
description:  Proof of ADDITION OF RATIONAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,associative,numbers,rational,proof
contributors: bookofproofs

---


---

Let `\(x,y,z\in\mathbb Q\)` be rational numbers, which [by definition][bookofproofs$1033] means that each rational number is an equivalence class of ordered pairs of integers represented by some integers `\(a,b,c,d,e,f\in\mathbb Z\)`, with `\(b\neq 0,d\neq 0,f\neq 0\)`[^1]:

`\[\begin{array}{ccc}x:=\frac ab,&y:=\frac cd,&z:=\frac ef.\end{array}\]`

In order to show the law 
`\[(x+y)+z=x+(y+z)\]`
we replace the symbols `\(x,y,z\)` by their representatives `\(\frac ab,\frac cd,\frac ef\)`, and use the following mathematical definitions and concepts:
* [definition of adding rational numbers][bookofproofs$1446],
* [distributivity law for integers][bookofproofs$1466],
* [associativity law for multiplying integers][bookofproofs$1450], and
* [commutativity law for multiplying integers][bookofproofs$1448].
`\[\begin{array}{rcll}
(x+y)+z&=&\left(\frac ab+\frac cd\right)+\frac ef&\text{by definition of rational numbers}\\
&=&\frac {ad + cb}{bd}+\frac ef& \text{by definition of adding rational numbers}\\
&=&\frac{(ad + cb)f + e(bd)}{(bd)f}&\text{by definition of adding rational numbers}\\
&=&\frac{adf + cbf + e(bd)}{(bd)f}&\text{by distributivity law for integers}\\
&=&\frac{adf + cbf + ebd}{bdf}&\text{by associativity of multiplying integers}\\
&=&\frac{adf + cfb + edb}{bdf}&\text{by commutativity of multiplying integers}\\
&=&\frac{adf + (cf + ed)b}{bdf}&\text{by distributivity law for integers}\\
&=&\frac{a(df) + (cf + ed)b}{b(df)}&\text{by  associativity of multiplying integers}\\
&=&\frac ab+\frac{cf + ed}{df}&\text{by definition of adding rational numbers}\\
&=&\frac ab+\left(\frac cd + \frac ef\right)&\text{by definition of adding rational numbers}\\
&=&x+(y+z)&\text{by definition of rational numbers}
\end{array}\]`

[^1]: Note that the symbol "`\(0\)`" denotes the zero defined for integers, and not the zero defined for rational numbers.
