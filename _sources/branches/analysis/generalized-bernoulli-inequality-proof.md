layout: proof
categories: branches,analysis
nodeid: bookofproofs$8642
orderid: 50
parentid: bookofproofs$8641
title: By Induction
description: PROOF OF GENERALIZED BERNOULLI'S INEQUALITY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8311
keywords: generalized bernoulli's inequality,bernoulli's inequality,bernoulli's inequality proof,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for [natural numbers][bookofproofs$718] `$n.$`
* Base case: `$n=1$`
`$$\prod_{k=1}^1(1+x_k)=1+x_1\ge 1+\sum_{k=1}^1 x_k=1+x_1.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$\prod_{k=1}^n(1+x_k)\ge 1+\sum_{k=1}^n x_k$$` holds for some `$n\ge 1.$`
   * Then `$$\begin{align}\prod_{k=1}^{n+1}(1+x_k)&=\prod_{k=1}^{n}(1+x_k)\cdot (1+x_{n+1})\nonumber\\
&\ge \left(1+\sum_{k=1}^n x_k\right)\cdot (1+x_{n+1})\nonumber\\
&= 1+x_{n+1} +\sum_{k=1}^n x_k+x_{n+1}\cdot \sum_{k=1}^n x_k\nonumber\\
&= 1+\sum_{k=1}^{n+1} x_k+x_{n+1}\cdot \sum_{k=1}^n x_k\nonumber\\
&\ge 1+\sum_{k=1}^{n+1} x_k\nonumber\end{align}$$`
* Thus, the above [product][bookofproofs$8599] holds for all [natural numbers][bookofproofs$718] `$n\ge 1.$`
