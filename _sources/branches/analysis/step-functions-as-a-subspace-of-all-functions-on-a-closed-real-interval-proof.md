layout: proof
categories: branches,analysis
nodeid: bookofproofs$2925
orderid: 50
parentid: bookofproofs$6796
title: 
description: Proof of STEP FUNCTIONS AS A SUBSPACE OF ALL FUNCTIONS ON A CLOSED REAL INTERVAL ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: step functions,subspace,proof
contributors: bookofproofs

---


---

According to the [definition of a subspace][bookofproofs$562], we have to verify the following properties:
#1 `$0\in T[a,b].$` 
* Obviously, the [constant function][bookofproofs$1371] defined by `$f(x)=0$` for all `$x\in[a,b]$` is [step function][bookofproofs$1751].
* Thus, it is an element of `$T[a,b].$`

#2 If `$\phi,\psi\in T[a,b]$` then `$\phi+\psi\in T[a,b].$`
* Let `$\phi$` be a [step function][bookofproofs$1751] defined with respect to the partition `$$a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b$$` and let `$\psi$` be a step function defined with respect to the partition `$$a=y_0 < y_1 < \ldots < y_{m-1} < y_m=b.$$`
* We define the [set union][bookofproofs$6827] of both partions:
`$$\{t_0,t_1\ldots t_k\}:=\{x_0, x_1, \ldots, x_n\}\cup\{y_0, y_1, \ldots, y_m\},$$`
and observe that `$\phi$` and `$\psi$` are both constant functions on every [real interval][bookofproofs$1153] `$]t_{i-1},t_{i}[$`, `$i=1,\ldots,k.$`
* Thus, `$\phi+\psi$` is a step function and therefore `$\phi+\psi\in T[a,b].$`

#3 If `$\phi\in T[a,b]$` and `$\lambda\in\mathbb R$` then `$\lambda\phi\in T[a,b].$`
* Obviously, if `$\phi$` is a step function, so is `$\lambda\phi.$`
