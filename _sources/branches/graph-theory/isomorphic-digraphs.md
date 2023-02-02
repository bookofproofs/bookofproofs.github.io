layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1178
orderid: 100
parentid: bookofproofs$393
title: Isomorphic Digraphs
description: ISOMORPHIC DIGRAPHS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$570
keywords: digraphs,isomorphic,isomorphic definition,define isomorphic,isomorphic digraph,isomorphic digraphs,digraph definition
contributors: bookofproofs


---


---

Two [digraphs][bookofproofs$524] `\(D_1(V_1,E_1,\alpha_1,\omega_1)\)` and `\(D_2(V_2,E_2,\alpha_2,\omega_2)\)` are **isomorphic**, written as `\(D_1\equiv D_2\)`, if `\(D_2\)` can be transformed to `\(G_1\)` (and vice versa) by relabelling the vertices, without changing [adjacent][bookofproofs$544] vertices and edges. This is equivalent to a transformation, in which the number of vertices outgoing from or incoming to each vertex in `\(D_1\)` is equal to the number of edges outgoing from or incoming to the corresponding vertex in `\(G_2\)`. 

Formally, `\(D_1\equiv D_2\)` if and only if there exist two [bijective functions][bookofproofs$771], a relabelling function `\(\rho : V_1 \to V_2\)` and an edge transformation function `\(\epsilon : E_1 \to E_2\)` and such that

> `\((i)\)` `\(\rho(\alpha_1(e))=\alpha_2(\epsilon(e))\)` for all `\(e\in E_1.\)`

> `\((ii)\)` `\(\rho(\omega_1(e))=\omega_2(\epsilon(e))\)` for all `\(e\in E_1.\)`
 
Note: In the left side of the two equations `\((i)\)` and `\((ii)\)`, `\(\rho(\alpha_1(e))\)` and `\(\rho(\omega_1(e))\)` mean that we relabel the initial and terminal vertices `\(\alpha_1(e)\)` and `\(\omega_1(e)\)` of given edge `\(e\)` in the first digraph `\(D_1\)`, obtaining (in the right side of the two equations) the corresponding initial and terminal vertices `\(\alpha_2(\epsilon(e))\)` and `\(\omega_2(\epsilon(e))\)` of an edge `\(\epsilon(e)\)` in the second digraph `\(D_2\)`.

#### Example:


![graphs12](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs12.jpg?raw=true)


In the above figure, the digraphs `\(D_1\)` and `\(D_2\)` are not the same, but they are isomorphic, since we can find two bijective functions `\(\rho : V_1 \to V_2\)` and `\(\epsilon : E_1 \to E_2\)` defined by 

Definition of `\(\rho\)`:

`\(v\in V_1\)` | `\(\rho(v)\in V_2\)`
:------------- |:-------------
 `\(a\)`| `\(u\)`
 `\(b\)`| `\(x\)`
 `\(c\)`| `\(v\)`
 `\(d\)`| `\(w\)`

Definition of `\(\epsilon\)`:
`\(e\in E_1\)`|`\(\epsilon(e)\in E_2\)`
 `\(e_1\)`| `\(f_1\)`
 `\(e_2\)`| `\(f_2\)`
 `\(e_3\)`| `\(f_3\)`
 `\(e_4\)`| `\(f_4\)`
 `\(e_5\)`| `\(f_5\)`
 `\(e_6\)`| `\(f_6\)`
 `\(e_7\)`| `\(f_7\)`

such that all adjacencies in the digraphs are preserved, like demonstrated in the following table:

|`\(e\)`|`\(\alpha_1(e)\)`|`\(\omega_1(e)\)`|`\(\rho(\alpha_1(e))\)`|`\(\rho(\omega_1(e))\)`|`\(\alpha_2(\epsilon(e))\)`|`\(\omega_2(\epsilon(e))\)`|`\(\epsilon(e)\)`| 
 `\(e_1\)`| `\(a\)`| `\(b\)`| `\(u\)`| `\(x\)`| `\(u\)`| `\(x\)`| `\(f_1\)`
 `\(e_2\)`| `\(b\)`| `\(a\)`| `\(x\)`| `\(u\)`| `\(x\)`| `\(u\)`| `\(f_2\)`
 `\(e_3\)`| `\(a\)`| `\(b\)`| `\(u\)`| `\(x\)`| `\(u\)`| `\(x\)`| `\(f_3\)`
 `\(e_4\)`| `\(a\)`| `\(c\)`| `\(u\)`| `\(v\)`| `\(u\)`| `\(v\)`| `\(f_4\)`
 `\(e_5\)`| `\(b\)`| `\(d\)`| `\(x\)`| `\(w\)`| `\(x\)`| `\(w\)`| `\(f_5\)`
 `\(e_6\)`| `\(c\)`| `\(d\)`| `\(v\)`| `\(w\)`| `\(v\)`| `\(w\)`| `\(f_6\)`
 `\(e_7\)`| `\(d\)`| `\(d\)`| `\(w\)`| `\(w\)`| `\(w\)`| `\(w\)`| `\(f_7\)`
