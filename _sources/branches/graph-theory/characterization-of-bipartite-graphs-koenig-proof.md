layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6371
orderid: 50
parentid: bookofproofs$6370
title: 
description:  Proof of CHARACTERIZATION OF BIPARTITE GRAPHS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$566
keywords: bipartite,characterization,graphs,koenig,proof
contributors: bookofproofs

---


---

### "`\(\Rightarrow\)`"

* Assume, `\(G(V,E,\gamma)\)` is an [undirected graph][bookofproofs$523], which is  [bipartite][bookofproofs$1236].
* Then, by definition, there is a [partition][bookofproofs$7991] of vertices `\(V=A\cup B,~ A\cap B=\emptyset\)` with `\(\gamma(e)=X\)` for pairs of vertices `\(X=\{x,y\}\)` such that either  `\(x\in A, y\in B\)`  or `\(x\in B, y\in A\)` for all `\(e\in E\)`.
* Since there is a [path][bookofproofs$1164] between any two vertices in `\(A\)` and `\(B\)`, and both form a partition of `\(V\)`, the graph is [connected][bookofproofs$1166].
* It follows that every [cycle][bookofproofs$1165] `\(C^k\)` alternates between `\(A\)` and `\(B\)`, and therefore has an [even][bookofproofs$8130] length `\(k\)`.
* It follows that there is no cycle in `\(G\)` with an [odd][bookofproofs$8130] length `\(k\)`.

### "`\(\Leftarrow\)`"

* Assume that there is no cycle in `\(G\)` with an [odd][bookofproofs$8130] length `\(k\)` and that `\(G\)` is [connected][bookofproofs$1166].
* Let the distance  `\(d(u,v)\)` between `\(u,v\in V\)` be the length of the shortest [path][bookofproofs$1164] between `\(u\)` and `\(v\)`. 
* Define `\(U_i:=\{v\in V~:~d(u,v)=i\}\)` for `\(i=0,1,2\ldots\)`. Note that an edge can join vertices in `\(U_i\)` and `\(U_j\)` only if `\(j=i\)` or `\(j=i+1\)` or `\(j=i-1\)`.
* Claim: There is no edge between vertices in `\(U_i\)`. 
   * Otherwise, if `\(y,y'\in U_i\)` and `\(yy'\in E\)`, then the shortest paths `\(u-y\)` and `\(u-y'\)` would have length `\(i\)` by construction. 
   * Let `\(w\)` be the last common vertex.
   * Then the paths `\(w-y\)` and `\(w-y'\)` and the edge `\(yy'\)` form a cycle of length `\(2(i-d(u,w)\)` + 1, [contradicting][bookofproofs$744] the absence of odd cycles.
* By setting `\(A:=U_0\cup U_2\cup U_4,\cup\ldots\)` and `\(B:=U_1\cup U_3\cup U_5,\cup\ldots\)` we get a partition of `\(G\)`
* Therefore `\(G\)` is bipartite.
