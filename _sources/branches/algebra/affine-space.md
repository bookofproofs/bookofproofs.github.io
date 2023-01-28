layout: definition
categories: branches,algebra
nodeid: bookofproofs$6277
orderid: 500
parentid: bookofproofs$404
title: Affine Space
description: AFFINE SPACE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1038
keywords: affine,afine space,afine spaces,affine space,affine space definition
contributors: bookofproofs

---


---

An **afine space** `\(\mathcal A\)` over a [field][bookofproofs$557] `\(F\)` is a triple `\(\mathcal A:=(A,V_A,v)\)`, in which

* `\(A\)` is a [set][bookofproofs$550],
* the elements `\(P\in A\)` are called **points**.
* `\(V_A\)` is a [vector space over the field `\(F\)` ][bookofproofs$560],
* `\(v:A\times A\mapsto V_A\)` is a [function][bookofproofs$592] with the following properties:
   * Any two points `\(P,Q\in \mathcal A\)` uniquely determine a vector `\(x\in V_A\)` with `\(x=v(P,Q)=P-Q=\overrightarrow{PQ}\)`. We might also express it equivalently as `\(P=Q+x\)`, i.e. we get the point `\(Q\)`, if we **translate** the point `\(P\)` by the vector `\(x\)`. 
   * For all `\(P,Q,R\in \mathcal A\)`, we have `\(\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PR}\)`, i.e. if we translate the point `\(P\)` by one vector and then translate the translated vector by another vector, then the final point is a single translation of the initial point by a third vector.
