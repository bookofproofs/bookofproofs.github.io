layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6383
orderid: 50
parentid: bookofproofs$6382
title: 
description: PROOF OF SPLITTING A GRAPH WITH EVEN DEGREE VERTICES INTO CYCLES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$566
keywords: cycles,degree,even,graph,into,splitting,vertices,proof
contributors: bookofproofs

---


---

* By hypothesis, `\(G(V,E)\)` is a [simple graph][bookofproofs$523] in which each vertex has [even][bookofproofs$8130] [degree][bookofproofs$362].
* Obtain a fist [cycle][bookofproofs$1165] as follows:
   * Denote `\(G(V,E)\)` by `\(G_1(V,E_1)\)`.
   * Start at any vertex `\(v\)` and traverse edges in an arbitrary manner, never repeating an edge. This is possible since the even degree of each vertex ensures that whenever we enter a vertex, we must be able to leave it via a different edge.
   * Since `\(|V|\)` is finite, we must eventually reach a vertex `\(v\)` that we have visited before. 
   * The edges of the trail between the two occurrences of the vertex `\(v\)` must, therefore, form a cycle `\(C_1\)`.
* Now remove from `\(E_1\)` the edges of `\(C_1\)`, i.e. this leaves a graph `\(G_2(V,E_2)\)` with `\(E_2:=E_1\setminus E(C_1)\)`.
* Claim: If `\(G_2\)` has any edges left, each vertex in `\(G_2\)` has still an even degree, since:
   * We have removed exactly `\(2\)` edges from each vertex contained in `\(C_1\)`: one via which we have visited it, and one via which we left it.
   * Therefore, the even degree each vertex contained in `\(C_1\)` remains even in `\(G_2\)`, since it was also even in `\(G_1\)`.
* If `\(G_2\)` as any edges left, we can repeat the procedure above to find a cycle `\(C_2\)` in `\(G_2\)` with no edges in common with `\(C_1\)`.
* This leaves a graph `\(G_3(V,E_3)\)` with `\(E_3:=E_2\setminus E(C_2)\)`.
* Continue in this way until there are no edges left, at which stage the constructed cycles `\(C_1, C_2, C_3,\ldots\)` together include every edge of `\(G\)`, and no two of which have any edges in common.
