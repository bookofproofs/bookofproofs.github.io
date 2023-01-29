layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8474
orderid: 50
parentid: bookofproofs$8473
title: 
description: PROOF OF A NECESSARY CONDITION FOR A GRAPH WITH SHORTEST CYCLES TO BE PLANAR II ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: necessary condition for planar graphs with shortest cycles,proof
contributors: bookofproofs

---


---

* By hypothesis, `$k\ge 3$` is a [positive integer][bookofproofs$1075] and `$G(V,E)$` is a [simple][bookofproofs$523], [biconnected][bookofproofs$1227], [planar graph][bookofproofs$1226] with `$|E|$` edges and `$|V|$` vertices and shortest [cycle][bookofproofs$1165] length `$k.$` 
* By a [necessary condition for `$G$` to be planar][bookofproofs$8471], `$$\begin{align}|E|\le\frac{k}{k-2}(|V|-2).\tag{*}\label{E21118a}\end{align}$$`
* Suppose, the [degree][bookofproofs$362] of each [vertex][bookofproofs$523] of `$G$` is `$\ge k+3.$`
   * With the [handshaking lemma for graphs][bookofproofs$1173], it follows `$2|E|=\sum_{v\in V}\deg(v)\ge|V|\cdot (k+3),$` or 
`$$\begin{align}|E|\ge|V|\frac{k+3}{2}.\tag{**}\label{E21118b}\end{align}$$`
   * Combining `$(\ref{E21118a})$` and `$(\ref{E21118b}),$` we obtain `$$|V|\frac{k+3}2\le |E|\le \frac{k}{k-2}(|V|-2).$$` 
   * This is equivalent to `$$|V|(k^2+k-6)\le 2k|V|-4k.$$`
   * Since `$k\ge 3,$` we get for `$k=3$`: `$6|V|\le 6|V|-12$` which is false.
* [By contradiction][bookofproofs$744], `$G$` contains a vertex `$v$` of degree `$\deg(v)\le k+2.$`
