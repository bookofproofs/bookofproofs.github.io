layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3533
orderid: 50
parentid: bookofproofs$8184
title: 
description: PROOF OF COUNTING THE ROOTS OF A DIOPHANTINE POLYNOMIAL MODULO A PRIME NUMBER &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: counting,diophantine,modulo,number,polynomial,prime,roots,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p$` is a [prime number][bookofproofs$473] and `$f(x)=a_0+a_1x+\ldots+a_nx^n$` a [polynomial][bookofproofs$487] of the degree `$n$` with [integer][bookofproofs$844] coefficients `$a_0,\ldots,a_n$` and with `$p\not\mid a_n$`.  
* If `$n=0$` then since `$p\not\div a_0$`, we have `$a_0(p)\not\equiv 0(p)$` and the polynomial has no [roots][bookofproofs$6736].
* Let `$n > 0$` and let the claim be correct for `$n-1.$`
* Assume, `$f(x)(p)\equiv 0(p)$` had more than `$n$` roots.
   * In particular, assume `$x_0,x_1,\ldots,x_n$` are `$n+1$` roots. Then
`$$\begin{array}{rcl}
f(x)-f(x_0)&=&\sum_{r=1}^na_i(x^r-x_0^r)\\
&=&(x-x_0)\sum_{r=1}^na_r(x^{r-1}+x_0x^{r-2}+\ldots+x_0^{r-2}x+x_0^{r-1})\\
&=:&(x-x_0)g(x)
\end{array}$$`
with some polynomial `$g(x)=b_0+b_1x_1+\ldots+b_{n-1}x^{n-1},$` such that `$b_{n-1}=c_n$` and `$p\not\mid b_{n-1}.$`
   * Therefore, for `$k=1,\ldots,n$` we have `$$(x_k-x_0)g(x_k)\equiv f(x_k)-f(x_0)\equiv 0-0\equiv 0\mod p.$$`
   * It follows that `$g(x_k)(p)\equiv 0(p)$` would have `$n$` roots for `$k=1,\ldots,n$`, in [contradiction][bookofproofs$744] to the result that it has only at most `$n-1$` roots.
* Therefore, the assumption `$f(x)(p)\equiv 0(p)$` had more than `$n$` roots is wrong.
* Thus, `$f(x)(p)\equiv 0(p)$` has at most `$n$` roots.
