layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8468
orderid: 50
parentid: bookofproofs$8467
title: 
description: PROOF OF A NECESSARY CONDITION FOR A GRAPH TO BE PLANAR &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$566
keywords: necessary condition for a graph to be planar,necessary condition for planarity,necessary conditions for planarity,proof
contributors: bookofproofs

---


---

* By hypothesis, `$G(V,E)$` is a [simple][bookofproofs$523],  [biconnected][bookofproofs$1227], and [planar graph][bookofproofs$1226].
* Let `$\mathcal D$` be a [planar drawing][bookofproofs$1212] of `$G$`.
* Let `$|F|$` be the number of faces in the drawing `$\mathcal D.$`
* Since a simple graph has no [loops][bookofproofs$523] or [multiple edges][bookofproofs$523], each [face][bookofproofs$6373] in `$\mathcal D$` has a [face degree][bookofproofs$8464] of at least `$3.$`
* It follows from the [handshaking lemma for planar graphs][bookofproofs$8465] that `$3|F|\le 2|E|.$`
* Using the [Euler's formula for planar graphs][bookofproofs$6374], we have `$|F|=|E|-|V|+2.$`
* It follows `$3|E|-3|V|+6\le 2|E|,$` which is equivalent to `$|E|\le 3|V|-6.$`
