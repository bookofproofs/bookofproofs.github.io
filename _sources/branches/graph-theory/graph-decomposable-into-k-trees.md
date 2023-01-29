layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$6392
orderid: 500
parentid: bookofproofs$96
title: Graph Decomposable Into `\(k\)` Trees
description: GRAPH DECOMPOSABLE INTO K TREES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1591
keywords: decomposable,graph,into,trees
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be a [finite][bookofproofs$6354] [undirected graph][bookofproofs$523] `\(G\)` is said to be *decomposable into `\(k\)` trees*, if there exist `\(k\)` [subsets][bookofproofs$552] of vertices `\(V_1,\ldots,V_k\)` with the following properties:

* The [subgraphs induced][bookofproofs$390] by the vertices `\(V_i\)`, i.e. the graphs `\(G[V_i]\)`, are all [trees][bookofproofs$96].
* The `\(V_i\)` [partition][bookofproofs$7991] the vertices of `\(G\)`, i.e.  
   * `\(V=V_1\cup\ldots\cup V_k\)`
   * `\(V_i\cap V_j=\emptyset\)` for `\(i=1,\ldots,k\)`, `\(j=1,\ldots,k\)`,  `\(i\neq j\)`,  and
   * `\(V_i\neq\emptyset\)` for `\(i=1,\ldots,k\)`.

A given partition `\(V_1,\ldots,V_k\)` with these properties is called a *tree decomposition of order `\(k\)`*. Please note that a graph can have different tree decompositions of the same order.
