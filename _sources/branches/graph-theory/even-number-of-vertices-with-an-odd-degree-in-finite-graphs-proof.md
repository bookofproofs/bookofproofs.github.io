layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1176
orderid: 50
parentid: bookofproofs$1175
title: 
description: Proof of EVEN NUMBER OF VERTICES WITH AN ODD DEGREE IN FINITE GRAPHS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$570
keywords: even number of vertices with an odd degree,proof
contributors: bookofproofs

---


---

* Let `\(G=(V,E,\gamma)\)` be a [finite graph][bookofproofs$6354] and let `\(O\subseteq V\)` be the subset of all vertices with odd degree. 
* Then `\(V\setminus O\)` is the subset of all vertices with [even][bookofproofs$8130] [degree][bookofproofs$362].
* According to the [handshaking lemma][bookofproofs$1173] we obtain `\(\sum_{v\in V}\deg_G(v)=2|E|.\)` 
* It follows `\[\sum_{v\in O}\deg_G(v)=2|E|-\sum_{v\in V\setminus O}\deg_G(v).\]`
* Because the right side of the equation is even, so must be the left side.
