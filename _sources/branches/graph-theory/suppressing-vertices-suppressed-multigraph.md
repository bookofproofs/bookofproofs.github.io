layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1169
orderid: 300
parentid: bookofproofs$328
title: Suppressing Vertices, Suppressed Multigraph
description: SUPPRESSING VERTICES, SUPPRESSED MULTIGRAPH &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1163
keywords: multigraph,suppressed,suppressing,suppressing vertices,vertices
contributors: bookofproofs

---


---

By **suppressing vertices** in an [undirected graph][bookofproofs$525] `\(G\)` we mean the deleting of each vertex `\(v\)` of [degree][bookofproofs$544] `\(d_G(v)=2\)` and adding an edge between its two neighbors. If the edges form a loop, we add no edge and obtain a graph without the vertex `\(v\)`.

Since the degrees of all vertices other than those with degree `\(d_G(v)=2\)` remain unchanged, no matter in which order those vertices are suppressed, the obtained multigraph is well-defined and called the *suppressed multigraph of `\(G\)`*, denoted by `\(\tilde G\)`. 

#### Example:

A multigraph `\(G\)` and its suppressed multigraph `\(\tilde G\)` - note that all blue vertices, which had degree `\(2\)` have been consecutively suppressed; independently of the order in which the vertices are suppressed, we always get the same suppressed multigraph:

![suppressing_vertex](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/suppressing_vertex.jpg?raw=true)

