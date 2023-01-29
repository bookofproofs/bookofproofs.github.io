layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1171
orderid: 200
parentid: bookofproofs$240
title: Subdigraphs and Superdigraphs; Induced Subdigraph
description: SUBDIGRAPHS AND SUPERDIGRAPHS; INDUCED SUBDIGRAPH &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$570
keywords: induced,subdigraph,subdigraphs,superdigraphs
contributors: bookofproofs

---


---

Let `\(D(V,E,\alpha,\beta)\)` be a [digraph][bookofproofs$524]. A digraph `\(S(V',E',\alpha',\beta')\)` is called a **subdigraph** of `\(D\)`, written as `\(S\subseteq D\)`, if it fulfills the following properties:

1. `\(V'\)` consists only of vertices from `\(V\)`, formally `\(V'\subseteq V\)`. 
1. `\(E'\)` consists only of edges from `\(E\)`, formally `\(E'\subseteq E\)`. 
1. `\(\alpha'\)` and `\(\omega'\)` are [restrictions][bookofproofs$1170] of `\(\alpha\)` and `\(\omega\)` on `\(E'\)`, i.e. `\(\alpha':={\alpha|}_{E'}E\mapsto V\)` and `\(\omega':={\omega|}_{E'}E\mapsto V\)`.  

If `\(S\)` is a subdigraph of `\(D\)`, then `\(D\)` is called the **superdigraph** of `\(S\)`.

If `\(S\)` contains all the edges `\(e\)` with `\(\alpha(e),\omega(e)\in V'\)`, then `\(S\)` is an **induced subdigraph** of `\(D\)`; we say that the vertices `\(V'\)` **induce** or **span** `\(S\)` in `\(D\)` and write `\(S:=D[V']\)`. Thus, if `\(V'\subseteq V\)` is any set of vertices, `\(V'=\{v_1,v_2,\ldots,v_n\}\)`, then the induced subdigraph `\(D[V']=D[v_1,v_2,\ldots,v_n]\)` denotes the digraph whose edges are precisely the edges of `\(D\)` with initial and terminal vertices in `\(V'\)`.
 
#### Example


![graphs8](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/graphs8.jpg?raw=true)


In the above figure, the digraphs `\(D_2, D_3\)` and `\(D_4\)` are all subdigraphs of the digraph `\(D_1\)`. However, only `\(D_2\)` and and `\(D_4\)` are induced subdigraphs of `\(D_1\)`, since

`\[D_2=D_1[a,b,c],\quad D_4=D_1[a,c,d],\]`

but

`\[D_3\neq D_1[c,d].\]`
