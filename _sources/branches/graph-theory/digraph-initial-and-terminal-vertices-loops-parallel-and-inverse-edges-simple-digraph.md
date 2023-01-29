layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$524
orderid: 50
parentid: bookofproofs$240
title: Digraph, Initial and Terminal Vertices, Loops, Parallel and Inverse Edges, Simple Digraph
description: DIGRAPH, INITIAL AND TERMINAL VERTICES, LOOPS, PARALLEL AND INVERSE EDGES, SIMPLE DIGRAPH &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$570
keywords: arcs,digraph,directed graph,edges,initial,inverse,loop,loops,nodes,parallel,simple,simple digraph,terminal,vertices,parallel edges examples,terminal vertex,parallel edges definition,terminal vertices,vertices definition,initial vertex and terminal vertex,terminal vertex meaning,parallel edges,initial vertex
contributors: bookofproofs

---


---

A **digraph** or **directed graph** `\(D\)` is a quadruple `\(D:=(V,E,\alpha,\omega)\)` with the following properties:

1. `\(V\)` is a non-empty [set][bookofproofs$550] of elements called **vertices** or **nodes**.
1. `\(E\)` is a set (non-empty or empty) of elements, called **edges** or **arcs**.
1. Vertices and edges are not the same objects, formally `\(V\cap E=\emptyset\)`. 
1. The [map][bookofproofs$592] `\(\alpha: E\mapsto V\)`, assigns to every edge `\(e\)` its **initial vertex**, denoted by `\(\alpha(e)\)`. 
1. The map `\(\omega: E\mapsto V\)` assigns to every edge `\(e\)` its **terminal vertex**, denoted by `\(\omega(e)\)`.



If `\(\alpha(e)=\omega(e)\)`, the edge `\(e\)` is called a **loop**. 

Two edges `\(e\)` and `\(e'\)` are called **parallel** or **multiple edges** if `\(\alpha(e)=\alpha(e')\)` and `\(\omega(e)=\omega(e')\)`, (thus they have the same initial and terminal vertices).

Two edges `\(e\)` and `\(e'\)` are called **inverse** if `\(\alpha(e)=\omega(e')\)` and `\(\omega(e)=\alpha(e')\)`, (thus the intial vertex of the first edge is the terminal vertex of the second edge and vice versa). 

We call `\(D\)` a **simple digraph** if it has no loops and no parallel edges.

#### Example digraph:


![graphs3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs3.jpg?raw=true)

