layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1679
orderid: 50
parentid: bookofproofs$1678
title: 
description:  Proof of DISTRIBUTIVITY LAW FOR COMPLEX NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,distributivity,law,numbers,proof
contributors: bookofproofs

---


---

By the [definition of complex numbers][bookofproofs$216], the complex numbers `\(x,y,z \in \mathbb C\)` are represented by pairs `\(x:=(a,b)\)`, `\(y:=(c,d)\)` and `\(z:=(e,f)\)` of some real numbers `\(a,b,c,d,e,f\in\mathbb R\)`.  Because [multiplying complex numbers is commutative][bookofproofs$1671], it is sufficient to show the left-distributivity law
`\[x\cdot(y+z)=(x\cdot y)+(x\cdot z).\]`

The left-distributivity law can be proven using the following mathematical definitions and concepts:
* [definition of adding complex numbers][bookofproofs$1657],
* [definition of multiplying complex numbers][bookofproofs$1668],
* [distributivity law for real numbers][bookofproofs$520],
* [associativity law for adding real numbers][bookofproofs$31], and
* [commutativity law for adding real numbers][bookofproofs$33].
The proof follows:


`\[\begin{array}{ccll}
x\cdot(y+z)&=&(a,b)\cdot((c,d)+ (e,f))&\text{by definition of complex numbers}\\
&=&(a,b)\cdot(c+e,d+f)&\text{by definition of adding complex numbers}\\
&=&(a(c+e)-b(d+f),a(d+f)+b(c+e))&\text{by definition of multiplying complex numbers}\\
&=&(ac+ae-bd-bf,ad+af+bc+be)&\text{by distributivity law of real numbers}\\
&=&(ac-bd+ae-bf,ad+bc+af+be)&\text{by commutativity of adding (and subtracting) real numbers}\\
&=&((ac-bd)+(ae-bf),(ad+bc)+(af+be))&\text{by associativity of adding complex numbers}\\
&=&(ac-bd,ad+bc)+(ae-bf,af+be)&\text{by definition of adding complex numbers}\\
&=&((a,b)\cdot (c,d))+ ((a,b)\cdot(e,f))&\text{by definition of multiplying complex numbers}\\
&=&(x\cdot y)+ (x\cdot z)&\text{by definition of complex numbers}\\
\end{array}
\]`
