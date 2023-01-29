layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1537
orderid: 50
parentid: bookofproofs$40
title: 
description:  Proof of EXISTENCE OF REAL ONE NEUTRAL ELEMENT OF MULTIPLICATION OF REAL NUMBERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: element,existence,multiplication,neutral,numbers,one,real,proof
contributors: bookofproofs

---


---

Note that since the [rational Cauchy sequence of ones `\((1)_{n\in\mathbb N}\)` exists][bookofproofs$1504], it is also true that the [real number][bookofproofs$1105] `\(1:=(1)_{n\in\mathbb N} + I\)` exists.  It remains to be shown that the real number `\(1\)` is neutral with respect to the [multiplication of real numbers][bookofproofs$1532]. Let `\(x=(x_n)_{n\in\mathbb N}+I\)` be a real number. Because the rational Cauchy sequence `\((1)_{n\in\mathbb N}\)` [is neutral with respect to the addition of rational Cauchy sequences][bookofproofs$1504], it follows that

`\[\begin{array}{ccll}
x\cdot 1&=&((x_n)_{n\in\mathbb N}+I)\cdot ((1)_{n\in\mathbb N}+I)&\text{by definition of real numbers}\\
&=&((x_n)_{n\in\mathbb N}\cdot (1)_{n\in\mathbb N})+I&\text{by definition of multiplying real numbers}\\
&=&(x_n)_{n\in\mathbb N}+I&\text{because }(1)_{n\in\mathbb N}\text{ is neutral element of multiplication of rational Cauchy sequences}\\
&=&x&\text{by definition of real numbers}\\
\end{array}\]`

It remains to be shown that also the equation `\(1\cdot x=x\)` holds for all `\(x\in\mathbb R\)`. It follows immediately from the [commutativity of multiplying real numbers][bookofproofs$38].