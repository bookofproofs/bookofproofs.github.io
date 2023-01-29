layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1179
orderid: 50
parentid: bookofproofs$227
title: Unit-Cost Random Access Machine
description: UNIT-COST RANDOM ACCESS MACHINE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: access,cost,machine,random,unit,unit-cost,unit-cost random access machine
contributors: bookofproofs

---


---

A *Unit-Cost Random Access Machine* (Unit-Cost `\(R A M \)`) is a model of computation with the following properties:

> `\((i)\)` `\(R A M \)` contains [finitely many][bookofproofs$985] registers `\(r_1,\ldots,r_n\)`.

> `\((ii)\)` Each register `\(r_i\)` can store exactly  one[^1] [natural number][bookofproofs$718].
> `\((iii)\)` At the beginning of computation, each register contains an initial number, generally it is the number `\(0\)`.

> `\((iv)\)` The `\(R A M\)` machine contains either a [ `\(L O O P\)` program][bookofproofs$1180] , or a [ `\(W H I L E\)` program][bookofproofs$1181], or a [ `\(G O T O \)` program][bookofproofs$1182].
[^1]: Note: Since the natural number can be arbitrarily big, we refer to the machine as *unit-cost*, since each register can store a natural number (at the same cost), no matter how big it is.
