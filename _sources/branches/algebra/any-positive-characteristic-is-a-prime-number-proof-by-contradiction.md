layout: proof
categories: branches,algebra
nodeid: bookofproofs$883
orderid: 50
parentid: bookofproofs$882
title: 
description: PROOF OF ANY POSITIVE CHARACTERISTIC IS A PRIME NUMBER &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: any,characteristic,number,positive,prime,proof
contributors: bookofproofs

---


---

* By assumption, `\((R, +,\cdot)\)` is a [ring][bookofproofs$683] with a multiplicative identity `\(1\)` and an additive identity `\(0\)`, which is free of [zero divisors][bookofproofs$821] 
* If the [characteristic][bookofproofs$881] is `\(\operatorname{char}( R )=0\)`, there is nothing to show. 
* Suppose `$\operatorname{char}( R )=n,$` `$n > 0$` is [composite][bookofproofs$8097]
* Therefore, there exist [positive integers][bookofproofs$1075] `\(a,b\in\mathbb N\)` with `\(1 < a,b < n\)` and `\(a\cdot b=n\)`. 
* It follows `$n\cdot 1=(a\cdot b)\cdot 1=(a\cdot 1)\cdot(b\cdot 1)=0.$`
* Since `\(R\)` is free of [zero divisors][bookofproofs$821], we have  `$(a\cdot 1)\cdot(b\cdot 1)=0\Longleftrightarrow (a\cdot 1)=0 \text{ or } (b\cdot 1)=0.$` 
* But this is a [contradiction][bookofproofs$744] to the minimality of the characteristic, by its definition.
* Thus, `$n > 0$` is a [prime number][bookofproofs$473]
