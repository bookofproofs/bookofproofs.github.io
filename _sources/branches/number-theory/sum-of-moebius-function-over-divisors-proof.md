layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8143
orderid: 50
parentid: bookofproofs$8142
title: 
description:  Proof of SUM OF MöBIUS FUNCTION OVER DIVISORS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: divisors,function,moebius,over,sum,sum of mobius function over divisors,proof
contributors: bookofproofs

---


---

* Let `$n\ge 1$` be a  [natural number][bookofproofs$718].
* For `$n=1,$` the [sum][bookofproofs$261] of the  [Möbius function][bookofproofs$8116] over the [divisors][bookofproofs$700] of `$n$` equals `$\sum_{d\mid 1}\mu(d)=\mu(1)=1,$` as required.

* For `$n > 1$` with the [factorization][bookofproofs$803] `$n=p_1^{e_1}\cdots p_r^{e_r},$` we have `$\mu(d)=0$` for non [square-free][bookofproofs$8116] divisors `$d\mid n.$` 
* In the remaining sum, there are exactly `$\binom rk$` square-free divisors `$d$` with exactly `$k$` different [prime][bookofproofs$473] factors.
* By the definition of the Möbius function, it follows
`$$\begin{array}{rcl}
\sum_{d\mid n}\mu(d)&=&\sum_{d\mid n,\text{ square-free}}\mu(d)=1+\binom{r}{1}(-1)+\binom{r}{2}+\cdots+\binom{r}{2}(-1)^r\\
&=&\sum_{k=0}^r\binom rk(-1)^k.
\end{array}$$`
* The last sum equals by the [binomial theorem][bookofproofs$1397] `$(1-1)^r=0.$`
