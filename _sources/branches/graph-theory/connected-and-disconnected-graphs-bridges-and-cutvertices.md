layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1166
orderid: 500
parentid: bookofproofs$159
title: Connected and Disconnected Graphs, Bridges and Cutvertices
description: CONNECTED AND DISCONNECTED GRAPHS, BRIDGES AND CUTVERTICES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$1163
keywords: articulation point,bridge,bridges,connected,cutvertex,cutvertices,disconnected,graphs,connected and disconnected graph,disconnected graph,connected graph,connected vs disconnected graph,connected graph and disconnected graph,connected and unconnected graph,connected graph vs disconnected graph,disconnected graph definition,unconnected graph,define,
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be a non-empty undirected [graph][bookofproofs$523].
* `\(G\)` is called **connected**, if there is a [path][bookofproofs$1164] `\(P=w-u\)` between any two of its vertices `\(w\)` and `\(u\)`. Equivalently, a connected graph has exactly one component, i.e. the [output of the algorithm][bookofproofs$1220] `\(\mathtt{getCOMPONENTS(G)}\)` is a set `\(C\)` of subgraphs with `\(|C|=1\)`.
* `\(G\)` is called **disconnected**, if it has more than one component, i.e. if it is not connected. 
* An edge in a connected graph is a **bridge**, if its removal leaves a disconnected graph.
* A vertex of a connected graph is a **cutvertex** or **articulation point**, if its removal leaves a disconnected graph.

#### Examples:


![graphs2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs2.jpg?raw=true)


The above graph `\(G\)`, consisting of `\(14\)` vertices is disconnected. However, It has the following conntected components:

* `\(G[1,2,3,4,5,6,7,8]\)`
* `\(G[9,10]\)`
* `\(G[11,12,13]\)`
* `\(G[ 14 ]\)`

The edge `\((3,6)\)` is a bridge of the component `\(G[1,2,3,4,5,6,7,8]\)` and the edge `\((9,11)\)` is a bridge of the component `\(G[9,10]\)`.

The vertices `\(3\)` and `\(4\)` are articulation points of the component  `\(G[1,2,3,4,5,6,7,8]\)`.
