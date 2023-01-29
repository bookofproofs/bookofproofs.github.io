layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1222
orderid: 50
parentid: bookofproofs$1221
title: 
description:  Proof of CONNECTIVITY IS AN EQUIVALENCE RELATION - COMPONENTS ARE A PARTITION OF A GRAPH &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$570
keywords: are,components,connectivity,equivalence,graph,partition,relation,proof
contributors: bookofproofs

---


---

From the definition of [connectivity][bookofproofs$1223] in a directed (or undirected) graph `\(G(V,E)\)` it follows that two vertices `\(x,y\in V\)` are connected (strongly connected), if there is a path from `\(x\)` to `\(y\)` (respectively also from `\(y\)` to `\(x\)`. We define the relation "`\(\leftrightarrow\)`" as follows:

`\[x\leftrightarrow y\Longleftrightarrow x\text{ and }y\text{ are (strongly) connected.}\]`

It is sufficient to show that "`\(\leftrightarrow\)`"  defines an [equivalence relation][bookofproofs$574] on the set `\(V\)`, because then it follows immediately that any vertex `\(v\in V\)` can be chosen as a representative of a unique equivalence class of vertices `\(V'\in V/_\leftrightarrow\)` such that the [subgraphs][bookofproofs$390] (respectively [subdigraphs][bookofproofs$1171]) `\(G[V']\)` contain the vertex `\(v\)`.

We have to show three properties of "`\(\leftrightarrow\)`" in order to prove, that it is an equivalence relation:

> `\((1)\)` Reflexivity: `\(x\leftrightarrow x\)` for all `\(x\in V\)`
This is trivial, since any vertex is connected to itself.

> `\((2)\)` Symmetry: `\(x\leftrightarrow y\Longleftrightarrow y\leftrightarrow x\)` for all `\(x,y\in V\)`
This follows immediately from the definition of connectivity (strong connectivity) of `\(G\)`.

> `\((3)\)` Transitivity: If `\(x\leftrightarrow y\)` and `\(y\leftrightarrow z\)`, then `\(x\leftrightarrow z\)` for all `\(x,y,z\in V\)`
If `\(P_1=v_0v_1\ldots v_k\)` is a path from `\(x\)` to `\(y\)` and `\(P_2=u_0u_1\ldots u_l\)` from `\(y\)` to `\(z\)`, then we have `\(v_0=x\)`, `\(v_k=u_0=y\)` and `\(u_l=z\)`. Thus, we can merge both path and create the walk`\[W:=v_0v_1\ldots v_ku_1\ldots u_l\]`from `\(x\)` to `\(z\)`. In general, this walk is not a path, since it may contain some identical vertices other then `\(v_k=u_0\)`. In this case, the walk contains cycles, and we can "short-cut" the walk to create a path by removing any detours. Since, by construction, such a path from `\(x\)` to `\(z\)` always exists, we have `\(x\leftrightarrow z\)`.
