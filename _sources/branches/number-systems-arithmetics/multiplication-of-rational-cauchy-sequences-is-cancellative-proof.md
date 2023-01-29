layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1573
orderid: 50
parentid: bookofproofs$1571
title: 
description:  Proof of MULTIPLICATION OF RATIONAL CAUCHY SEQUENCES IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: multiplication,rational cauchy sequences,cauchy sequence,definition of cauchy sequence,define cauchy sequence,what is a cauchy sequence,what is cauchy sequence,proof,proof
contributors: bookofproofs

---


---

Because the [multiplication of rational Cauchy sequences is commutative][bookofproofs$1502], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[\exists N\in\mathbb N:~ (x_n)_{n > N} \cdot (z_n)_{n > N}=(y_n)_{n > N} \cdot (z_n)_{n > N}\Longleftrightarrow (x_n)_{n > N}=(y_n)_{n > N},\]`
for all [rational Cauchy sequences][bookofproofs$1485] `\((x_n)_{n\in\mathbb N}, (y_n)_{n\in\mathbb N}, (z_n)_{n\in\mathbb N}\)` such that `\((z_n)_{n\in\mathbb N}\)` is [not convergent][bookofproofs$1572] to `\(0\)`. 

Because by hypothesis `\((z_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence not convergent to `\(0\)`, there exist an index `\(N\in\mathbb N\)` such that `\(|z_n|>0\)` for all `\(n > N\)`. For all sequence members with indices `\(n > N\)`, it follows from the [cancellation property of multiplication of rational numbers][bookofproofs$1480] and from the [definition of multiplying rational Cauchy sequences][bookofproofs$1488] that

`\[\begin{array}{rcl}
(x_n)_{n > N} \cdot (z_n)_{n > N}=(y_n)_{n\in\mathbb N} \cdot (z_n)_{n > N}&\Longleftrightarrow&(x_n\cdot z_n)_{n > N}=(y_n\cdot z_n)_{n > N}\\
&\Longleftrightarrow&(x_n)_{n > N}=(y_n)_{n > N}.
\end{array}\]`
