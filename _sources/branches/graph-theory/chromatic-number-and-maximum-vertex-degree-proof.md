layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$8450
orderid: 50
parentid: bookofproofs$8449
title: By Induction
description: PROOF OF CHROMATIC NUMBER AND MAXIMUM VERTEX DEGREE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$566
keywords: chromatic number and maximum vertex degree,proof
contributors: bookofproofs

---


---

* By hypothesis, `$G$` is a [simple graph][bookofproofs$523] with the maximum [vertex degree][bookofproofs$362] `$d$`.
* We will prove `$\chi(G)\le d+1$` [by induction][bookofproofs$657] on `$d$`.
* Base case `$n=1:$`
   * For a simple graph `$K_1$` with one vertex, the [chromatic number][bookofproofs$8448] is trivially `$\chi(K_1)=1$` and `$d=0$`, thus `$\chi(K_1)\le 0 + 1.$` 
* Induction step `$n\to n+1:$`
   * Let `$G$` be a simple graph with `$n$` vertices `$v_1,\ldots,v_n$` and maximum vertex degree `$d$` and assume, `$\chi(H)\le d+1$` for all simple subgraphs `$H\subset G$` of `$G$` with fewer than `$n$` vertices.
   * We construct a [subgraph][bookofproofs$390] `$H_i=G[v_1,\ldots,v_{i-1},v_{i+1},\ldots,v_n],$` obtained from `$G$` by removing any vertex `$v_i$` ($i\in\{1,\ldots,n\}$ and its incident edges.
   * By induction assumption, `$\chi(H_i)\le d+1$` for all `$i=1,\ldots,n.$`
   * Since `$v_i$` has at most `$d$` neighbours, these vertices can be colored with at most `$d$` colors.
   * From the [coloring][bookofproofs$8448] of any given subgraph `$H_i,$` we can therefore obtain the coloring of `$G$` by selecting a `$(d+1)$`st color distinct to the `$d$` colors of the neighbours of `$v_i$`. 
   * It follows `$\chi(G)\le d+1.$` 
* By induction, it follows that the statement is true for all simple graphs with `$n$` vertices, `$n\ge 1.$`
