layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8472
orderid: 50
parentid: bookofproofs$8471
title: 
description: PROOF OF A NECESSARY CONDITION FOR A GRAPH WITH SHORTEST CYCLES TO BE PLANAR ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: necessary condition for a graph with shortest cycles to be planar,proof
contributors: bookofproofs

---


---

* By hypothesis, `$k\ge 3$` is a [positive integer][bookofproofs$1075], and `$G(V,E)$` is a [simple][bookofproofs$523], [biconnected][bookofproofs$1227], [planar graph][bookofproofs$1226] with shortest [cycle][bookofproofs$1165] length `$k.$`
* Let `$\mathcal D$` be a [planar drawing][bookofproofs$1212] of `$G.$`
* Since all cycles in `$G$` have the length of at least `$k,$` all faces in the planar drawing `$\mathcal D$` have a [face degree][bookofproofs$8464] of at least `$k.$`
* It follows from the [handshaking lemma for planar graphs][bookofproofs$8465] that `$k|F|\le 2|E|.$`
* Using the [Euler's formula for planar graphs][bookofproofs$6374], we have `$|F|=|E|-|V|+2.$`
* It follows `$k|E|-k|V|+2k\le 2|E|,$` which is equivalent to `$|E|\le \frac{k}{k-2}(|V|-2).$`
