layout: proof
categories: branches,algebra
nodeid: bookofproofs$6331
orderid: 50
parentid: bookofproofs$71
title: 
description:  Proof of QUOTIENT SPACE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: quotient space,quotient spaces,proof
contributors: @Brenner,bookofproofs

---


---

* By hypothesis, `\(V\)` is a [vector space][bookofproofs$560] over a [field][bookofproofs$557] `\(F\)`, and `\(U\subseteq V\)` is its [subspace][bookofproofs$562] defining the [equivalence relation induced by `\(U\)` on `\(V\)` ][bookofproofs$6328] with the quotient set `\(V/U\)`. 
* Because the [canonical projection][bookofproofs$6330] `\(q\colon V\longrightarrow V/U,\,v\longmapsto [v]\,,\)` must become a [linear map][bookofproofs$403] over the field `\(F\)`, it has to fulfill the properties 
   * addition `\([v]+[w]=[v+w]\)` for all [equivalent classes][bookofproofs$574] in `\(V/U\)` and
   * scalar multiplication `\(\lambda [v]=[\lambda v]\)` for all `\[[v]\in V/U\]` and `\(\lambda \in F\)`.
* Because the above properties have to be valid for all elements, there can only be only one quotient space `\(V/U\)` such that `\(q\)` is a linear map over `\(F\)`. 
* The above properties do not depend on the representatives of the equivalence classes. 
   * Let `\([v]=[v']\)` and `\([w]=[w']\)`. We have to show that `\([v+w]=[v'+w']\)`. By hyothesis, we can set `\(v'=v+u\)` and `\(w'=w+u'\)` with some `\(u,u'\in U\)`. It follows `\[v'+w'=v+w+u+u'\,\]`
and the representative `\(v+w+u+u'\)` is equivalent to the representative `\(v+w\)` because of `\(u+u'\in U\)`. 
   * Similarly, let `\(v'=v+u\)` with `\(u\in U\)`. Then it follows `\[\lambda v'=\lambda (v+u)=\lambda v+\lambda u\,,\]`
and the representative `\(\lambda v+\lambda u'\)` is equivalent to `\(\lambda v\)` because of `\(\lambda u \in U\)`. 
* Because the addition and the scalar multiplication on `\(V/U\)` are well-defined and because `\(q\)` is [surjective][bookofproofs$770] it follows that `\(V/U\)` `\(q\)` is linear map and that the quotient space `\(V/U\)` is a vector space.
