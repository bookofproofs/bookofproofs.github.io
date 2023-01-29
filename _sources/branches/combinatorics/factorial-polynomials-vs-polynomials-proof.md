layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8420
orderid: 50
parentid: bookofproofs$8419
title: By Induction
description: PROOF OF FACTORIAL POLYNOMIALS VS. POLYNOMIALS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8404
keywords: factorial polynomials versus polynomials,proof
contributors: bookofproofs

---


---

Proof of the statement [by induction][bookofproofs$657].
### "`$\Rightarrow$`"

* Let `$\phi(x)=a_nx^{\underline{n}}+a_{n-1}x^{\underline{n-1}}+\ldots+a_1x^{\underline{1}}+a_0$` be a [factorial polynomial][bookofproofs$8418] of degree `$n\ge 0.$`
* Base case `$n=0:$`
   * If `$\phi(x)=a_0$` then set `$b_0:=a_0$` and we have `$\phi(x)=b_0.$`
* Induction Step `$n\to n+1$` 
   * Assume, `$n\ge 0$` and _any_ factorial polynomial `$$\phi(x)=a_mx^{\underline{m}}+a_{m-1}x^{\underline{m-1}}+\ldots+a_1x^{\underline{1}}+a_0$$` of degree `$m$` equals some [polynomial][bookofproofs$252] `$$\phi(x)=b_mx^{m}+b_{m-1}x^{m-1}+\ldots+b_1x^{1}+b_0$$` of degree `$m$` for all `$m\le n.$`
   * By definition of the [falling factorial power][bookofproofs$1399], we have `$$x^\underline{n+1}=x(x-1)\cdots(x-m)=x^{n+1}+p(x),$$` where `$p(x)$` is some polynomial of degree `$n.$` 
   * By induction hypothesis, `$\phi(x)=a_{n+1}x^\underline{n+1}+q(x)$` with a polynomial `$q(x)$` of degree `$n.$`
   * Thus, `$\phi(x)=a_{n+1}(x^{n+1}+p(x))+q(x)=a_{n+1}x^{m+1}+s(x),$` where `$s(x)=a_{n+1}p(x)+q(x)$` is a polynomial of degree `$n.$`
* Thus, `$\phi(x)$` can be written as a [polynomial][bookofproofs$252] of degree `$n+1$`. 

### "`$\Leftarrow$`"

* analogously
