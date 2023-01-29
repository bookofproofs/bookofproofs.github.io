layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6384
orderid: 50
parentid: bookofproofs$6381
title: 
description:  Proof of CHARACTERIZATION OF EULERIAN GRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566
keywords: characterization,eulerian,graphs,eulerian graphs,characterization of eulerian graphs,eulerian graph,proof
contributors: bookofproofs

---


---

### "`\(\Rightarrow\)`"

* Assume, a [simple graph][bookofproofs$523] `\(G(V,E)\)` is [Eulerian][bookofproofs$6348].
* Then there is an [Eulerian tour][bookofproofs$391].
* Whenever this trail passes through a vertex, there is a contribution of `\(2\)` to the [degree][bookofproofs$362] of that vertex. 
* Since each edge is used exactly once, the degree of each vertex is [even][bookofproofs$8130].
* In particular, `\(G\)` is [connected][bookofproofs$1166], since every vertex is connected to any other by a [path][bookofproofs$1164].
### "`\(\Leftarrow\)`"

* Assume, `\(G\)` is [connected][bookofproofs$1166], and every one of its vertices has an even degree.
* We know from the [lemma about splitting a graph with even degree vertices into cycles][bookofproofs$6382] that `\(G\)` can be split into [cycles][bookofproofs$1165] `\(C_1, C_2, C_3,\ldots\)`, no two of which have an edge in common.
* Fit these cycles to make an [Eulerian tour][bookofproofs$391] as follows:
   * Start at any vertex of `\(C_1\)` and travel round `\(C_1\)` until we meet a vertex of another cycle. Without any loss of generality, let it be `\(C_2\)` (otherwise re-label the cycles obtained in the order provided by the above lemma). 
   * Travel the edges of `\(C_2\)`, and then resume traveling round `\(C_1\)`.
   * This gives a [closed trail][bookofproofs$1165] that includes `\(C_1\)` and `\(C_2\)`.
* If this trail includes all the edges of `\(G\)`, then we have found the required Eulerian tour. 
* Otherwise, travel around our new closed trail, and add a new cycle, say `\(C_3\)`.
* Continue this process, until you have traversed enough cycles to include all the edges of `\(G\)`. At the worst case, we will need all the cycles constructed in the above lemma.
* It follows that `\(G\)` is [Eulerian][bookofproofs$6348].