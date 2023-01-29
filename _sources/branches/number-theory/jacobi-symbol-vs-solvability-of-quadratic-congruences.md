layout: explanation
categories: branches,number-theory
nodeid: bookofproofs$8220
orderid: 200
parentid: bookofproofs$8213
title: Jacobi Symbol vs. Solvability of Quadratic Congruences
description: JACOBI SYMBOL VS. SOLVABILITY OF QUADRATIC CONGRUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8187
keywords: congruences,jacobi,quadratic,solvability,symbol
contributors: bookofproofs

---


---

We have introduced the [Legendre symbol][bookofproofs$8198] `$\left(\frac ap\right)$` as an indicator, if a given quadratic [congruence][bookofproofs$8153] `$x^2(p)\equiv a(p)$` is solvable for a given [odd][bookofproofs$8130] [prime number][bookofproofs$473] `$p,$` and a given [integer][bookofproofs$844] `$a.$` 

The [Jacobi symbol][bookofproofs$8214] `$\left(\frac an\right)$` is a generalization of the Legendre symbol, allowing the case if the number `$n$` is not a prime number. A big advantage of this generalization is that it extremely simplifies the calculation of Legendre symbols. It is no more necessary to know the [factorization][bookofproofs$803] of the number `$|a|,$` the knowledge of which was required when applying calculation rules developed for Legendre symbols (see [calculating Legendre symbols][bookofproofs$8204]). Now, we can simply apply the [properties of the Jacobi symbol][bookofproofs$8216] and transform a given Legendre symbol consecutively into a simpler one until we can calculate it directly (see [applications of the Jacobi symbol][bookofproofs$8218] for examples of such transformations).

But does the Jacobi symbol `$\left(\frac an\right)$` say anything about the solvability of the [congruence][bookofproofs$8153] `$x^2(n)\equiv a(n),$` if `$n$` is composite? Not quite and you should be cautious with such conclusions! Namely:

* If `$\left(\frac an\right)=-1,$` then the congruence is `$x^2(n)\equiv a(n)$` _is for sure_ not solvable. If it was, then `$x^2(p)\equiv a(p)$` would be solvable modulo each prime number `$p$` dividing `$n.$` But in this case, we would have `$\left(\frac an\right)=1$` by definition of the [Jacobi symbol][bookofproofs$8214].
* If `$\left(\frac an\right)=1,$` then the congruence _might be_ solvable, but it can also be not solvable! For instance, if `$a$` is a [quadratic nonresidue][bookofproofs$8196] modulo a prime `$p$` and `$n=p^2$`, then `$\left(\frac an\right)=1,$` but `$x^2(n)\equiv a(n)$` is not solvable.
