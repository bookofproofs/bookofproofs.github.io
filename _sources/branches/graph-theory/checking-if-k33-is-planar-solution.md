layout: solution
categories: branches,graph-theory
nodeid: bookofproofs$8476
orderid: 50
parentid: bookofproofs$8475
title: 
description: SOLUTION OF CHECKING IF $K_{3,3}$ IS PLANAR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$566
keywords: checking if k33 is planar,solution
contributors: bookofproofs

---


---

* Suppose that the [complete bipartite graph][bookofproofs$6372] `$K_{3,3}$` is [planar][bookofproofs$1226] is [planar][bookofproofs$1226].
* Note that the shortest cycle in `$K_{3,3}$` is of length `$4.$`
* A [necessary condition for a graph to be planar with shortest cycle][bookofproofs$8471] requires that `$$|E|\le \frac{k}{k-2}(|V|-2),$$` where `$|E|$` ist the number of its edges and `$|V|$` is the number of its vertices.
* For `$K_{3,3}$` this condition means that `$$|E|=9\le \frac{4}{2}(6-2)=2\cdot 4=8.$$` which is false.
* Therefore, `$K_{3,3}$` is not planar.
