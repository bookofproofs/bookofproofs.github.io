layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8043
orderid: 50
parentid: bookofproofs$8042
title: By Induction
description:  Proof of SET-THEORETICAL MEANING OF ORDERED TUPLES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$983
keywords: meaning,ordered,set,theoretical,tuples,proof
contributors: bookofproofs

---


---

We use a proof by [complete induction][bookofproofs$657].
### Base case: `$n=1$`

* If `$(x_1)=(y_1)$` then, by definition of [$n$-tuple][bookofproofs$747] `$\{x_1\}=\{y_1\}.$`
* By definition of [singleton][bookofproofs$8034] and using the [axiom of foundation][bookofproofs$717] as well as the [axiom of extensionality][bookofproofs$551], it followis `$x_1=y_1.$`

### Induction step: `$n\ge 1$`

* By base case, `$(x_1,\ldots,x_n)=(y_1,\ldots,y_n)$`. For readability reasons, we write `$x^{(n)}=y^{(n)}.$`
* By the definition of `$n$`-tuple, we have `$(x_1,\ldots,x_{n+1})=(x^{(n)},x_{n+1})$` and `$(y_1,\ldots,y_{n+1})=(y^{(n)},y_{n+1}).$`
* By the definition of ordered pairs we have `$(x^{(n)},x_{n+1})=\{\{x^{(n)},x_{n+1}\},\{x_{n+1}\}\}$` and `$(y^{(n)},y_{n+1})=\{\{y^{(n)},y_{n+1}\},\{y_{n+1}\}\}.$`
* By the base case, the definition of [singleton][bookofproofs$8034], the [axiom of foundation][bookofproofs$717] and the [axiom of extensionality][bookofproofs$551], we have `$x_{n+1}=y_{n+1}.$`
