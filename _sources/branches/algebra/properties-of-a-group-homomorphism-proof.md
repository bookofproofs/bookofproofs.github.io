layout: proof
categories: branches,algebra
nodeid: bookofproofs$681
orderid: 0
parentid: bookofproofs$680
title: 
description: DIRECT PROOF Proof of PROPERTIES OF A GROUP HOMOMORPHISM ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$677
keywords: properties of group homomorphism,property of group homomorphism,properties of group homomorphisms,property of group homomorphisms,properties of homomorphism,group homomorphism properties,homomorphism properties,group homomorphism,properties of homomorphisms,homomorphism property,group homomorphism pdf,proof
contributors: bookofproofs

---


---

### Proof of (1)

* Since `\(f\)` is a [group homomorphism][bookofproofs$679], it follows for the [identity][bookofproofs$661] `\(e_G\)` of the [group][bookofproofs$671] `\((G,\ast)\)` that `$f(e_G)=f(e_G\ast e_G)=f(e_G)\cdot f(e_G).$`
* The multiplication (inside the group `\(H\)`) of the equation with the element and `\(f(e_G)^{-1}\)` gives us   `$f(e_G)\cdot f(e_G)^{-1}=f(e_G)\cdot f(e_G)\cdot f(e_G)^{-1}.$` 
* This can be simplified to `$e_H=f(e_G)\cdot e_H=f(e_G).$`

### Proof of (2)

* In order to show `\(f(x^{-1})=f(x)^{-1}\)`, we multiply the equation (inside the group `\(H\)`) with `\(f(x)\)`, use the homomorphism property of `\(f\)` and the result in (1), which gives us `$f(x)\cdot f(x^{-1})=f(x\ast x^{-1})=f(e_G)=e_H.$`
* After multiplying both sides of the equation with `\(f(x)^{-1}\)`, we get `$f(x)^{-1}\cdot f(x)\cdot f(x^{-1})=f(x)^{-1}\cdot e_H.$`
* This can be simplified to `$e_H\cdot f(x^{-1})=f(x)^{-1},$` and finally to `$f(x^{-1})=f(x)^{-1}.$`
