layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$8448
orderid: 50
parentid: bookofproofs$226
title: Chromatic Number and `$k$`-Coloring of a Graph
description: CHROMATIC NUMBER AND K-COLORING OF A GRAPH ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$566
keywords: chromatic number,k-coloring,k-colorable,colored,k-colored
contributors: bookofproofs

---


---

Let `$G(V,E)$` be a [simple graph][bookofproofs$523] and let `$K:\{1,\ldots,n\}$` be a set of `$n$` "colors". A *$k$-coloring* is a [function][bookofproofs$592] `$f:V\to K$` assigning to the vertices `$V$` exactly `$k\in K$` colors in such a way that adjacent vertices are assigned different colors. We call `$G$` *$k$-colorable*, if it has a `$k$`-coloring.

The **chromatic number** `$\chi(G)$` is the smallest number `$k$` for which `$G$` is `$k$`-colorable.

### Notes

* This definition makes sense for simple graphs only. In general [undirected graphs][bookofproofs$523], there might be loops and therefore, a vertex would be adjacent to itself and excluded from coloring. 
* Also, multiple edges between two edges are irrelevant for coloring, since even only one edge between two vertices forces the vertices to have different colors.
