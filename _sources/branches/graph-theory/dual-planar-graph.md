layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$6391
orderid: 600
parentid: bookofproofs$178
title: Dual Planar Graph
description: DUAL PLANAR GRAPH ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$566
keywords: dual,dual graph,graph,planar,dual planar graph,dual of planar graph,dual of a planar graph,dual graphs,dual graph definition,dual graph example,dual of a graph,graph dual,dual of graph,planar dual,dual graph in graph theory,what is a dual graph,graph duality,planar graph,what is dual graph
contributors: bookofproofs

---


---

Given a [planar][bookofproofs$1212] [undirected graph][bookofproofs$523] `\(G(V,E,\gamma)\)`, let `\(F\)` denote the [set][bookofproofs$550] of all the [faces][bookofproofs$6373] of `\(G\)` in a particular given [planar drawing][bookofproofs$1212] `\(\mathcal D\)` of `\(G\)`. 

A **dual graph** `\(G^\ast_{\mathcal D}(V^\ast,E^\ast,\gamma^\ast)\)` is constructed as follows:

* Draw one new vertex in each face of the planar drawing: these are the vertices `\(V^\ast\)`, of `\(G^\ast_{\mathcal D}\)`. Thus, there are the same number of vertices in `\(G^\ast_{\mathcal D}\)`, as there are faces in the planar drawing of `\(G\)`, formally `\(|F|=|V^\ast|\)`.
* For each edge `\(e\)` of the plane drawing, draw a new line joining the vertices of `\(G^\ast_{\mathcal D}\)` in the faces on either side of `\(e\)`: these lines are the edges of `\(G^\ast_{\mathcal D}\)`. Thus, there are the same number of edges in `\(G^\ast_{\mathcal D}\)`, as there are edges in the planar drawing of `\(G\)`, formally `\(|E|=|E^\ast|\)` and this defines the function `\(\gamma^\ast\)`.

The index "`\(\mathcal D\)`" in the notation "`\(G^\ast_{\mathcal D}\)`" is used to indicate that the dual graph depends on a particular planar drawing of `\(G\)`.

### Example

The following figure shows a planar drawing of a graph (with orange vertices, labeled with numbers and with solid edges) and its dual graph (with blue vertices, labeled with letters and with dashed edges).


![dual](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dual.png?raw=true)

(c) bookofproofs

### Notes and Observations

* A dual graph is defined for planar graphs, which do not necessarily have to be simple graphs, i.e. the original graph can contain loops and multiple edges.
* Loops or multiple edges in the original graphs transform into edges in the dual graph and vice versa. Thus, both graphs have exactly the same number of edges.
* The dual depends on the particular planar drawing. E.g. The following two figures show different planar drawings of the same graph (orange vertices) with different planar drawings resulting in different (i.e. not isomorphic) dual graphs:


![dual1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dual1.png?raw=true)

(c) bookofproofs


![dual2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dual2.png?raw=true)

(c) bookofproofs
