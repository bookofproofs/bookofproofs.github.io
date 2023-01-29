layout: proof
categories: branches,number-theory
nodeid: bookofproofs$6408
orderid: 50
parentid: bookofproofs$6407
title: 
description:  Proof of SETS OF INTEGERS CO-PRIME TO A GIVEN INTEGER ARE DIVISOR-CLOSED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: are,closed,divisor,given,integer,integers,prime,sets,proof
contributors: bookofproofs

---


---

* Assume, `\(d\ge 0\)` is a fixed [integer][bookofproofs$844].
* Case `\(d=0\)`:
   * Let `\(n\in \mathbb Z_0\)`. 
   * By [definition of `$Z_0$` ][bookofproofs$6405] we have `\(\gcd(n,0)=1\)` only for `\(n=1\)`, it follows that `\(\mathbb Z_0=\{1\}\)`.
   * Trivially, `\(\mathbb Z_0\)` is [divisor-closed][bookofproofs$6406].
* Case `\(d = 1\)`:
   * Let `\(n\in \mathbb Z_1\)`.
   * Since we have `\(\gcd(n,1)=1\)` for all `\(n\in \mathbb Z\)`, it follows  `\(\mathbb Z_1=\mathbb Z\)`.
   * Trivially, `\(\mathbb Z\)` is divisor-closed.
* Case `\(d > 1\)`:
   * There is a unique [factorization][bookofproofs$803] `\(|d|=p_1^{e_1}\cdot\ldots\cdot p_k^{e_k}\)` with `\(e_i\ge 0\)` for `\(i=1,\ldots,k\)`  by the [fundamental theorem of arithmetic][bookofproofs$8094].
   * Let `\(n\in \mathbb Z_d\)` and let `\(t\mid n\)`. We have to show that `\(t\in\mathbb Z_d\)`.
   * If `\(t=1\)`, then `\(\gcd(t,d)=1\)`. Thus, `\(t\in \mathbb Z_d\)`. 
   * If `\(t > 1\)`, then also `\(n > 1\)` and we have two unique factorizations: 
      * `\(n=q_1^{f_1}\cdot\ldots\cdot q_m^{f_m}\)` be with `\(0\le f_j\)` for `\(j=1,\ldots,m\)` and 
      * `\(t=q_1^{g_1}\cdot\ldots\cdot q_m^{g_m}\)` with `\(0\le g_j\le f_j\)` for `\(j=1,\ldots,m\)`, since `\(t\mid n\)`. 
   * Because `\(n\in \mathbb Z_d\)`, we have `\(\gcd(n,d)=1\)`. 
   * Thus, there is no such index `\(l\)`, `\(l=1,\ldots,\min(m,k)\)`, for which both exponents `\(e_l > 0\)` and `\(g_l > 0\)`. 
   * Otherwise, `\(\gcd(q_l^{e_l},q_l^{g_l})=q_l^{\min(e_l,g_l)}  > 1 \)`, because `\(\min(e_l,g_l)>1\)`, and we would have found a proper common divisor of `\(n\)` and `\(d\)`, contradicting `\(n\in\mathbb Z_d\)`.
   * For the same reason, `$t$` and`\(d\)` are [co-prime][bookofproofs$8093].
   * Thus, `\(t\in\mathbb Z_d\)`.
