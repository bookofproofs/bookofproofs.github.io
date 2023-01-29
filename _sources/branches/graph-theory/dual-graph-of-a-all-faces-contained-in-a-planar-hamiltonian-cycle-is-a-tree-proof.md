layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6399
orderid: 50
parentid: bookofproofs$6398
title: 
description:  Proof of DUAL GRAPH OF A ALL FACES CONTAINED IN A PLANAR HAMILTONIAN CYCLE IS A TREE &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1591
keywords: all,contained,cycle,dual,faces,graph,hamiltonian,planar,tree,proof
contributors: bookofproofs

---


---

* Assume, `\(G(V,E)\)` is a [simple][bookofproofs$523], [planar][bookofproofs$1226], and [Hamiltonian][bookofproofs$6349] graph with `\(n\)` vertices. 
* Take any [planar drawing][bookofproofs$1212] `\(\mathcal D\)` of `\(G\)`.
* Construct the corresponding [dual graph][bookofproofs$6391] `\(G^\ast_{\mathcal D}\)`.
* Draw the [Hamiltonian cycle][bookofproofs$330] `\(C^n\)` of `\(G\)` in `\(\mathcal D\)` and identify vertices `\(v_1,\ldots v_m\)` of `\(G^\ast_{\mathcal D}\)`, which are enclosed by `\(C_n\)` in `\(\mathcal D\)`. 
* We claim that the [subgraph induced][bookofproofs$390] in `\(G^\ast_{\mathcal D}\)` by those vertices, i.e. the graph `\(G^\ast_{\mathcal D}[v_1,\ldots v_m]\)` is always a [tree][bookofproofs$96]. Proof by [contradiction][bookofproofs$744]:
   * Assume,  `\(G^\ast_{\mathcal D}[v_1,\ldots v_m]\)` is not a tree.
   * Then it contains at least one cycle, say `\(C_k^\ast\)`.
   * Therefore, the drawing of `\(C_k^\ast\)` inside the planar drawing `\(D\)` contains at least one [face][bookofproofs$6373], since either `\(C_k^\ast\)` is a face itself, or it has some [chords][bookofproofs$1165] forming a face. Denote this face by `\(f^\ast\)`.
   * By [definition of the dual graph][bookofproofs$6391] `\(G^\ast_{\mathcal D}\)`, there must be a vertex `\(w\)` of `\(G\)` inside the face `\(f^\ast\)` we find in the planar drawing of the cyclic subgraph `\(G^*_{\mathcal D}[v_1,\ldots v_m]\)`.
   * But `\(w\in f^\ast\)` cannot be contained in the Hamiltonian cycle `\(C^n\)`, since `\(C^n\)` surrounds the hole subgraph subgraph `\(G^\ast_{\mathcal D}[v_1,\ldots v_m]\)`, and thus is not adjacent to `\(w\)`.
   * This a contradiction to the hypothesis that `\(C^n\)` is a Hamiltonian cycle.
   * Therefore, `\(G^\ast_{\mathcal D}[v_1,\ldots v_m]\)` must be a tree.
