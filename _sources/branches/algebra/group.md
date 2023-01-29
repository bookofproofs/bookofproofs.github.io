layout: definition
categories: branches,algebra
nodeid: bookofproofs$671
orderid: 100
parentid: bookofproofs$212
title: Group
description: GROUP ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$6907
keywords: group,groups
contributors: bookofproofs

---


---

A **group** `$(G,\ast)$` is a [monoid][bookofproofs$659], in which an [inverse element][bookofproofs$670] exists for each element, i.e. for all `$x\in G$` there is an `$x^{-1}\in G$` with `$x\ast x^{-1} =x^{-1}\ast x=e,$` where `$e\in G$` is the [neutral element][bookofproofs$661].
Please note that `$e\in X$` is [unique][bookofproofs$669] in `$G$` and `$x^{-1}$` is [unique][bookofproofs$359] for all `$x\in G.$`

"Unfolding" all definitions, a _group_ fulfills the following axioms:

* Associativity: `$x\ast (y\ast z)=(x\ast y)\ast z$` for all `$x,y,z\in G.$`
* Neutral Element: There is an element `$e\in G$` with `$e\ast x=x\ast e=x$` for all `$x\in G.$`
* Inverse elements: For all `$x\in G$` there exists an `$x^{-1}\in G$` with `$x\ast x^{-1} =x^{-1}\ast x=e.$`

### Notes

* For technical reasons, these axioms are not minimal. 
* It is also possible to define a group if we require only the existence of a [left-neutral][bookofproofs$661] (respectively a [right-neutral][bookofproofs$661]), and the existence of [left-inverse][bookofproofs$670] (respectively a  [right-inverse][bookofproofs$670]) elements. 
* The reader might encounter this approach in some sources.
