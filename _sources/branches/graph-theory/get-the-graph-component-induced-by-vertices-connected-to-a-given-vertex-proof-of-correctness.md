layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1218
orderid: 100
parentid: bookofproofs$1216
title: By Induction
description:  OF CORRECTNESS Proof of GET THE COMPONENT INDUCED BY VERTICES CONNECTED TO A GIVEN VERTEX &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$570,bookofproofs$1163
keywords: component,connected,get,given,graph,induced,vertex,vertices,proof
contributors: bookofproofs

---


---

The if-statement in the steps `\(9\)` to `\(12\)` of the algorithm `\(\mathtt{getCOMPONENT(G,v,m)}\)` makes sure that in the algorithm **visits only** the vertices [connected][bookofproofs$1223] to `\(v\)`.

In order to prove that the algorithm **visits all** such vertices, i.e. that `\(G'\)` contains all vertices `\(n\)` in `\(G\)` connected to `\(v\)`, follows [by induction][bookofproofs$657] on the length `\(k\)` of the [path][bookofproofs$1164] from `\(v\)` to a vertex `\(n\)`

### Base case

For `\(k=0\)` we have trivially `\(u=v\)`.

### Induction step

Let `\(v\)` and `\(u\)` be connected, i.e, for `\(k\ge 0\)`, `\(P^k\)` be the path from `\(v\)` to `\(u\)`:
`\[P^k:=x_0x_1\ldots x_{k-1}x_k\]`

with `\(x_0:=v\)` and `\(x_k=u\)`. The for-next loop in the lines `\(8\)` to `\(13\)` iterates over all neighbors of `\(u\)`, which have not yet been visited in the algorithm. Therefore, each such neighbor `\(n\)` is not yet in `\(P^k\)`. Thus, we can add `\(n\)` to `\(P_k\)` creating an even longer path from `\(v\)` to `\(n\)`, i.e.

`\[P^{k+1}:=x_0x_1\ldots x_{k-1}x_kx_{k+1}\]`

with `\(x_0:=v\)`, `\(x_k=u\)` and `\(x_{k+1}=n\)`. Therefore, `\(v\)` is connected with `\(n\)`.
