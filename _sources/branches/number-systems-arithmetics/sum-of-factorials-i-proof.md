layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$8640
orderid: 50
parentid: bookofproofs$8639
title: By Induction
description: PROOF OF SUM OF FACTORIALS I &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: sum of factorials (i),proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for all [natural numbers][bookofproofs$718] `$n.$`
* Base case: `$n=0$`
`$$\sum_{k=0}^0 k\cdot k !=0\cdot 0 !=0\cdot 1=1-1=(0+1)!-1.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$\sum_{k=0}^n k\cdot k !=(n+1) !-1$$` is correct for an `$n\ge 0.$`
   * Then `$$\begin{align}\sum_{k=0}^{n+1} k\cdot k !&=\sum_{k=0}^{n} k\cdot k ! + (n+1)\cdot (n+1) !\nonumber\\
&=(n+1)!-1 +(n+1)\cdot (n+1) !\nonumber\\
&=(n+2)!-1.\nonumber\end{align}$$`
* Thus, the above sum of [factorials][bookofproofs$1005] holds for all [natural numbers][bookofproofs$718] `$n\in\mathbb N.$`
