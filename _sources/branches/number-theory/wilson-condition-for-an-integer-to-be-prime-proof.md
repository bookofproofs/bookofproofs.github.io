layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3538
orderid: 50
parentid: bookofproofs$8193
title: By Induction
description: PROOF OF WILSON'S CONDITION FOR AN INTEGER TO BE PRIME &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8152
keywords: condition,integer,prime,wilson,wilson's theorem,proof
contributors: bookofproofs

---


---

* Let `$n > 1$` be an [integer][bookofproofs$844], and let `$(n-1)!$` be the [factorial][bookofproofs$1005] of `$n-1.$` 

### "`$\Rightarrow$`"

* Assume `$n:=p$` is a [prime number][bookofproofs$473].
* Obviously, for `$p=2$`, we have `$1!=-1\mod 2.$` Therefore, assume `$p > 2$` is [odd][bookofproofs$8130].
* The [polynomial][bookofproofs$487] `$$f(x)=x^{p-1}-1-\prod_{m=1}^{p-1}(x-m)\label{eq:E18657a}\tag{1}$$` has the degree `$p-2$`, since the two terms in `$f(x)$` involving `$x^{p-1}$` cancel. 
* Therefore, the polynomial (we look at it modulo `$p$`) can be written as `$$f(x)\equiv c_0+c_1x+\cdots+c_{p-2}x^{p-2}\mod p,\label{eq:E18657b}\tag{2}$$` with some integers `$c_0,c_1,\ldots,c_{p-2}\in\mathbb Z.$`
* According to the [necessary condition for an integer to be prime][bookofproofs$8191], we have that `$(x^{p-1}-1)(p)\equiv 0(p)$` for `$x\equiv 1,2,\ldots,p-1\mod p.$` 
* Moreover, the product `$\prod_{m=1}^{p-1}(x-m)$` vanishes, since it has a factor equal to the congruence `$0(p).$`
* Therefore, the polynomial `$(\ref{eq:E18657a})$` is constructed in such a way that it has the roots `$x\equiv 1,2,\ldots,p-1\mod p.$` 
* But according to [counting the roots of a diophantine polynomial modulo a prime number][bookofproofs$8184], `$f(x)(p)\equiv 0(p)$` has _at most_ `$p-2$` roots, since it is of the degree `$p-2.$`
* Thus, since `$p$` divides both sides of the equation `$(\ref{eq:E18657b})$`, the coefficients `$c_0,c_1,\ldots,c_{p-2}$` must all be divisible by `$p$`, according to the [divisibility law no. 6][bookofproofs$508].
* In particular, `$p$` divides `$c_0=-1-(-1)^{p-1}(p-1)!.$` 
* This means that `$(-1)^{p-1}(p-1)!\equiv -1\mod p,$` or `$(p-1)!(p)\equiv -1(p),$` since `$p$` is odd.

### "`$\Leftarrow$`"

* Let `$(n-1)!(n)\equiv -1(n).$`
* According to [congruence modulo a divisor][bookofproofs$8171], we have `$(n-1)!(m)\equiv -1(m)$` for any [divisor][bookofproofs$700] `$m\mid n.$`
* But if `$m < n,$` then `$m$` appears as a factor of `$(n-1)!.$` 
* So `$(n-1)!(m)\equiv 0(m),$` and hence `$-1(m)\equiv 0(m).$`
* By definition of [congruence][bookofproofs$8153], this implies `$m\mid -1,$` or `$m=1.$`
* Therefore, `$n$` has only the trivial divisors `$n$` and `$1.$`
* By definition of [prime numbers][bookofproofs$473], `$n$` is prime.
