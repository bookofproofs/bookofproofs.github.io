layout: proof
categories: branches,analysis
nodeid: bookofproofs$2984
orderid: 50
parentid: bookofproofs$6639
title: By Induction
description: PROOF OF INEQUALITY BETWEEN POWERS OF 2 AND FACTORIALS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: inequality between powers of 2 and factorials,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for all [natural numbers][bookofproofs$718] `$n\in\mathbb N.$`

* Base case: `$n=4$`
   * `$$16=2^4 < 4!=24.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$2^n < n !$$` is correct for an `$n\ge 4.$` 
   * Then `$$\begin{align}2^(n+1)&=2\cdot 2 n\nonumber\\
& < 2\cdot n !\quad\text{(by assumption)}\nonumber\\
& < (n+1)\cdot n ! \nonumber\\
& = (n+1) ! \nonumber
\end{align}$$`
* Thus, the powers of `$2$` are smaller than the corresponding [factorials][bookofproofs$1005] for `$n\ge 4.$`
