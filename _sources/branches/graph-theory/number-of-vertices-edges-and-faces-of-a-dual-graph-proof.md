layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8478
orderid: 50
parentid: bookofproofs$8477
title: 
description: PROOF OF NUMBER OF VERTICES, EDGES, AND FACES OF A DUAL GRAPH &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$566
keywords: number of vertices, edges, and faces in a dual graph,proof
contributors: bookofproofs

---


---

* By hypothesis, `$G$` is a [connected][bookofproofs$1166] [planar graph][bookofproofs$1226] with a [planar drawing][bookofproofs$1212] `$\mathcal D,$` and with `$|V|$` [vertices][bookofproofs$523], `$|E|$` [edges][bookofproofs$523] and `$|F|$` [faces][bookofproofs$6373].
* It follows from the construction of the [dual graph][bookofproofs$6391] `$G^*_{\mathcal D}$` that `$G^*_{\mathcal D}$` has `$|F|$` vertices and `$|E|$` edges and that it is a [planar graph][bookofproofs$1226].
* From the [Euler's formula for planar graphs][bookofproofs$6374] he have:
   * For `$G$`: `$|V|-|E|+|F|=2.$`
   * For `$G^*_{\mathcal D}$`: `$|F|-|E|+f=2,$` where `$f$` is the (unknown) number of face of `$G^*_{\mathcal D}.$`
* Comparing both equations, we get `$f=|V|.$`
