layout: definition
categories: branches,analysis
nodeid: bookofproofs$8382
orderid: 50
parentid: bookofproofs$8381
title: Pointwise and Uniformly Convergent Sequences of Functions
description: POINTWISE AND UNIFORMLY CONVERGENT SEQUENCES OF FUNCTIONS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: pointwise convergent,uniformly convergent,sequence of functions,pointwise convergent function,uniformly convergent function,pointwise convergent functions,uniformly convergent functions,uniform,pointwise,conveges uniformly,converges pointwise
contributors: bookofproofs

---


---

Let `$\mathbb F$` be a either the [field of real numbers][bookofproofs$1640] or the [field of complex numbers][bookofproofs$1690] and let `$D\subseteq \mathbb F$` be the [domain][bookofproofs$592] of infinitely many given functions `$f_n:D\to\mathbb F.$` The **sequence of functions** `$(f_n)_{n\in\mathbb N}$` is called:

* **pointwise convergent** to a function `$f:D\to\mathbb F,$` if for every `$x\in D$` the [real sequence][bookofproofs$875] (or the [complex sequence][bookofproofs$1249]) `$(f_n(x))_{n\in\mathbb N}$` is convergent[^1], i.e. for every `$x\in D$` and every `$\epsilon > 0$` there exists an index `$N\in\mathbb N$` such that `$$|f_n(x)-f(x)|<\epsilon\quad\forall n\ge N,$$`
* **uniformely convergent** to a function `$f:D\to\mathbb F,$` if the sequence `$(f_n)_{n\in\mathbb N}$` is pointwise convergent to `$f$` and for a given `$\epsilon > 0$` the index `$N$` does not depend on `$x.$` In other words, for every `$\epsilon > 0$` there exists an index `$N\in\mathbb N$` such that `$$|f_n(x)-f(x)|<\epsilon\quad\forall n\ge N,\quad\forall x\in D.$$`

[^1]: i.e. a [convergent real sequence][bookofproofs$175] (or (a [convergent complex sequence][bookofproofs$1700])
