layout: example
categories: branches,algebra
nodeid: bookofproofs$8652
orderid: 200
parentid: bookofproofs$679
title: Examples of Properties of Group Homomorphisms
description: PROPERTIES OF GROUP HOMOMORPHISMS BY EXAMPLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: examples of properties of group homomorphisms
contributors: bookofproofs

---


---

We want to verify the [properties of group homomorphisms][bookofproofs$680] for the [examples given for group homomorphisms][bookofproofs$8651].
### Ad Example 1 

* Verifying the property (1) `$f(e_G)=e_H$`: 
   * The [neutral element][bookofproofs$661] of `$G=(\mathbb Z,+)$` is `$e_G=0$` and the same neutral element has `$H=(\{3n\mid n\in\mathbb Z\}, +)$`, i.e. `$e_H=0$`. Thus `$$f(0)=3\cdot 0=0.$$`
* Verifying the property (2) `$f(x^{-1})=f(x)^{-1}$` for all `$x\in G$`:
   * Let `$x\in(\mathbb Z,+)$`. Then `$x^{-1}=-x.$`
   * Then `$f(-x)=3\cdot(-x)=-3x$` which is the inverse element of `$3x\in (\{3n\mid n\in\mathbb Z\},+).$` 

### Ad Example 2

* Verifying the property (1) `$f(e_G)=e_H$`: 
   * The [neutral element][bookofproofs$661] of `$G=(\mathbb R,+)$` is `$e_G=0$` and the neutral element of `$H=(\mathbb R^{ +}, \cdot)$` is `$e_H=1$`. We verify by [exponential function zero][bookofproofs$1423] `$$\exp(0)=1.$$`
* Verifying the property (2) `$f(x^{-1})=f(x)^{-1}$` for all `$x\in G$`:
   * Let `$x\in(\mathbb R,+)$`. Then `$x^{-1}=-x.$` We verify by the [reciprocity law for the exponential function][bookofproofs$1417].
`$$\exp(-x)=\frac{1}{\exp(x)},$$` which is the inverse element of `$\exp(x)\in (\mathbb R^{ +},\cdot).$` 

### Ad Example 3

* Verifying the property (1) `$f(e_G)=e_H$`: 
   * The [neutral element][bookofproofs$661] of `$G=(\mathbb R,+)$` is `$e_G=0$` and the neutral element of `$H=(\operatorname{GL}(2,\mathbb R),\cdot)$` is `$$e_H=\pmatrix{1&0\\0&1}.$$` We verify for the in the example defined group homomorphism `$$\rho(0)=\pmatrix{\cos(0)&-\sin(0)\\\sin(0)&\cos(0)}=\pmatrix{1&0\\0&1}.$$`
* Verifying the property (2) `$f(x^{ -1})=f(x)^{ -1}$` for all `$x\in G$`:
   * Let `$x\in(\mathbb R,+)$`. Then `$x^{ -1}=-x.$` We verify by the [eveness of cosine][bookofproofs$1790] and the [oddness of sine][bookofproofs$1792].
`$$\rho(-x)=\pmatrix{\cos( -x)&-\sin( -x)\\\sin( -x)&\cos( -x)}=\pmatrix{\cos(-x)&\sin(x)\\-\sin(x)&\cos(x)},$$` which is the inverse element of `$H.$` This can be verified by the [Pythagorean identity][bookofproofs$1794] `$$\pmatrix{\cos(x)&-\sin(x)\\\sin(x)&\cos(x)}\cdot \pmatrix{\cos(x)&\sin(x)\\-\sin(x)&\cos(x)}=\pmatrix{1&0\\0&1}.$$`
