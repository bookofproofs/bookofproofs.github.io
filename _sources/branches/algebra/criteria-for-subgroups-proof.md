layout: proof
categories: branches,algebra
nodeid: bookofproofs$812
orderid: 50
parentid: bookofproofs$811
title: 
description: Proof of CRITERIA FOR SUBGROUPS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$677,bookofproofs$696
keywords: criteria for subgroups,subgroup criterion,subgroup criteria,criterion for subgroup,proof
contributors: bookofproofs

---


---

### Proof for criterion `$(1)$`

"`\(\Rightarrow\)`"

* Let `\(H\subseteq G\)` be a [subgroup][bookofproofs$554] of the [group][bookofproofs$671] `\((G,\ast)\)`. 
* From the definition of the subgroup we have for `$a,b\in H$` that `$a\ast b^{-1}\in H.$`

"`\(\Leftarrow\)`"

* Assume `\(a\ast b^{-1}\in H\)` for all `\(a,b\in H\)`. 
* If `\(a=b\)`, we have `\(b\ast b^{-1}=e\)`, which means `$e\in H$`, i.e. `$H$` contains the [neutral element][bookofproofs$669].
* If `\(a=e\)`, we have `\(e\ast b^{-1}=b^{-1}\)`, which means if `$b\in H$` then `$b^{-1}\in H$`, i.e. `$H$` contains with `$b$` also its [unique inverse element][bookofproofs$359]  `$b^{-1}.$`
* If `\(a,b\in H\)`, then according to the above result, also `\(b^{-1}\in H\)`.
* By assumption, `$a\ast(b^{-1})^{-1}=a\ast b\in H$`. 
* Therefore `$H$` is [closed][bookofproofs$1103] under the operation `$"\ast".$`

### Proof for criterion `$(2)$`

* For any given `\(a,b\in H\)`, we have `\(a,b \in H_i\)` for every `\(i\in I\)`. 
* Therefore also `\(a^{-1},b^{-1}\in H_i\)`.
* By the definition of [set intersection][bookofproofs$6828], also `\(a^{-1},b^{-1}\in H\)`. 
* In particular, `\(a\ast b^{-1}\in H\)`. 
* By criterion `$(1),$` `\(H\)` is a [subgroup][bookofproofs$554] of `$G.$`
