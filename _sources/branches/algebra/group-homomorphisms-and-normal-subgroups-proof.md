layout: proof
categories: branches,algebra
nodeid: bookofproofs$835
orderid: 50
parentid: bookofproofs$832
title: 
description: Proof of GROUP HOMOMORPHISMS AND NORMAL SUBGROUPS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$696
keywords: group homomorphisms,normal subgroups,group homomorphism,normal subgroup,proof
contributors: bookofproofs

---


---

* By hypothesis, `\(f:(G,\ast)\mapsto (H,\cdot)\)` is a [group homomorphism][bookofproofs$679].
* Due to the [corresponding lemma][bookofproofs$833], the [kernel][bookofproofs$809] `\(\ker(f)\)` is a [subgroup][bookofproofs$554] of `\(G\)`. 
* It remains to be shown that it is a [normal subgroup][bookofproofs$273] of `$G.$`
   * Let `$g\in G$` and `\(h\in \ker(f)\)`, i.e. `$f(h)=e_H.$` 
   * It follows from the [properties of group homomorphism][bookofproofs$680] that `$$\begin{array}{rcl}f(g\ast h\ast g^{-1})&=&f(g)\cdot f(h)\cdot f(g^{-1})\\&=&f(g)\cdot e_H\cdot (f(g))^{-1}\\&=&f(g)\cdot f(g)^{-1}\\&=&e_H.\end{array}$$`
   * Thus, `$g\ast h\ast g^{-1}\in \ker(f)$` for any `$g\in G$` and any `$h\in \ker(f).$` 
   * Therefore, `$\ker(f)$` is a normal subgroup of `\(G\)`, i.e. `$\ker(f)\unlhd G.$`
