layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6395
orderid: 50
parentid: bookofproofs$6394
title: 
description:  Proof of BOUNDS FOR THE MINIMAL TREE DECOMPOSABILITY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: bounds,decomposability,minimal,tree,proof
contributors: bookofproofs

---


---

By hypothesis, `\(G(V,E,\gamma)\)` is a [finite][bookofproofs$6354] [undirected graph][bookofproofs$523].
* **Trivial lower bound**: If `\(G\)` contains loops if and only if the [minimal tree decomposability][bookofproofs$6393] `\(\tau(G)=0\)`, since there is no [tree decomposition][bookofproofs$6392] of at least the order `\(k\ge 1\)`: `\(V_1,\ldots,V_k\)`, such that the  [subgraphs induced][bookofproofs$390] by the vertices `\(V_i\)`, `\(G[V_i]\)` are all [trees][bookofproofs$96]. Otherwise, if a loop vertex is contained in e.g. the partition `\(V_i\)` for some `\(i\)`, then the induced subgraph `\(G[V_i]\)` is not a tree. Thus, `\(\tau(G)\ge 0\)`.
* **Trivial upper bound**: If `\(G\)` contains no loops and `\(n\)` vertices in total, then taking each vertex `\(v\)` as a single partition gives us an induced tree `\(G[v]\)` and there are exactly `\(n\)` such trees. Thus, `\(\tau(G)\le n\)`.
* **Improved lower bound**: 
   * Assume, `\(G\)` has no loops.
   * If `\(G\)` has `\(l\)` [components][bookofproofs$1221], let `\(m_i\)` denote the number of vertices in the `\(i\)`-th component, `\(i=1,\ldots, l\)` with multiedges. 
   * If the `\(i\)`-th component contains vertices `\(v\)` and `\(w\)` connected by multiedges, the induced graph `\(G[v,w]\)` is not a tree. Note that `\(m_i\)` equals either `\(0\)` or is an even number `\(\ge 2\)`.
   * Therefore, the `\(i\)`-th component can be decomposed into at least `\(k_i\)` trees, where `\(k_i\)` equals at least `\(1\)` or the the even number `\(m_l\ge 2\)` of vertices connected by multiedges.
   * It follows that `\(\tau(G)\ge\sum_{i=1}^l\max(1,m_i)\)`. 
* **Lower and upper bounds for forests**:
   * If `\(G\)` is a [forest][bookofproofs$96] with `\(l\)` trees, each of its components is a tree, and each tree has the minimal tree decomposition of `\(1\)`. 
   * Therefore `\(\tau(G)=l\)`.
