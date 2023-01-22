layout: proof
categories: branches,algebra
nodeid: bookofproofs$826
orderid: 0
parentid: bookofproofs$825
title: 
description: Proof of SUBGROUPS OF FINITE CYCLIC GROUPS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: finite cyclic groups,subgroups,proof
contributors: bookofproofs
issues: broken-links

---


---

* Let `\((G,\ast)\)` be a [finite][bookofproofs$985] "cyclic group":https://www.bookofproofs.org/branches/cyclic-group-order/ [generated by][bookofproofs$8265] `\(g\)`, i.e. `\(G=\langle g \rangle\)` with `\(|G|=n\)`. 
* Furthermore, let `\(d\mid n\)` be a [divisor][bookofproofs$700] of `$n$`, there is a `\(k\in\mathbb Z\)` with `\(d\cdot k=n\)`. 

### Existence

* Following the lemma about [subgroups of cyclic groups][bookofproofs$817], the element `\(g^k\in G\)` generates a subgroup `\(H=\langle g^k\rangle \subseteq G\)`. 
* Because `\((g^k)^d=g^{kd}=g^n=e\)`, the [order][bookofproofs$808] of `\(g^k\)` in `\(G\)` is `\(d\)`.
* Thus, `\(|H|=d\)`.

### Uniqueness

* If there was another subgroup `\(H'\subseteq G\)` with `\(|H'|=d\)`, but `\(H'\neq H\)`, then it would be generated by the element  `\(g^j\in G\)` with `\(j\neq k\)`. 
* This is a [contradiction][bookofproofs$744] to `\(dj=n=dk\)`, which is equivalent to `\(j=k\)`.