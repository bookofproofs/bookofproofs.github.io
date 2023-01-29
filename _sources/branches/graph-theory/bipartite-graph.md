layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1236
orderid: 50
parentid: bookofproofs$239
title: Bipartite Graph
description: BIPARTITE GRAPH &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$570
keywords: bipartite,graph
contributors: bookofproofs

---


---

A [digraph][bookofproofs$524] `\(D(V,E,\alpha,\omega)\)` or an  [undirected graph][bookofproofs$523] `\(G(V,E,\gamma)\)` is called **bipartite**, if its vertices can be split into two subsets `\(A\)` and `\(B\)` in such a way that each edge of the graph joins a vertex in `\(A\)` and a vertex in `\(B\)`. Formally, if there is a [partition][bookofproofs$7991] of vertices `\(V=A\cup B,~ A\cap B=\emptyset\)` with 

* Either `\(\alpha(e)\in A \wedge \omega(e)\in B)\)` or `\(\alpha(e)\in B \wedge \omega(e)\in A\)`  for all `\(e\in E\)` in a digraph `\(D(V,E,\alpha,\omega)\)`.
* `\(\gamma(e)=X\)` with some pairs of vertices `\(X=\{x,y\}\)` such that either  `\(x\in A, y\in B\)`  or `\(x\in B, y\in A\)` for all `\(e\in E\)` in a graph `\(G(V,E,\gamma)\)`.

In particular, a bipartite graph has no loops.

### Example

The following figure shows a bipartite digraph. The vertices of one partition `\(A\)` are colored blue, while the vertices of the other partition `\(B\)` are colored orange. Please note that there are only edges between vertices with alternating colors. In particular, there are no loops:


![bipartite](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/bipartite.jpg?raw=true)

