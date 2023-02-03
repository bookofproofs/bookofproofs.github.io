layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1235
orderid: 1200
parentid: bookofproofs$178
title: Interlacing Pieces with Respect to a Cycle, Interlacement Graph
description: INTERLACING PIECES WITH RESPECT TO A CYCLE, INTERLACEMENT GRAPH &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1228
keywords: cycle,exterior,graph,interior,interlacement,interlacement graph,interlacing,pieces,respect
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be an [biconnected graph][bookofproofs$1227] and let `\(C(V_c,E_c)\)` be a [cycle][bookofproofs$1165] in `\(G\)`[^1], such that the cycle `\(C\)` (but not necessarily the whole graph `\(G\)`) has[^2] a [planar drawing][bookofproofs$1212] so that the planar drawing of `\(C\)` divides the plane into an **interior** region bounded by the drawing and an **exterior** region[^3].  

### Example

In the following figure a drawing of a graph `\(G\)` is shown, which is not planar, however, the cycle `\(C\)` (blue) has a planar drawing:


![pieces6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces6.jpg?raw=true)


We say that two [pieces of `\(G\)` with respect to `\(C\)` ][bookofproofs$1231] **interlace**, if they can neither be drawn entirely in the interior of `\(C\)` nor can they be drawn entirely in the exterior of `\(C\)`, without violating planarity. 

In our example, there are `\(6\)` pieces of `\(G\)` with respect to `\(C\)`. In particular, the pieces `\(P_2\)` and `\(P_1\)` interlace, while the  the pieces `\(P_2\)` and `\(P_3\)` do not interlace: 
  

![pieces](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces.jpg?raw=true)


The **interlacement graph** `\(I(V_i,E_i)\)` of the pieces of `\(G\)` with respect to `\(C\)` is the graph whose vertices `\(V_i\)` are the pieces of `\(G\)` and whose edges `\(E_i\)` are the pairs of pieces that interlace. 

The following figure demonstrates the interlacement graph of our example:


![interlacementgraph](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/interlacementgraph.jpg?raw=true) 


[^1]: Please note that in a biconnected graph such a cycle always exists.

[^2]: Please note that every cycle has a planar drawing. The condition requiring `\(C\)` to have a planar drawing is made in this definition only for the reason to make sure that an interior and exterior of the drawing of `\(C\)` exists.

[^3]: The existence of an interior and an exterior region follows from the Jordan Curve Theorem (still to be done at <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong>).
