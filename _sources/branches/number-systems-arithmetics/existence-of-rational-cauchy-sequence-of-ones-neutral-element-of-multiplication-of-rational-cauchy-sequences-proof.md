layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1505
orderid: 50
parentid: bookofproofs$1504
title: 
description: Proof of EXISTENCE OF RATIONAL CAUCHY SEQUENCE OF ONES NEUTRAL ELEMENT OF MULTIPLICATION OF RATIONAL CAUCHY SEQUENCES ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$696
keywords: multiplication,rational cauchy sequences,cauchy sequence,definition of cauchy sequence,define cauchy sequence,what is a cauchy sequence,what is cauchy sequence,proof,proof
contributors: bookofproofs

---


---

* Note that since the [rational one `\(1\)` exists][bookofproofs$1482], it is also true that the [rational sequence][bookofproofs$1484] `\((1)_{n\in\mathbb N}\)` exists, i.e. a sequence whose members all equal the [rational one][bookofproofs$1482] `\(1\)`.
* For any rational `\(\epsilon > 0\)` we have `\[|1_i-1_j|=0 < \epsilon\quad\quad\text{ for all }i,j\ge 1.\]`
* Therefore, the sequence `\((1)_{n\in\mathbb N}\)` is, trivially, a [rational Cauchy sequence][bookofproofs$1485].
* Let `\((x_n)_{n\in\mathbb N}\)`be a [rational Cauchy sequence][bookofproofs$1485].
* It follows from the [definition of multiplying rational Cauchy sequences][bookofproofs$1488] and because [rational one is neutral with respect to the multiplication of rational numbers][bookofproofs$1482] that

`\[\begin{array}{ccll}
(x_n)_{n\in\mathbb N}\cdot (1)_{n\in\mathbb N}&=&(x_n\cdot 1)_{n\in\mathbb N}&\text{by definition of multiplying rational Cauchy sequences}\\
&=&(x_n)_{n\in\mathbb N}&\text{because }1\text{ is neutral with respect to the multiplication of rational numbers}\\
\end{array}\]`
* From the [commutativity of multiplying rational Cauchy sequences][bookofproofs$1502], it follows that also the equation `\((1)_{n\in\mathbb N}\cdot (x_n)_{n\in\mathbb N}=(x_n)_{n\in\mathbb N}\)` holds for all rational Cauchy sequences `\((x_n)_{n\in\mathbb N}\)`.
