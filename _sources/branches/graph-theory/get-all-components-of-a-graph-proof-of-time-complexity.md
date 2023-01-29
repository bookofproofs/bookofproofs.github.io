layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1225
orderid: 100
parentid: bookofproofs$1220
title: 
description:  OF TIME COMPLEXITY Proof of GET ALL COMPONENTS OF A GRAPH &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$570
keywords: all,components,get,graph,proof
contributors: bookofproofs

---


---

The time complexity of the corresponding algorithm `\(\mathtt{getCOMPONENT(G,v,m)}\)` obtaining the [component induced by vertices connected to a biven vertex][bookofproofs$1216] `\(v\)` is `\(\mathcal O(|V|+|E|)\)`. 

The fact that `\(\mathtt{getCOMPONENT(G)}\)` calls the algorithm `\(\mathtt{getCOMPONENT(G,v,m)}\)` inside an additional for-next loop in the lines `\(6\)` to `\(12\)` has no impact on this time complexity, since both algorithms make use of the same `\(visited\)` property of the vertices in the graph.
