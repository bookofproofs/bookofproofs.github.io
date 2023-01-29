layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1002
orderid: 50
parentid: bookofproofs$1001
title: 
description: Proof of NUMBER OF ORDERED n-TUPLES IN A SET ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8297
keywords: ordered pairs in sets,ordered pairs in a set,n-tuples in a set,n-tuples and sets,proof
contributors: bookofproofs

---


---

* Let `$X$` be a [non-empty set][bookofproofs$550] and let `$\{a_1,a_2,\ldots,a_n\}$` be a [finite set][bookofproofs$985] with `$n\ge 1$` elements.
* A given [map][bookofproofs$592] `$f:\{a,b\}\to X$` determines uniquely an [ordered n-tuple][bookofproofs$747]  `$(x_1,x_2,\ldots,x_n)$` of elements `$x_i\in X$`  by setting `$x_i:=f(a_i)$` for `$i=1,\ldots,n.$`
* Vice versa, every ordered n-tuple `$(x_1,\ldots,x_n)$` uniquely determines a map `$f:\{a_1,\ldots,a_b\}\to X$` such that `$f(a_i):=x_i$` for `$i=1,\ldots,n.$`
* Therefore, the number of different [maps][bookofproofs$592] of the set `$\{a_1,a_2,\ldots,a_n\}$` to the set `$X$` is [equipotent][bookofproofs$978] to the  [Cartesian product][bookofproofs$748] `$$\underbrace{X\times X\times\cdots\times X}_{n\text{ 
 times}},$$` since the latter consists exactly of the ordered n-tuples `$(x_1,x_2,\ldots,x_n).$`
* Now, let `$X$` be [finite][bookofproofs$985] with the [cardinality][bookofproofs$980] `$|X|=m.$`
* According to the [fundamental counting principle][bookofproofs$111], the [cardinality][bookofproofs$980] of the `$n$`-fold Cartesian product is `$m^n.$`
