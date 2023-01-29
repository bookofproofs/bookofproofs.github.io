layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1499
orderid: 50
parentid: bookofproofs$1498
title: 
description:  Proof of EXISTENCE OF RATIONAL CAUCHY SEQUENCE OF ZEROS NEUTRAL ELEMENT OF ADDITION OF RATIONAL CAUCHY SEQUENCES &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$696
keywords: addition,cauchy,element,existence,neutral,rational,sequence,sequences,zeros,proof
contributors: bookofproofs

---


---

Note that since the [rational zero `\(0\)` exists][bookofproofs$1473] , it is also true that the [rational sequence][bookofproofs$1484] `\((0)_{n\in\mathbb N}\)` exists. We have to show that  `\((0)_{n\in\mathbb N}\)` is a [rational Cauchy sequence][bookofproofs$1485]. But this is trivially the case, since for any rational `\(\epsilon > 0\)` we have

`\[|0_i-0_j|=0 < \epsilon\quad\quad\text{ for all }i,j\ge 1.\]`

It remains to be shown that the rational Cauchy sequence `\((0)_{n\in\mathbb N}\)` is neutral with respect to the [addition of rational Cauchy sequences][bookofproofs$1486]. Let `\((x_n)_{n\in\mathbb N}\)` be a rational Cauchy sequence. Because [`\(0\)` is neutral with respect to the addition of rational numbers][bookofproofs$1473], it follows that

`\[\begin{array}{ccll}
(x_n)_{n\in\mathbb N}+(0)_{n\in\mathbb N}&=&(x_n+0)_{n\in\mathbb N}&\text{by definition of adding rational Cauchy sequences}\\
&=&(x_n)_{n\in\mathbb N}&\text{because }0\text{ is neutral with respect to the addition of rational numbers}\\
\end{array}\]`

It remains to be shown that also the equation `\((0)_{n\in\mathbb N}+(x_n)_{n\in\mathbb N}=(x_n)_{n\in\mathbb N}\)` holds for all rational Cauchy sequences `\((x_n)_{n\in\mathbb N}\)`. It follows immediately from the [commutativity of adding rational Cauchy sequenses][bookofproofs$1496].