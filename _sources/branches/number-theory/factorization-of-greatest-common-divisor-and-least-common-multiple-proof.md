layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8121
orderid: 50
parentid: bookofproofs$2483
title: 
description:  Proof of FACTORIZATION OF GREATEST COMMON DIVISOR AND LEAST COMMON MULTIPLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,divisor,factorization,greatest,least,multiple,proof
contributors: bookofproofs

---


---

* Assume, Let `$n,m\in\mathbb N$` with `$n\ge 1,$` `$m\ge 1$` have the [factorizations][bookofproofs$803] `$n=\prod_{i=1}^\infty p_i^{e_i}$` and `$m=\prod_{i=1}^\infty p_i^{f_i}.$`
* We set `$d:=\prod_{i=1}^\infty p_i^{\min(e_i,f_i)}$`, `$\min(e_i,f_i)$` being the [minimum][bookofproofs$7995] of the respective exponents `$e_i,f_i.$`
   * It is clear that `$d\mid n$` is a [divisor][bookofproofs$700] of `$n,$` because `$\min(e_i,f_i)\le e_i$` and `$\min(e_i,f_i)\le f_i$` for all `$i.$`
   * For any other divisor `$t\mid a$` and `$t\mid b$` with the factorization `$d:=\prod_{i=1}^\infty p_i^{r_i}$` we have therefore `$r_i\le  \min(e_i,f_i)$` for all `$i.$`
   * Therefore, `$t\mid d$` and we have that `$d$` equals the [greatest common divisor][bookofproofs$1280] `$d=\gcd(n,m).$`
* Analogously, we set `$l:=\prod_{i=1}^\infty p_i^{\max(e_i,f_i)}$`, `$\max(e_i,f_i)$` being the [maximum][bookofproofs$7995] of the respective exponents `$e_i,f_i.$`
   * It is clear that `$n\mid l$`, i.e. `$l$` is a [multiple][bookofproofs$700] of `$n.$` This is because `$\max(e_i,f_i)\ge e_i$` and `$\max(e_i,f_i)\ge f_i$` for all `$i.$`
   * For any other multiple `$m$` of `$n$` with the factorization `$m:=\prod_{i=1}^\infty p_i^{s_i}$` we have therefore `$s_i\ge  \max(e_i,f_i)$` for all `$i.$`
   * Therefore, `$l\mid m$` and we have that `$l$` equals the [least common multiple][bookofproofs$1276] `$m=\operatorname{lcm}(n,m).$`
