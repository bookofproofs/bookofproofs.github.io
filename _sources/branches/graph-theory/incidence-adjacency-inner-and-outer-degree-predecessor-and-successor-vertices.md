layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$544
orderid: 100
parentid: bookofproofs$240
title: Incidence, Adjacency, Predecessor and Successor Vertices, Neighbours
description: INCIDENCE, ADJACENCY, PREDECESSOR AND SUCCESSOR VERTICES, NEIGHBOURS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$570
keywords: adjacency,degree,incoming edges,outgoing edges,incidence,neighbors,predecessors,predecessor,successors,successor
contributors: bookofproofs

---


---

Let `\(D=(V,E,\alpha,\omega)\)` be a [digraph][bookofproofs$524].
A vertex `\(v\in V\)` and an edge `\(e\in E\)` are called **incident** if `\(v\in\{\alpha(e),\omega(e)\}\)`.

Two different edges `\(e,e'\in E\)` are called **adjacent**, if there is at least one vertex incident with these edges, formally `\( e\neq e'\)` and `\(\exists v:~ v\in \{\alpha(e),\omega(e)\} \cap \{\alpha(e'),\omega(e')\} \)`. 

Two different vertices `\(v,v'\in V\)` are **neighbours** or are called **adjacent**, if there is at at least one edge incident with these vertices. `\( v\neq v'\)` and `\(\exists e:~v,v'\in \{\alpha(e),\omega(e)\} \)`. 

Let `\(v\in V\)` be a vertex of `\(D\)`. (Note: In the following definitions, the index `\(D\)` can be omitted in the notation, if it is clear from the context, which digraph `\(D\)` is concerned).

The set `\(\delta_D^+(v):=\{e\in E: \alpha(e)=v\}\)` is called **edges outgoing from v**.

The set `\(\delta_D^-(v):=\{e\in E: \omega(e)=v\}\)` is called **edges incoming to v**.

The set `\(N_D^+(v):=\{\omega(e): e\in\delta_D^+(v)\}\)` is called **successor vertices of v** or **successors of v**. 

The set `\(N_D^-(v):=\{\alpha(e): e\in\delta_D^-(v)\}\)`  is called **predecessor vertices of v** or **predecessors of v**.

The set `\(N_D(v):=N_D^+(v)\cup N_D^-(v)\)`  is called the **neighbours of v**.

### Example:


![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true)


The values of the degrees of vertices in the above graph are:

Vertex `\(v\)`  | Neighbours `\(N(v)\)` | Predecessors `\(N^-(v)\)` | Successors `\(N^+(v)\)`
:------------- |:------------- |:------------- |:-------------
 `\(a\)`| `\(\{b,c,d\}\)`| `\(\{b\}\)`| `\(\{b,c,d\}\)`
 `\(b\)`| `\(\{a,c\}\)`| `\(\{a,c\}\)`| `\(\{a\}\)`
 `\(c\)`| `\(\{a,b\}\)`| `\(\{a\}\)`| `\(\{b\}\)`
 `\(d\)`| `\(\{a,e\}\)`| `\(\{a\}\)`| `\(\{e\}\)`
 `\(e\)`| `\(\{d,e\}\)`| `\(\{d,e\}\)`| `\(\{e\}\)`
 `\(f\)`| `\(\emptyset\)`| `\(\emptyset\)`| `\(\emptyset\)`
