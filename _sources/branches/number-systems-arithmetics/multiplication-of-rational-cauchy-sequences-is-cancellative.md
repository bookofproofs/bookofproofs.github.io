layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1571
orderid: 400
parentid: bookofproofs$1488
title: Multiplication of Rational Cauchy Sequences Is Cancellative
description: MULTIPLICATION OF RATIONAL CAUCHY SEQUENCES IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: multiplication,rational cauchy sequences,cauchy sequence,definition of cauchy sequence,define cauchy sequence,what is a cauchy sequence,what is cauchy sequence,proof
contributors: bookofproofs

---


---

The [multiplication of rational Cauchy sequences][bookofproofs$1488] is [cancellative][bookofproofs$837], i.e. for all [rational Cauchy sequences][bookofproofs$1485] `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`  and `\((z_n)_{n\in\mathbb N}\)` such that `\((z_n)_{n\in\mathbb N}\)` is [not convergent][bookofproofs$1572] to `\(0\)`, there exists `\(N\in\mathbb N\)` such that for all sequence members with indices `\(n > N\)`, following laws (both) are fulfilled:

* **Left cancellation property**:
If the equation `\((z_n)_{n > N}\cdot (x_n)_{n > N}=(z_n)_{n > N} \cdot (y_n)_{n > N}\)` holds, then `\((x_n)_{n > N}=(y_n)_{n > N}\)`.  

* **Right cancellation property**:
If the equation `\((x_n)_{n > N}\cdot (z_n)_{n > N}=(x_n)_{n > N} \cdot (z_n)_{n > N}\)` holds, then `\((x_n)_{n > N}=(y_n)_{n > N}\)`.  

Conversely, for a rational Cauchy sequence `\((z_n)_{n\in\mathbb N}\)`, which is not convergent to `\(0\)`, there exists a natural number `\(N\)` such that the equation `\((x_n)_{n > N}=(y_n)_{n > N}\)` implies 
* `\((z_n)_{n  > N}\cdot (x_n)_{n  > N}=(z_n)_{n  > N} \cdot (y_n)_{n  > N}\)` and 
* `\((x_n)_{n  > N}\cdot (z_n)_{n > N}=(x_n)_{n > N} \cdot (z_n)_{n > N}\)`.
