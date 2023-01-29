layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1164
orderid: 50
parentid: bookofproofs$159
title: Walks, Trails, and Paths
description: WALKS, TRAILS, AND PATHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$1163
keywords: cycles,length,path,paths,trail,trails,walk,walks
contributors: bookofproofs

---


---

A **walk** in a [digraph][bookofproofs$524] `\(D(V,E,\alpha,\omega)\)` or an  [undirected graph][bookofproofs$523] `\(G(V,E,\gamma)\)` is a non-empty, alternating succession of vertices `\(v_i\in V\)` and edges `\(e_i\in E\)` 
`\[W^k:=v_0e_0v_1e_1v_2e_2\ldots e_{k-1}x_{k},\]`
such that `\(e_i=v_iv_{i+1}\)` for all `\(i < k\)`. 

A **trail** is a walk, in which all the edges, but not necessarily all the vertices all distinct. 

A **path** is a walk, in which all the edges and all the vertices are distinct. We denote the path by  `\(P^k:=x_0x_1\ldots x_{k-1}x_k\)`. 

The number `\(k\)` of the edges in the walk (or the trail, or the path) is called its **length**. 

Please note that for walks, (or trails or paths), `\(k\)` is allowed to be zero; thus e.g. a walk with `\(k\)` vertices `\(W_k\)` has a length of `\(k-1\)` edges; a path `\(P^0\)` consists of just one vertex (and does not contain any edges).


#### Examples: 


![graphs1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs1.jpg?raw=true)


In the undirected graph above: 

* `\(abcgfcdefghabcde\)` is a walk, but not a trail because the e.g. the edges `\(gf\)`, `\(ab\)`, etc. are passed more then once.
* `\(abcdefcg\)` is a trail, but not a path because the vertex `\(c\)` is passed more then once.
* `\(abcdef\)` is a path (every edge and every vertex is passed exactly once).


![graphs5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs5.jpg?raw=true)



In the digraph above: 

* there is no path from `\(e\)` to `\(a\)`, however, `\(ade\)` is a path from `\(a\)` to `\(e\)`
* `\(acbacbdeee\)` is a walk
