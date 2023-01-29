layout: proof
categories: branches,analysis
nodeid: bookofproofs$2983
orderid: 50
parentid: bookofproofs$6638
title: By Induction
description: Proof of INEQUALITY BETWEEN SQUARE NUMBERS AND POWERS OF $2$ ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: inequality between square numbers and powers of 2,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for all [natural numbers][bookofproofs$718] `$n\in\mathbb N.$`

* Base case: `$n=0$`
`$$0^2 < 2^0=1.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$n^2 < 2 ^n$$` is correct for an `$n\ge 0.$` 
   * Then `$$\begin{align}(n+1)^2&=n^2+2n+1\nonumber\\
& \le n^2+n^2\nonumber\\
&=2\cdot n^2.\nonumber\\
& < 2\cdot 2^n\quad\text{(by assumption)}\nonumber\\
&=2^{n+1}\nonumber
\end{align}$$`
* Thus, the sum of consecutive [odd numbers][bookofproofs$8130] from `$1$` to `$n$` equals the square of `$n.$`
