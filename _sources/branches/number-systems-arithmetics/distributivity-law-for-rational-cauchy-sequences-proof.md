layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1507
orderid: 50
parentid: bookofproofs$1506
title: 
description:  Proof of DISTRIBUTIVITY LAW FOR RATIONAL CAUCHY SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: cauchy,distributivity,law,rational,sequences,distributive,sequence,property,proof
contributors: bookofproofs

---


---

Let `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` be [rational Cauchy sequences][bookofproofs$1485]. Because [multiplying rational Cauchy sequences is commutative][bookofproofs$1502], it is sufficient to show the [left-distributivity law][bookofproofs$682].
`\[(x_n)_{n\in\mathbb N}\cdot[(y_n)_{n\in\mathbb N}+(z_n)_{n\in\mathbb N}]=[(x_n)_{n\in\mathbb N}\cdot (y_n)_{n\in\mathbb N}]+[(x_n)_{n\in\mathbb N}\cdot (z_n)_{n\in\mathbb N}].\]`

The left-distributivity law can be proven using the following mathematical definitions and concepts:
* [definition of adding rational Cauchy sequences][bookofproofs$1486],
* [definition of multiplying rational Cauchy sequences][bookofproofs$1488], and
* [distributivity law for rational numbers][bookofproofs$1491].
The proof follows:


`\[\begin{array}{ccll}
(x_n)_{n\in\mathbb N}\cdot[(y_n)_{n\in\mathbb N}+(z_n)_{n\in\mathbb N}]&=&(x_n)_{n\in\mathbb N}\cdot(y_n+z_n)_{n\in\mathbb N}&\text{by definition of adding rational Cauchy sequences}\\
&=&(x_n\cdot [y_n+z_n])_{n\in\mathbb N}&\text{by definition of multiplying rational Cauchy sequences}\\
&=&([x_n\cdot y_n]+[x_n\cdot z_n])_{n\in\mathbb N}&\text{by distributivity law of rational numbers}\\
&=&(x_n\cdot y_n)_{n\in\mathbb N}+(x_n\cdot z_n)_{n\in\mathbb N}&\text{by definition of adding rational Cauchy sequences}\\
&=&[(x_n)_{n\in\mathbb N}\cdot (y_n)_{n\in\mathbb N}]+[(x_n)_{n\in\mathbb N}\cdot (z_n)_{n\in\mathbb N}]&\text{by definition of multiplying rational Cauchy sequences}
\end{array}
\]`
