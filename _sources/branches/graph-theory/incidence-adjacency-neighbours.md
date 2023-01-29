layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$525
orderid: 400
parentid: bookofproofs$97
title: Incidence, Adjacency, Neighbours
description: INCIDENCE, ADJACENCY, NEIGHBOURS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: adjacency,edges incident to v,incidence,neighbors of v,neighbours
contributors: bookofproofs


---


---

Let `\(G=(V,E,\gamma)\)` be an [undirected graph][bookofproofs$523].
A vertex `\(v\in V\)` and an edge `\(e\in E\)` are called **incident** if `\(v\in\gamma(e)\)`.

Two different edges `\(e,e'\in E\)` are called **adjacent**, if there is at least one vertex incident with these edges, formally `\( e\neq e'\)` and `\(\exists v:~ v\in \gamma(e) \cap \gamma(e') \)`. 

Two different vertices `\(v,v'\in V\)` are **neighbours** or are called **adjacent**, if there is at at least one edge incident with these vertices, formally `\( v\neq v'\)` and `\(\exists e:~v,v'\in \gamma(e) \)`. 

Let `\(v\in V\)` be a vertex of `\(G\)`. (Note: In the following definitions, the index `\(D\)` can be omitted in the notation, if it is clear from the context, which digraph `\(G\)` is concerned).

The set `\(\delta_G(v):=\{e\in E: v\in \gamma(e)\}\)` is called **edges incident to v**.

The set `\(N_G(v):=\{x\in V: x\in \delta_G(v)\}\)` is called **neighbors of v**. 

### Example:


![graphs6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs6.jpg?raw=true)


The values of the degrees of vertices in the above graph are:

Vertex `\(v\)`  | Neighbours `\(N(v)\)`
:------------- |:-------------
 `\(a\)`| `\(\{b,c,d\}\)`
 `\(b\)`| `\(\{a,c\}\)`
 `\(c\)`| `\(\{a,b\}\)`
 `\(d\)`| `\(\{a,e\}\)`
 `\(e\)`| `\(\{d,e\}\)`
 `\(f\)`| `\(\emptyset\)`
