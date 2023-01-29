layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$8644
orderid: 50
parentid: bookofproofs$8643
title: By Induction
description: PROOF OF GEOMETRIC SUM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: geometric sum,geometric sums,proof
contributors: bookofproofs

---


---

* By hypothesis, `$a,b\in R$` are elements of a [unit ring][bookofproofs$683] `$R,$` and `$n\in\mathbb N$` is a [natural number][bookofproofs$718].
* We provide a [proof by induction][bookofproofs$657] on `$n.$`
* Base case: `$n=0$`
`$$(a-b)\sum_{k=0}^0 a^k\cdot b^{-k}=(a-b)\cdot 1=a^1-b^1.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$(a-b)\sum_{k=0}^n a^k\cdot b^{n-k}=a^{n+1}-b^{n+1}$$` holds for some `$n\ge 0.$`
   * Then `$$\begin{align}(a-b)\sum_{k=0}^{n+1} a^k\cdot b^{n+1-k}&=(a-b)\sum_{k=0}^{n} a^k\cdot b^{n+1-k}+(a-b)\cdot ( a^{n+1}b^{0})\nonumber\\
&=b(a-b)\sum_{k=0}^{n} a^k\cdot b^{n-k}+a^{n+2}-a^{n+1}b\nonumber\\
&=b(a^{n+1}- b^{n+1})+a^{n+2}-a^{n+1}b\nonumber\\
&=ba^{n+1}- b^{n+2}+a^{n+2}-a^{n+1}b\nonumber\\
&=a^{n+2}-b^{n+2}\nonumber\\
\end{align}$$`
* Thus, the geometric sum holds for all `$n\in\mathbb N.$`
