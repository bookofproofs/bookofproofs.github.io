layout: example
categories: branches,algebra
nodeid: bookofproofs$6820
orderid: 200
parentid: bookofproofs$212
title: Examples of Groups
description: EXAMPLES OF GROUPS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6735
keywords: examples of groups,group examples,group example
contributors: bookofproofs

---


---

### Examples

The following are examples of [groups][bookofproofs$671] and the reader is invited to verify the defining properties of a group for each of the examples.

* The set `$(\mathbb Z, + )$` of [integers][bookofproofs$1654], together with addition is a group.
* The set of `$(\mathbb Q, + )$` of [rational numbers][bookofproofs$1033] under addition forms a group. 
* The set of non-zero `$(\mathbb Q^*,\cdot)$` of rational numbers under multiplication forms a group. 
* The set of `$(\mathbb R,+ )$` of [real numbers][bookofproofs$1105] under addition forms a group. 
* The set of non-zero `$(\mathbb R^*,\cdot)$` of real numbers under multiplication forms a group. 
* The set of `$(\mathbb C,+ )$` of [complex numbers][bookofproofs$216] under addition forms a group. 
* The set of non-zero `$(\mathbb C^*,\cdot)$` of complex numbers under multiplication forms a group.
* Let `$(G,\ast)$` be a group and let `$S$` be a non-empty set. The set `$(M,\circ)$` of maps `$f,g:S\to G$` is itself a group for each `$x\in S$`, with the binary operation `$(f\circ g)(x):=f(x)\ast g(x)$` and the inverse `$f^{-1}(x):=(f(x))^{-1}\in G$`. The identity element is the map `$e'\in M$` which maps the element `$x$` to the identity element `$e\in G$`.
* Let `$S$` be a non-empty set and let `$G$` be the set of bijective mappings `$f:S\to S$`. Then `$(G,\circ)$` is a group with the composition of mappings `$(f\circ g)(x):=f(g(x))$` for all `$x\in S$`. The identity element is the identity map `$id:S\to S$` and, since all mappings `$f\in G$` are bijective, `$G$` contains inverse mappings `$f^{-1}\in G$` for all `$f\in G$`. This example is called a *symmetric group.*
* Let `$V$` be a [vector space][bookofproofs$560] over a field `$F$`. Let `$GL(V)$` denote the set of invertible linear maps of `$V$` onto itself. Then `$(GL(V),\circ)$` is a group, where the binary operation `$\circ$` denotes the composition of mappings.
* Let `$V$` be a vector space over a field `$F$`. Let `$GL(V,F)$` denote the set of invertible `$n\times n$` matrices with components in `$F$`. Then `$(GL(F),\circ)$` is a group, where the binary operation `$\circ$` denotes the [matrix multiplication][bookofproofs$1050] This group is called the **general linear group**.
* The [direct product of groups][bookofproofs$6822] is a group.

### Counterexamples

The following are examples which are not groups:

* The set `$(\mathbb N, + )$` of [natural numbers][bookofproofs$718], together with addition is not a group since not all natural numbers have an inverse element. In fact, only `$0\in \mathbb N$` is the only element with the inverse `$-0\in\mathbb N.$`
* The set `$(\mathbb Z, \cdot )$` of integers together with multiplication is not a group, since not all elements `$a\in \mathbb Z$` have an inverse, e.g. `$2\in \mathbb Z$` but `$\frac 12\not\in\mathbb Z.$`
* The set `$(\mathbb R,\ast)$` of [real numbers][bookofproofs$1105], together with the mean value operation `$a \ast b=\frac{a+b}2$` is not a group, since this operation is not [associative][bookofproofs$668]
