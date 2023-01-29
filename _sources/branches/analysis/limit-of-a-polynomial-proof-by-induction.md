layout: proof
categories: branches,analysis
nodeid: bookofproofs$6898
orderid: 50
parentid: bookofproofs$6897
title: By Induction
description: PROOF BY INDUCTION Proof of LIMIT OF A POLYNOMIAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: limit,polynomial,proof
contributors: bookofproofs

---


---

### Context

* Let  `$n$` be a [natural number][bookofproofs$718].
* Let `$a, a_n,a_{n-1},\ldots,a_1,a_0\in\mathbb R$` be [real numbers][bookofproofs$1105].
* Let `$p:\mathbb R\to\mathbb R,$` `$p(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_1x+a_0$` be a [polynomial][bookofproofs$199] of the degree `$n.$` 
* We will provide a proof for the [limit][bookofproofs$6683].
`$$\lim_{x\to a }p(x)=p(a)$$`
on the degree `$n.$`

### Base Case

* For `$n=0$` we have that `$p(x)=a_0$`. 
* By the limit of the [constant function][bookofproofs$6891] it follows that `$\lim_{x\to a}a_0=a_0.$`

### Hypothesis

* Assume that for some natural number `$k$`, if `$p(x)=a_kx^k+a_{k-1}x^{k-1}+\ldots+a_1x+a_0$`, then `$\lim_{x\to a }p(x)=p(a)=a_ka^k+a_{k-1}a^{k-1}+\ldots+a_1a+a_0$`.

### Induction Step

* If if `$p(x)=a_{k+1}x^{k+1}+a_kx^k+a_{k-1}x^{k-1}+\ldots+a_1x+a_0,$` then by the [limit of `$n$`-th powers][bookofproofs$6895] and the [limit of product][bookofproofs$6685] it follows `$$\begin{array}{rcl}
\lim_{x\to a }p(x)&=&\lim_{x\to a }a_{k+1}x^{k+1}+a_kx^k+a_{k-1}x^{k-1}+\ldots+a_1x+a_0\\
&=&(\lim_{x\to a }a_{k+1}x^{k+1})+(\lim_{x\to a }a_kx^k+a_{k-1}x^{k-1}+\ldots+a_1x+a_0)\\
&=&(\lim_{x\to a }a_{k+1})(\lim_{x\to a }x^{k+1})+a_ka^k+a_{k-1}a^{k-1}+\ldots+a_1a+a_0\\
&=&a_{k+1}a^{k+1}+a_ka^k+a_{k-1}a^{k-1}+\ldots+a_1a+a_0\\
&=&p(a).
\end{array}$$`

### Conclusion

* By [induction][bookofproofs$657], it follows that `$\lim_{x\to a }p(x)=p(a)$` is true for all `$n\ge 0.$`
