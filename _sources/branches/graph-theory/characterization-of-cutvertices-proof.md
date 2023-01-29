layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1239
orderid: 50
parentid: bookofproofs$1238
title: 
description: PROOF OF CHARACTERIZATION OF CUTVERTICES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1163
keywords: characterization,cutvertices,proof
contributors: bookofproofs

---


---

### "`\(\Rightarrow\)`" 

* Let `\(v\)` be a [cutvertex][bookofproofs$1166] in the connected graph `\(G(V,E,\gamma)\)`. 
* Since the subgraph `\(G[V\setminus v]\)` is disconnected, it is not empty and has at least two vertices `\(x,y\in V\)`, which are in different components of this graph left after the removal of the cutvertex `\(v\)`. 
* Moreover, every [path][bookofproofs$1164] between `\(x\)` and `\(y\)` must pass `\(v\)`. 
* For if a path between `\(x\)` and `\(y\)` existed, which does not pass `\(v\)`, the removal of the vertex `\(v\)` would not leave the graph `\(G\)` disconnected, in [contradiction][bookofproofs$744] to `\(v\)` being a cutvertex.

### "`\(\Leftarrow\)`" 

* Let `\(x,y,v\)` be different vertices of `\(G\)` such that every path between `\(x\)` and `\(y\)` passes `\(v\)`. 
* Then the removal of `\(v\)` cuts all these passes and there is no path between `\(x\)` and `\(y\)` in the graph  `\(G[V\setminus v]\)`. 
* Thus, `\(G[V\setminus v]\)` is disconnected and `\(v\)` is a cutvertex.
