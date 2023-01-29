layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$1234
orderid: 50
parentid: bookofproofs$1233
title: 
description:  Proof of WHEN IS IT POSSIBLE TO FIND A SEPARATING CYCLE IN A BICONNECTED GRAPH, GIVEN A NON-SEPARATING CYCLE? &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1228
keywords: biconnected,cycle,find,given,graph,non,possible,separating,when,proof
contributors: bookofproofs

---


---

Let `\(G(V,E,\gamma)\)` be a [biconnected graph][bookofproofs$1227] and let `\(C(V_c,E_c)\)` be a [non-separating cycle][bookofproofs$1232] with the [piece][bookofproofs$1231] `\(P(V_p,E_p)\)`, which is, by hypothesis, not a [path][bookofproofs$1164]. Let `\(u\)` and `\(v\)` be two [attachments][bookofproofs$1231] of `\(P\)` that are consecutive in the circular order of `\(C\)`, i.e. if `\(C:=x_0x_1\ldots x_{k-1}x_k\)` with `\(x_k=x_0\)`, then `\(u=x_i\)` and `\(v=x_j\)` for some `\( i < j\)` and there is no other attachment of `\(P\)` among the vertices `\(u=x_i,x_{i+1},\ldots,x_{j-1},x_j=v\)`, besides `\(u\)` and `\(v\)`. 

In the example below, the edges of the cycle `\(C\)` are colored blue and the vertices of the piece `\(P\)` are colored orange. Moreover, `\(u\)` and `\(v\)` are two attachments of `\(P\)` that are consecutive in the circular order of `\(C\)`:


![pieces3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces3.jpg?raw=true)


We want to show that, provided `\(P\)` is not a path (which is the case in our example), it is possible to construct a separating cycle `\(S(V_s,E_s)\)`, which consists of a subpath of `\(C\)` plus a path of `\(P\)` between the attachments `\(u\)` and `\(v\)` of `\(P\)`. 

We observe that, by construction, `\(E=x_ix_{i+1}\ldots x_{j-1}x_j\)` is a subpath of `\(C\)` from `\(u\)` to `\(v\)` that does not contain any attachment of `\(P\)`. Moreover, by [definition of a piece][bookofproofs$1231], `\(P(V_p,E_p)\)` is connected. Thus, there is also another path `\(F\)` from `\(u\)` to `\(v\)` in `\(P\)`. 

In our example, both paths `\(E\)` (dashed red) and `\(F\)` (dashed blue) are shown in the following figure: 


![pieces4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces4.jpg?raw=true)



Let `\(S\)` be a cycle obtained from `\(C\)` by replacing `\(E\)` with `\(F\)` (see next figure):


![pieces2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces2.jpg?raw=true)


It remains to be shown that `\(S\)` is a [separating cycle][bookofproofs$1232] cycle. First of all, we have by construction that `\(E\)` is a piece of `\(G\)` with respect to `\(S\)`. By hypothesis, `\(P\)` is not a path. Therefore, there exists an edge `\(e\)` of `\(P\)` which is not an edge of `\(F\)`. Therefore, there must exist  another piece of `\(G\)` with respect to `\(S\)`, which is distinct to `\(E\)` (see next figure):


![pieces5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/pieces5.jpg?raw=true)


Since there are more than one pieces of `\(G\)` with respect to `\(S\)`, `\(S\)` is a separating cycle.
