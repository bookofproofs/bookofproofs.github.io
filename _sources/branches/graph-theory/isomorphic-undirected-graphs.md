layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1177
orderid: 50
parentid: bookofproofs$393
title: Isomorphic Undirected Graphs
description: ISOMORPHIC UNDIRECTED GRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566,bookofproofs$570
keywords: graphs,isomorphic,undirected
contributors: bookofproofs


---


---

Two [graphs][bookofproofs$523] `\(G_1(V_1,E_1,\gamma_1)\)` and `\(G_2(V_2,E_2,\gamma_2)\)` are **isomorphic**, written as `\(G_1\equiv G_2\)`, if `\(G_1\)` can be transformed to `\(G_2\)` (and vice versa) by relabelling the vertices, without changing [adjacent][bookofproofs$525] vertices and edges. 

Formally, `\(G_1\equiv G_2\)` if and only if there exist two [bijective functions][bookofproofs$771], a relabelling function `\(\rho : V_1 \to V_2\)` and an edge transformation function `\(\epsilon : E_1 \to E_2\)` and such that

`\[\rho(\gamma_1(e))=\gamma_2(\epsilon(e))\quad\forall e\in E_1.\]`

This is equivalent to a transformation, in which the number of edges joining each pair of vertices in `\(G_1\)` is equal to the number of edges joining the corresponding pair of vertices in `\(G_2\)`. 

Note: In the left side of the equation, `\(\rho(\gamma_1(e))\)` means that we relabel the end vertices `\(\gamma_1(e)\)` of given edge `\(e\)` in the the first graph `\(G_1\)`, obtaining in the right side of the equation the corresponding end vertices `\(\gamma_2(\epsilon(e))\)` of an edge `\(\epsilon(e)\)` of the second graph `\(G_2\)`.

#### Example:


![graphs11](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs11.jpg?raw=true)


In the above figure, the graphs `\(G_1\)` and `\(G_2\)` are not the same, but they are isomorphic, since we can find two bijective functions `\(\rho : V_1 \to V_2\)` and `\(\epsilon : E_1 \to E_2\)` defined by 

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


|`\(e\)`|`\(\gamma_1(e)\)`|`\(\rho(\gamma_1(e))\)`|`\(\gamma_2(\epsilon(e))\)`|`\(\epsilon(e)\)`| 
 `\(e_1\)`| `\(\{a,b\}\)`| `\(\{u,x\}\)`| `\(\{u,x\}\)`| `\(f_1\)`
 `\(e_2\)`| `\(\{a,b\}\)`| `\(\{u,x\}\)`| `\(\{u,x\}\)`| `\(f_2\)`
 `\(e_3\)`| `\(\{a,b\}\)`| `\(\{u,x\}\)`| `\(\{u,x\}\)`| `\(f_3\)`
 `\(e_4\)`| `\(\{a,c\}\)`| `\(\{u,v\}\)`| `\(\{u,v\}\)`| `\(f_4\)`
 `\(e_5\)`| `\(\{b,d\}\)`| `\(\{x,w\}\)`| `\(\{x,w\}\)`| `\(f_5\)`
 `\(e_6\)`| `\(\{c,d\}\)`| `\(\{v,w\}\)`| `\(\{v,w\}\)`| `\(f_6\)`
 `\(e_7\)`| `\(\{d\}\)`| `\(\{w\}\)`| `\(\{w\}\)`| `\(f_7\)`
