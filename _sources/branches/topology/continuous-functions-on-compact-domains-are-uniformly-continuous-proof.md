layout: proof
categories: branches,topology
nodeid: bookofproofs$6615
orderid: 50
parentid: bookofproofs$6614
title: 
description:  Proof of CONTINUOUS FUNCTIONS ON COMPACT DOMAINS ARE UNIFORMLY CONTINUOUS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: are,compact,continuous,domains,functions,uniformly,proof
contributors: bookofproofs

---


---

* Let `$(X,d_X)$` and `$(Y,d_Y)$` be [metric spaces][bookofproofs$617].
* Let `\(X\)` be [compact][bookofproofs$6575].
* Let `\(f:X\mapsto Y\)` be a [continuous function][bookofproofs$1205].
* It is to be shown that `\(f:X\mapsto Y\)` is [uniformly continuous][bookofproofs$6612], i.e. for every `$\epsilon > 0$` there is a `$\delta > 0$` such that `$d_Y(f(x),f(y)) < \epsilon$` for all `$x,y\in X$` with `$d_X(x,y) < \delta.$`
   * Choose a fixed `$\epsilon > 0$`.
   * According to the [definition of continuity using open sets][bookofproofs$6195], `\(f\)` is [*continuous at a point `$x\in X$`*][bookofproofs$1205], if and only if for any [neighborhood][bookofproofs$849] `$V\subset Y$` of `$f(x)$` there exists a neighborhood `$U$` of `$x$` such that `$f(U)\subset V.$` In the following argument, for every `$x\in X$` we will choose `$V$` to be a neighborhood of `$f(x)$` with a [diameter][bookofproofs$6581] `$\operatorname{diam}(V) < \epsilon / 2$` and construct `$U$` to be an [open ball][bookofproofs$849] `$B(x, r(x))$` with an appropriate radius  `$r(x) > 0$` depending on `\(x\)` and  `$ \epsilon$`.
   * Since `$f$` is continuous at any point `$x\in X$`, for every `$x\in X$` there is a radius `$r(x) > 0$` such that `$$d_Y(f(x),f(y)) < \frac \epsilon2$$` for all `$$y\in B(x,r(x)).$$`
   * Note that `$$\bigcup_{x\in X} B\left(x,\frac {r(x)}2 \right)$$` is an [open cover][bookofproofs$150] of `$X$`.
   * Since `$X$` is [compact][bookofproofs$6575], there exist [finitely many][bookofproofs$985] `\(x_1,\ldots,x_n\in X\)` with `$$X\subset \bigcup_{k=1}^n B\left(x_k,\frac {r(x_k)}2 \right).$$`
   * Set the [minimum][bookofproofs$6603] `$\delta:=\frac 12\min(r(x_1),\ldots,r(x_n))$`.
   * For this `$\delta$`, we have that if we take `$x,y\in X$` with `$d_X(x,y) < \delta$`, we can find an index `$k\in \{1, \ldots,n\}$` with `$x,y\in B(x_k,r(x_k)/2)$`.
   * For these `\(x,y\in X\)` with `$d_X(x,y) < \delta$` we have that `$$d_Y(f(x),f(y))\le d_Y(f(x),f(x_k)) + d_Y(f(x_k),f(y))=\frac \epsilon2 + \frac \epsilon2 = \epsilon.$$`
