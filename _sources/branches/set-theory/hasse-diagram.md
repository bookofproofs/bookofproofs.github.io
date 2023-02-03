layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$267
orderid: 600
parentid: bookofproofs$189
title: Hasse Diagram
description: HASSE DIAGRAM ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: diagram,hasse,hasse diagram,hasse diagrams
contributors: bookofproofs


---


---

A **Hasse diagram** is a method named after [Helmut Hasse](https://mathshistory.st-andrews.ac.uk/Biographies/Hasse/) (1898 - 1979), who used it to visualize a [poset][bookofproofs$576] `$(V,\preceq )$`, which has only a finite number[^1] of elements. A Hasse diagram of a set `$V$` can be drawn by applying the following rules:

* Draw the elements of `$V$` as points in the plane and label them.
* If `$a\preceq b$` for some two elements `$a$` and `$b$`, then draw `$b$` "above" `$a$` and connect both by an arrow or line `$ab$`.
* If `$a\preceq c$` because `$a\preceq b\preceq c$` for some `$b$`, avoid drawing an additional arrow `$ac$`, because there are already arrows `$ab$` and `$bc.$` 
 

As an example, consider the poset of the [divisors][bookofproofs$1273]  of `$24,$` i.e. the set `$D:=\{1,2,3,4,6,8,12,24\}$` with the order `$\prec:=\{(a,b)\in D\times D: a\mid b\}$`. There are elements, which are incomparable (e.g. `$3$` and `$8$` since `$3\not\mid 8$`). Otherewise, there are many transitivities, e.g. `$1 \mid 2$`, `$2\mid 4$`, `$4\mid 8$`, and `$8\mid 24$`). To see the Hasse diagram, click on the _Evaluate_ button below: 
§§§1

[^1]: We will define later on what "finite" means in a strict mathematical manner. For the time being, it is sufficient to rely on the meaning of this word in the English language.

---

§§§1
<div class='sage'>
P = Poset((divisors(24), attrcall("divides")), linear_extension=True); P
</div>
