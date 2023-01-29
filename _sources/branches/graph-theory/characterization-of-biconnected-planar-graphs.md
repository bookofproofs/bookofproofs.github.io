layout: theorem
categories: branches,graph-theory
nodeid: bookofproofs$1237
orderid: 1600
parentid: bookofproofs$178
title: Characterization of Biconnected Planar Graphs
description: CHARACTERIZATION OF BICONNECTED PLANAR GRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1228
keywords: biconnected,characterization,graphs,planar
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be a [biconnected graph][bookofproofs$1227] and let `\(C\)` be a [cycle][bookofproofs$1165] in `\(G\)`[^1]. `\(G\)` is [planar][bookofproofs$1226], if and only if the following (recursive) conditions hold:

> `\((1)\)` Every [piece `\(P\)` of `\(G\)` with respect to `\(C\)` ][bookofproofs$1231] is planar, and 

> `\((2)\)` the [interlacement graph][bookofproofs$1235] `\(I_C\)` of the pieces of `\(G\)` with respect to `\(C\)` is [bipartite][bookofproofs$1236].
### Example

In the left-upper corner of the following figure, a graph `\(G\)` with a cycle (blue) is shown. The pieces of `\(G\)` with respect to this cycle are shown in the middle of the figure (`\(P_1,P_2,\ldots,P_6\)`. The interlacement graph of these pieces (in the left-bottom corner) is bipartite. Since every piece of its own is planar, a planar drawing of `\(G\)` exists (shown on the right side of the figure):


![planarity1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/planarity1.jpg?raw=true)


In the following figure, the graph `\(G\)` has been slightly changed (see piece `\(P_2\)`). The resulting interlacement graph is not bipartite. Although all pieces, by themselves, are planar, the graph `\(G\)` as a whole, is not planar. On the right side of the figure, a drawing is shown, in which the pieces `\(P_2\)` and `\(P_5\)` cross each other. The theorem proves that there is no way to find a planar drawing of `\(G\)`.  


![planarity2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/planarity2.jpg?raw=true)



 
[^1]: Please note that in a biconnected graph such a cycle always exists.
