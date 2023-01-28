layout: example
categories: branches,algebra
nodeid: bookofproofs$8653
orderid: 400
parentid: bookofproofs$679
title: Examples of Kernels and Images of Group Homomorphisms
description: EXAMPLES OF KERNELS AND IMAGES OF GROUP HOMOMORPHISMS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$677
keywords: examples of kernels and images of group homomorphisms
contributors: bookofproofs

---


---

We will now build the respective [group homomorphisms][bookofproofs$680] for the [examples given for group homomorphisms][bookofproofs$8651]

### Ad Example 1 

* Kernel `$\operatorname{ker}(f):= \{g\in G\mid f(g)=e_H\}$`:
   * The [neutral element][bookofproofs$661] of `$H=(\{3n\mid n\in\mathbb Z\}, +)$` is `$e_H=0$`. The only element of `$x\in G=(\mathbb Z, +)$` for which `$f(x)=3x=0$` is `$x=0.$` Thus `$\{0\}$` is the kernel of `$f.$` 
* Image `$\operatorname{im}(f):=f[G]=\{f(g)\in H\mid g\in G\}$`: 
   * The image `$f[G]=\{3x\mid x\in\mathbb Z\}$` are all [multiples][bookofproofs$700] of `$3$`, i.e. `$f[G]=H.$`

### Ad Example 2

* Kernel `$\operatorname{ker}(f):= \{g\in G\mid f(g)=e_H\}$`:
   * The [neutral element][bookofproofs$661] of `$H=(\mathbb R^*, \cdot)$` is `$e_H=1$`. The only element of `$x\in G=(\mathbb R,+)$` for which `$\exp(x)=1$` is `$x=0.$` Thus `$\{0\}$` is the kernel of `$\exp.$` 
* Image `$\operatorname{im}(\exp):=f[G]=\{f(g)\in H\mid g\in G\}$`: 
   * The image `$\exp[\mathbb R]=\mathbb R^+$` are all [positive real numbers][bookofproofs$1107], i.e. `$\exp[\mathbb R]=\mathbb R^+.$`

### Ad Example 3

* Kernel `$\operatorname{ker}(f):= \{g\in G\mid f(g)=e_H\}$`:
   * The [neutral element][bookofproofs$661] of `$H$` is `$$e_H=\pmatrix{1&0\\0&1}.$$` The elements of `$x\in (\mathbb R,+)$` for which `$\rho(x)=e_H$` are all integer multiples of `$2\pi k,$` `$k\in\mathbb Z.$` This follows from [special values of cosine and sine][bookofproofs$6739] and their [periodicity][bookofproofs$6740] Thus `$\{2\pi k\mid k\in\mathbb Z\}$` is the kernel of `$\rho.$` 
* Image `$\operatorname{im}(\exp):=f[G]=\{f(g)\in H\mid g\in G\}$`: 
   * The image `$\rho[\mathbb R]=\mathbb R^+$` are all matrices of `$H=(\operatorname{GL}(2,\mathbb R),\cdot).$`
