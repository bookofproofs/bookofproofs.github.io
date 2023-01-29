layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6397
orderid: 50
parentid: bookofproofs$6396
title: 
description:  Proof of BICONNECTIVITY IS A NECESSARY CONDITION FOR A HAMILTONIAN GRAPH &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: biconnectivity,condition,graph,hamiltonian,necessary,proof
contributors: bookofproofs

---


---

Let `\(G(V,E)\)` be a [simple graph][bookofproofs$523] `\(G(V,E)\)`.

* It is obvious, that if `\(G\)` is disconnected, then it is not [Hamiltonian][bookofproofs$6349], because it otherwise does not contain a [Hamiltonian cycle][bookofproofs$330].
* If `\(G\)` is only [connected][bookofproofs$1166], but not at least [biconnected][bookofproofs$1227], then it contains by definition [cutvertices][bookofproofs$1166]. 
* In this case, it cannot contain a [Hamiltonian cycle][bookofproofs$330]. Otherwise, every [closed walk][bookofproofs$1165], which contains every vertex of `\(G\)`, passes a cutvertex at least twice.
* By [contraposition][bookofproofs$1330], if `\(G\)` is [Hamiltonian][bookofproofs$6349], then it must be at least [biconnected][bookofproofs$1227].
