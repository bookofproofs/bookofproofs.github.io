layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$2970
orderid: 50
parentid: bookofproofs$6624
title: By Induction
description: Proof of SUM OF CONSECUTIVE ODD NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: sum of consecutive odd numbers,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for all [natural numbers][bookofproofs$718] `$n.$`
* Base case: `$n=1$`
`$$\sum_{k=1}^1(2k-1)=2\cdot 1-1=1=1^2.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$\sum_{k=1}^n (2k-1)=n^2$$` is correct for an `$n\ge 1.$`
   * Then `$$\begin{align}\sum_{k=0}^{n+1} (2k-1)&=n^2+(2(n+1)-1)\nonumber\\
&=n^2+2n+1\nonumber\\
&=(n+1)^2.\nonumber\end{align}$$`
* Thus, the sum of consecutive [odd numbers][bookofproofs$8130] from `$1$` to `$n$` equals the square of `$n.$`
