layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1172
orderid: 300
parentid: bookofproofs$240
title: Vertex Degrees for Digraphs
description: VERTEX DEGREES FOR DIGRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: degrees,digraphs,vertex
contributors: bookofproofs


---


---

Let `\(D=(V,E,\alpha,\omega)\)` be a [digraph][bookofproofs$524], `\(v\in V\)` be a vertex of `\(D\)`.

The number  `\(d_D^+(v)\)` of [edges outgoing][bookofproofs$544] from `\(v\)`, i.e. the number of elements of the set `\(\delta_D^+(v):=\{e\in E: \alpha(e)=v\}\)`, is called the **outer degree** of `\(v\)`, formally `\(d_D^+(v):=|\delta_D^+(v)|\)`.


The number `\(d_D^-(v)\)` of [edges incoming][bookofproofs$544] to `\(v\)`, i.e. the number of elements of the set   `\(\delta_D^-(v):=\{e\in E: \omega(e)=v\}\)` is called the **inner degree** of `\(v\)`, formally `\(d_D^-(v):=|\delta_D^-(v)|\)`.

The number `\(d_D(v):=d_D^+(v)+d_D^-(v)\)` is called the **degree** of `\(v\)`.

Note: In the above definitions, the index `\(D\)` can be omitted in the notation, if it is clear from the context, which digraph `\(D\)` is concerned.

### Example:


![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true)


The values of the degrees of vertices in the above graph are:

Vertex `\(v\)`  | Degree `\(d(v)\)` | Inner Degree `\(d^-(v)\)` | Outer Degree `\(d^+(v)\)`
:------------- |:------------- |:------------- |:-------------
 `\(a\)`| `\(5\)`| `\(2\)`| `\(3\)`
 `\(b\)`| `\(6\)`| `\(4\)`| `\(2\)`
 `\(c\)`| `\(4\)`| `\(1\)`| `\(3\)`
 `\(d\)`| `\(3\)`| `\(1\)`| `\(2\)`
 `\(e\)`| `\(4\)`| `\(3\)`| `\(1\)`
 `\(f\)`| `\(0\)`| `\(0\)`| `\(0\)`
