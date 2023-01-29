layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1492
orderid: 50
parentid: bookofproofs$1491
title: 
description:  Proof of DISTRIBUTIVITY LAW FOR RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: numbers,rational,rational numbers,rational number,definition of rational number,definition of rational numbers,is -1 a rational number,is zero a rational number,define rational number,rational numbers def,rational numbers definition,rational number definition,rational numbers meaning,proof,proof
contributors: bookofproofs

---


---

By the [definition of rational numbers][bookofproofs$1033], the rational numbers `\(x,y,z \in \mathbb Q\)` are identified by pairs `\(x:=\frac ab\)`, `\(y:=\frac cd\)` and `\(z:=\frac ef\)` of some integers  `\(a,b,c,d,e,f\in\mathbb Z\)` with `\(b\neq 0\)`, `\(d\neq 0\)`, and `\(f\neq 0\)`.  Because [multiplying rational numbers is commutative][bookofproofs$1478], it is sufficient to show the left-distributivity law
`\[x\cdot(y+z)=(x\cdot y)+(x\cdot z).\]`

The left-distributivity law can be proven using the following mathematical definitions and concepts:
* [definition of adding rational numbers][bookofproofs$1446],
* [definition of multiplying rational numbers][bookofproofs$1475],
* [distributivity law for integers][bookofproofs$1466],
* [associativity law for multiplying integers][bookofproofs$1450], and
*  [commutativity law for multiplying integers][bookofproofs$1448].
The proof follows:


`\[\begin{array}{ccll}
x\cdot(y+z)&=&\frac ab\cdot\left(\frac cd + \frac ef\right)&\text{by definition of rational numbers}\\
&=&\frac ab\cdot\frac{cf+ed}{df}&\text{by definition of adding rational numbers}\\
&=&\frac{a(cf+ed)}{b(df)}&\text{by definition of multiplying rational numbers}\\
&=&\frac{a(cf)+a(ed)}{b(df)}&\text{by distributivity law of integers}\\
&=&\frac{(ac)f+(ae)d}{bdf}&\text{by associativity law for multiplying integers}\\
&=&\frac{(ac)f}{(bd)f}+\frac{(ae)d}{bdf}&\text{by definition of adding rational numbers}\\
&=&\frac{(ac)f}{(bd)f}+\frac{(ae)d}{(bf)d}&\text{by commutativity law for multiplying integers}\\
&=&\frac{ac}{bd}+\frac{ae}{bf}&\text{by  definition of rational numbers}\\
&=&(x\cdot y)+(x\cdot z)&\text{by definition of rational numbers}
\end{array}
\]`
