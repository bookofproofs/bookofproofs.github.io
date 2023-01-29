layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$972
orderid: 50
parentid: bookofproofs$6374
title: 
description: Proof of EULER CHARACTERISTIC FOR PLANAR GRAPHS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$566
keywords: euler characteristic,euler's formula for polyhedra,euler's formula for planar graphs,proof
contributors: bookofproofs

---


---

* By hypothesis, `$G$` is a [connected][bookofproofs$1166] [planar graph][bookofproofs$1226] with a [planar drawing][bookofproofs$1212] consisting of `\(v\)` [vertices][bookofproofs$523], `\(e\)` [edges][bookofproofs$523] and `\(f\)` [faces][bookofproofs$6373].
* We may assume that `$v\ge 1,$` since a connected graph requires at least one vertex.
* First, we observe: If the formula `$v-e+f=2$` holds for a [multigraph][bookofproofs$523] (i.e. an undirected graph with some [loops][bookofproofs$523] and/or [multiple edges][bookofproofs$523]), then it also holds for a [simple graph][bookofproofs$523] obtained from this multigraph by removing all loops and replacing all multiple edges by simple edges.
   * For if we remove a loop or remove in a given multiple edge one of the edges, the numbers `$e$`,$f$ and `$v$` change as follows:
      * `$e\to e-1$`
      * `$f\to f-1$`
      * `$v\to v$`
      * an the formula remains unchanged.
* Therefore, we can assume that we have a [connected][bookofproofs$1166] [simple graph][bookofproofs$523], for which we have to check the formula `$v-e+f=2.$` 
* Case `$v=1$`:
   * We have `$e=0$` and `$f=1$` ([infinite face][bookofproofs$6373]) and the formula is correct.
* Case `$v=2$`:
   * We have `$e=1$` and `$f=1$` ([infinite face][bookofproofs$6373]) and the formula is again correct.
* Case `$v > 2.$`
   * Since the graph is [connected][bookofproofs$1166], we can remove edges one by one to get the case `$v=2.$` When removing the edges, we have again two sub-cases:
      * Case a) The to-be-removed edge has one vertex with [degree][bookofproofs$362] `$=1$` and the other with degree `$ > 1$`.
         * In this case, removing the edge would disconnect the graph unless we also remove the vertex with degree `$=1$`. Thus, 
         * `$e\to e-1$` (the removed edge)
         * `$f\to f$` (the surrounding face of the removed edge does not change).
         * `$v\to v-1$` (the removed vertex with degree `$=1$`)
         * Thus, the formula `$v-e+f=2$`, if correct, does not change.
      * Case b) Both vertices incident to the to-be-removed edge have a [degree][bookofproofs$362] `$ > 1$`.
         * In this case, removing the edge will not disconnect the graph and we do not have to remove any vertices. Thus, 
         * `$e\to e-1$` (the removed edge),
         * `$f\to f-1$` (two faces incident to the removed edge are melted together to one face),
         * `$v\to v$` (no removed vertices).
         * Thus, the formula `$v-e+f=2$`, if correct, does not change.
   * Altogether, we have shown for the case `$v > 2$` that we can transform the graph to the case `$v=2,$` for which we have already proven the formula `\[v-e+f=2.\]`
* It follows that the formula holds for all connected [planar graphs][bookofproofs$1226] with a [planar drawing][bookofproofs$1212].
