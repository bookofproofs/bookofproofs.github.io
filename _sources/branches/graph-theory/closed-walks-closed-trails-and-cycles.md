layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1165
orderid: 100
parentid: bookofproofs$159
title: Closed Walks, Closed Trails, and Cycles
description: CLOSED WALKS, CLOSED TRAILS, AND CYCLES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$1163
keywords: chord,cycle,cycles,trails,walks,closed walk chords,closed walk,closed trail,closed walks
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be a [simple graph][bookofproofs$523].
* A [walk (or trail) ][bookofproofs$1164] `\(W^k=v_0e_0v_1e_1v_2e_2\ldots e_{k-1}x_{k}\)` in `\(G\)` is called a **closed walk** (or a closed trail) if `\(x_k=x_0\)`.
* A [path][bookofproofs$1164] `\(C^k:=x_0x_1\ldots x_{k-1}x_k\)` with `\(x_0=x_k\)`, but `\(x_0\neq x_i\)` for `\(i=1,\ldots,k-1\)` is called a **cycle**. Note that from this definition it allows any cycle in a simple graph contains at least three different vertices.
* An edge which joins two vertices of a cycle but is not itself an edge of the cycle is a **chord** of that cycle.


#### Examples:


![graphs1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs1.jpg?raw=true)


In the figure above: 

* `\(abcgfcdefcdefgha\)` is a closed walk, but not a closed trail because the e.g. the edges `\(gf\)`, `\(cd\)`, etc. are passed more then once.
* `\(abcdefcgha\)` is a closed trail, but not a cycle because the vertex `\(c\)` is passed more then once.
* `\(abcdefgha\)` is a cycle (every edge and every vertex is passed exactly once); the edges `\(cg\)` and `\(cf\)` are the chords of that cycle.
* `\(abcgha\)` is a cycle without any chords.
