layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1219
orderid: 600
parentid: bookofproofs$159
title: Weakly and Strongly Connected Digraphs
description: WEAKLY AND STRONGLY CONNECTED DIGRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: connected,digraphs,strongly,weakly
contributors: bookofproofs

---


---

Let `\(D(V,E,\alpha,\omega)\)`  be a non-empty [digraph][bookofproofs$524].
> `\(D\)` is called **disconnected**, if for some vertices `\(x,y\in V\)` there is **either** a [path][bookofproofs$1164] in `\(D\)` from `\(x\)` to `\(y\)` **nor** a path from `\(y\)` to `\(x\)`.


> `\(D\)` is called **weakly connected**, if for any two vertices `\(x,y\in V\)` there is a [path][bookofproofs$1164] in `\(D\)` from `\(x\)` to `\(y\)` **or** from `\(y\)` to `\(x\)`.

> `\(D\)` is called **strongly connected**, if for any two vertices `\(x,y\in V\)` there is a [path][bookofproofs$1164] in `\(D\)` from `\(x\)` to `\(y\)` **and** from `\(y\)` to `\(x\)`.

### Example
 

![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true)


In the digraph above, there is no path to or from `\(f\)`. Thus the digraph is disconnected.

However, the subgraph `\(D[a,b,c,d,e]\)` is weakly connected, since `\(ade\)` is a path from `\(a\)` to `\(e\)`, but there is no path from `\(e\)` to `\(a\)`.

The subgraph `\(D[a,b,c]\)` is strongly connected, since for any pairs of vertices `\(a,b\)`, and `\(b,c\)` and `\(c,a\)`, there are paths in both directions.
