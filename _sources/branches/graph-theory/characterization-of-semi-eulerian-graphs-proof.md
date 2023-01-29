layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6388
orderid: 50
parentid: bookofproofs$6385
title: 
description: PROOF OF CHARACTERIZATION OF SEMI-EULERIAN GRAPHS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566
keywords: characterization,eulerian,graphs,semi,semi eulerian graph,semi eulerian,semi-eulerian graph,eulerian graph,proof
contributors: bookofproofs

---


---

### "`\(\Rightarrow\)`"

* Assume, a [simple graph][bookofproofs$523] `\(G(V,E)\)` is [semi-Eulerian][bookofproofs$6387].
* Then there is an [semi-Eulerian tour][bookofproofs$6386] between a starting and finishing vertices `\(v\)` and `\(w\)`.
* Adding an edge `\(e\)` between `\(v\)` and `\(w\)` creates an [Eulerian tour][bookofproofs$391], and thus an [Eulerian graph][bookofproofs$6348] `\(G'(V,E')\)` with `\(E':=E\cup\{e\}\)`.
* By the [characterization of Eulerian graphs][bookofproofs$6381], `\(G'\)` is  [connected][bookofproofs$1166], and each of its vertices has an  [even][bookofproofs$8130] [degree][bookofproofs$362].
* Whenever this trail passes through a vertex, there is a contribution of `\(2\)` to the [degree][bookofproofs$362] of that vertex. 
* By removing the edge `\(e\)` again, we see that `\(v\)` and `\(w\)` are exactly the two vertices with an odd degree.
* Removing the edge `\(e\)` does not disconnect the graph `\(G'\)`, because there is still an open trail between `\(v\)` and `\(w\)`.
* Thus, also `\(G\)` is connected.

### "`\(\Leftarrow\)`"

* Assume, `\(G\)` is a [connected][bookofproofs$1166] graph with exactly two vertices with an [odd][bookofproofs$8130] [degree][bookofproofs$362], `\(v\)` and `\(w\)`.
* Add an edge `\(e\)` between `\(v\)` and `\(w\)` to create an [Eulerian tour][bookofproofs$391], and thus an [Eulerian graph][bookofproofs$6348] `\(G'(V,E')\)` with `\(E':=E\cup\{e\}\)`.
* By the [characterization of Eulerian graphs][bookofproofs$6381], `\(G'\)` is  [connected][bookofproofs$1166], and each of its vertices has an  [even][bookofproofs$8130] [degree][bookofproofs$362].
* Removal of the edge `\(e\)` from this trail produces an [open trail][bookofproofs$6386], i.e. a trail that includes every edge of `\(G\)` but is not a [closed trail][bookofproofs$1165].
* So, `\(G\)` is [semi-Eulerian][bookofproofs$6387].