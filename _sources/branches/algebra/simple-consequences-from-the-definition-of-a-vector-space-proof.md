layout: proof
categories: branches,algebra
nodeid: bookofproofs$7979
orderid: 50
parentid: bookofproofs$7978
title: 
description: Proof of SIMPLE CONSEQUENCES FROM THE DEFINITION OF A VECTOR SPACE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$7937
keywords: consequences,definition,general associative law,general commutative law,simple,space,vector,proof
contributors: bookofproofs

---


---

Let `$V$` be a [vector space][bookofproofs$560] over the [field][bookofproofs$557] `$F.$` Since, by definition, all vectors `$x\in V$` form an [Abelian group][bookofproofs$553], the statements 1 to 8 follow immediately as a [corollary from the group axioms][bookofproofs$555]. The statements 9 to 12 remain to be shown.

### Ad 9)

* Since `$-1=1\cdot (-1)$` in the field `$F$`, the [axioms of scalar multiplication][bookofproofs$560] show that `$-1x=(1\cdot (-1))x=1\cdot ((-1)x)).$`
* Since by these axioms, `$1$` is the neutral element of the scalar multiplication in `$V$`, it follows that `$-1x=(-1)x.$`

### Ad 10)

* Since `$0=1+(-1)$` in the field `$F$`, the axioms of scalar multiplication demonstrate that `$0x=(1+(-1))x=x+(-x)=o,$` in which we have used the rules no. 2 and no. 9.

### Ad 11)

* By no.2 we have `$x+(-x)=o$` for all vectors `$x\in V.$`
* Thus, by the axioms of scalar multiplication we have `$\lambda o=\lambda(x+(-x))=\lambda x + (-\lambda x)=o$` for all `$\lambda\in F.$`

### Ad 12)

* No. 10 and/or no. 11 imply `$\lambda x=o.$`
* The converse remains to be shown, so assume `$\lambda x=o.$` 
* We want to show that then, at least one of `$\lambda$` or `$x$` must be zero.
   * Assume `$\lambda\neq 0.$` Then `$\lambda^{-1}\cdot\lambda=1.$` Thus, multiplying both sides of the above equation by `$\lambda^{-1}$` and applying the axioms of scalar multiplication as well as no. 11 we get `$$\begin{array}{rcl}\lambda^{-1}\cdot(\lambda x)&=&\lambda^{-1} o\\(\lambda^{-1}\cdot\lambda)x&=&o\\1x&=&o\\x&=&o.\end{array}$$`
   * Now, assume `$x\neq o.$` Note that `$\lambda x=o=\lambda (x+(-x))=\lambda x+(-\lambda x)=o+(-\lambda x)=-\lambda x.$`
   * Since `$\lambda x=-\lambda x$` and `$x\neq o$`, we must have `$\lambda=-\lambda$`, which is only true for `$\lambda=0.$`
