layout: proof
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1186
orderid: 50
parentid: bookofproofs$1185
title: 
description:  Proof of LOOP-COMPUTABLE FUNCTIONS ARE TOTAL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: are,computable,functions,loop,total,proof
contributors: bookofproofs

---


---

Let `\(f : \mathbb N^k \to \mathbb N\)`  be a `\(L O O P\)`-computable function. We have to show that `\(f\)` is [total][bookofproofs$592], i.e. that `\(f(n_1,\ldots,n_k)\)` is defined for every input `\((n_1,\ldots,n_k)\in\mathbb N^k\)`.


By [definition of `\(L O O P\)`-computability][bookofproofs$1183], there exists a [finite][bookofproofs$985] [`\(L O O P\)` program][bookofproofs$1180] `\(P\)`, which computes `\(f\)`. Any LOOP command `\(\mathtt{LOOP~r_i~DO~P_1~END}\)` is repeated for a finite number of times, i.e. the natural number contained in the register `\(r_i\)`. Therefore, `\(P\)` must terminate for any input `\((n_1,\ldots,n_k)\in\mathbb N^k\)`. Therefore, `\(f\)` is total.
