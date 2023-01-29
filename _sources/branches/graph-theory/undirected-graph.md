layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$523
orderid: 50
parentid: bookofproofs$97
title: Undirected Graph, Vertices, Edges, Simple Graph
description: UNDIRECTED GRAPH, VERTICES, EDGES, SIMPLE GRAPH ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$570
keywords: edges,graph,loop,multiple loops,nodes,undirected,undirected graph,vertices,graphs,parallel edges,ends,multiple loop,simple graph,simple graphs,simple undirected graph,vertices definition,multigraph,multiple edges,loops,edge,undirect graph,simple undirected graph definition,definition of undirected graph,definition of simple graph
contributors: bookofproofs

---


---

An **undirected graph** or **graph** `\(G\)` is a triple `\(G:=(V,E,\gamma)\)` with the following properties:

1. `\(V\)` is a non-empty [set][bookofproofs$550] of elements called **vertices** or **nodes**.
1. `\(E\)` is a set (non-empty or empty) of elements, called **edges**.
1. Vertices and edges are not the same objects, formally `\(V\cap E=\emptyset\)`. 
1. The [map][bookofproofs$592] `\(\gamma: E\mapsto \{X:~X\subseteq V,~1\le|X|\le 2\}\)`, assigns to every edge `\(e\)` its **ends**, denoted by `\(\gamma(e)\)`. 

Please note that the ends of an edge `\(e\)` can be two different vertices (this is the case if `\(|\gamma(e)|=2\)`) or one an the same vertex (this is the case if `\(|\gamma(e)|=1\)`).

If `\(|\gamma(e)|=1\)`, i.e. if the ends of `\(e\)` are the same vertex, the edge `\(e\)` is called a **loop**. 

Two edges `\(e\)` and `\(e'\)` are called **parallel** or **multiple edges** if `\(\gamma(e)=\gamma(e')\)`, (thus they have the same ends). If additionally `\(|\gamma(e)|=1\)`, they are called **multiple loops**.

We call `\(G\)` a **simple undirected graph** (or **simple graph**), if it has no loops and no parallel edges. A simple graph is written `\(G(V,E)\)`. An edge of simple graph `\(e:=(x,y)\)` is written as `\(xy\)` (or `\(yx\)`).

#### Example graph:


![graph3_1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graph3_1.jpg?raw=true)

