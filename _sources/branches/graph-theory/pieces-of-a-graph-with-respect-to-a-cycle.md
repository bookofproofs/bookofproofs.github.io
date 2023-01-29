layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1231
orderid: 1000
parentid: bookofproofs$178
title: Pieces of a Graph With Respect to A Cycle
description: PIECES OF A GRAPH WITH RESPECT TO A CYCLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1228
keywords: attachments,cycle,graph,pieces,respect
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be an [biconnected graph][bookofproofs$1227] and let `\(C(V_c,E_c)\)` be a [cycle][bookofproofs$1165] in `\(G\)`[^1]. The cycle `\(C\)`  partitions all edges `\(E\setminus E_c\)`, i.e. the edges, which are not in the cycle, into [equivalence classes][bookofproofs$7990] in the following way:

> Two edges `\(e_1,e_2\in E\setminus E_c\)` are equivalent if and only if there is a [path][bookofproofs$1164] `\(P(V_p,E_p)\)` between them that does not contain any vertex of `\(C\)`, formally
`\[\forall e_1,e_2\in E\setminus E_c:~e_1\equiv e_2\Longleftrightarrow\exists \text{ path }P:~e_1,e_2\in E_p\wedge V_p\cap V_c=\emptyset.\]`

The [subgraphs][bookofproofs$390] of `\(G\)` induced by these equivalence classes are called the *pieces of the graph `\(G\)` with respect to the cycle `\(C\)`*.

The vertices of a piece `\(P_i(V_i,E_i)\)` with respect to the cycle `\(C(V_c,E_c)\)` that are also in `\(C\)`, i.e. `\(v\in V_i\cap V_c\)`, are called the  **attachments** of that piece.

### Example

A graph (left-upper corner) with a cycle (blue) and the corresponding partition of this graph into `\(6\)` pieces `\(P_1,P_2,\ldots,P_6\)`. While `\(P_1,P_2,P_5,P_6\)` have two attachments, the pieces `\(P_3\)` and `\(P_4\)` have three attachments.


![pieces](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces.jpg?raw=true)


[^1]: Please note that in a biconnected graph such a cycle always exists.
