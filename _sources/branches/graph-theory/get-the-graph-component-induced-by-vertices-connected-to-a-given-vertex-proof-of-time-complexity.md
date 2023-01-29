layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1217
orderid: 50
parentid: bookofproofs$1216
title: 
description: OF TIME COMPLEXITY PROOF OF GET THE COMPONENT INDUCED BY VERTICES CONNECTED TO A GIVEN VERTEX &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$570
keywords: component,connected,get,given,graph,induced,vertex,vertices,proof
contributors: bookofproofs

---


---

Let `\(G(V,E)\)` be a [directed][bookofproofs$524] or [undirected graph][bookofproofs$523] and let `\(v\in V\)` be one of its vertices. We want to prove that the time complexity of the algorithm `\(\mathtt{getCOMPONENT(G,v,m)}\)` is `\(\mathcal O (|V|+|E|)\)`.

The time complexity of the first for-next loop in the lines from `\(1\)` to `\(4\)` is `\(|V|\)`. 

Since the input graph `\(G\)` is in [adjacency list representation][bookofproofs$1215] and according to the [handshaking lemma for undirected graphs][bookofproofs$1173], the while loop in the lines from `\(5\)` to `\(14\)` is repeated for at most `\(2 \cdot |E|\)` times, with a constant time complexity of each repetition. 

The final for-next loop in the lines from `\(15\)` to `\(20\)` has the time complexity of at most  `\(|V| + |E|\)`.

Altogether, the time complexity of the algorithm is

`\[|V|+2\cdot |E|+ |V|+|E|=\mathcal O(|V|+|E|).\]`
