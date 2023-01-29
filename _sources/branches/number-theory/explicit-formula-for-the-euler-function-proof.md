layout: proof
categories: branches,number-theory
nodeid: bookofproofs$2789
orderid: 50
parentid: bookofproofs$2790
title: 800 BC
description: PROOF OF EXPLICIT FORMULA FOR THE EULER FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: euler,explicit,formula,function,proof
contributors: bookofproofs

---


---

* By [sum of Euler function][bookofproofs$6196], we have `$\sum_{d\mid n}\phi(d)=n.$`
* By [Möbius inversion][bookofproofs$8149], we have
`$$\phi(n)=\sum_{d\mid n}\mu(d)\frac nd=n\sum_{d\mid n}\frac{\mu(d)}d.$$`
* By [sum of Möbius function over divisors with division][bookofproofs$3247], 
`$$\phi(n)=n\prod_{k=1}^r\left(1-\frac1{p_k}\right),$$`
where `$n=\prod_{k=1}^r p_k^{e_k}$` is the [factorization][bookofproofs$803] of `$n.$`
* This is equivalent to 
`$$\begin{array}{rcl}\phi(n)&=&\prod_{k=1}^rp_k^{e_k}\left(1-\frac1{p_k}\right)\\
&=&\prod_{k=1}^r\left(p_k^{e_k}-p_k^{e_k-1}\right)\\
&=&\prod_{k=1}^r p_k^{e_k-1}(p_k-1),\end{array}$$` as required.
