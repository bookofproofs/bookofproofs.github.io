layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$2969
orderid: 50
parentid: bookofproofs$6623
title: By Induction
description: PROOF OF SUM OF CONSECUTIVE NATURAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: sum of consecutive natural numbers,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for all [natural numbers][bookofproofs$718] `$n.$`
* Base case: `$n=1$`
   * `$$\sum_{k=0}^1k =0 + 1=1(1+1)/2.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$\sum_{k=0}^n k=\frac{n(n+1)}2$$` is correct for an `$n\ge 1.$`
   * Then `$$\begin{align}\sum_{k=0}^{n+1} k&=\frac{n(n+1)}2+(n+1)\nonumber\\
&=\frac{n(n+1)+2(n+1)}{2}\nonumber\\
&=\frac{(n+1)(n+2)}2.\nonumber\end{align}$$`
