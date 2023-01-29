layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$569
orderid: 50
parentid: bookofproofs$568
title: 
description: PROOF OF EVEN NUMBER OF VERTICES WITH AN ODD DEGREE IN FINITE DIGRAPHS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$570
keywords: digraphs,finite,handshaking,lemma,handshaking lemma,handshake lemma,handshaking theorem,proof,proof
contributors: bookofproofs

---


---

* Let `\(D=(V,E,\alpha,\omega)\)` be a finite digraph and let `\(O\subseteq V\)` be the subset of all vertices with odd degree.
* Then it follows from the [handshaking lemma][bookofproofs$565] that `\[2|E|=\sum_{v\in V}d_D^+(v)+\sum_{v\in V}d_D^-(v)=\underbrace{\sum_{v\in V}d_D(v)}_{\text{even}}.\]`
* On the other hand, we have `\[\sum_{v\in V}d_D(v)= \underbrace{\sum_{v\in V\setminus O}d_D(v)}_{\text{even}}+\underbrace{\sum_{v\in O}(d_D(v)-1)}_{\text{even}}+|O|.\]`
* Thus, `\(|O|\)` must be even, since it is a difference of [even numbers][bookofproofs$8130].