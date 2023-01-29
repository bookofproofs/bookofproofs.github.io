layout: proof
categories: branches,set-theory
nodeid: bookofproofs$981
orderid: 50
parentid: bookofproofs$980
title: 
description:  Proof of CARDINAL NUMBER &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979
keywords: cardinal number,cardinalities,cardinality,cardinal numbers,proof
contributors: bookofproofs

---


---

It is sufficient to show that being [equipotent][bookofproofs$978] is an [equivalence relation][bookofproofs$574] `\("\sim"\)` on the sets belonging to a given (non-empty) set system `\(\mathcal X\)`. In the following, let `\(A,B,C\subseteq\mathcal X.\)`

* Since there is always a [bijective function][bookofproofs$771] `\(f:A\to A\)` (i.e. the set `\(A\)` is equipotent to itself), we have that `\(A\sim A\)`. Therefore, "`$\sim$`" is [reflexive][bookofproofs$572].
* Let `\(A\sim B\)`. Since there is bijective function `\(f:A\to B\)`, it is [invertible][bookofproofs$407] with `$f^{-1}:B\to A.$` Thus, `$B\sim A$` and "`$\sim"`" is [symmetric][bookofproofs$572].
* Let `\(A\sim B\)` and `\(B\sim C\)`. Therefore there are bijective maps `\(f_1:A\to B\)` and `\(f_2:B\to C\)`. Since the [composition of bijective functions is bijective][bookofproofs$6866], the is bijective function  `\(f:=f_2\circ f_1 :A\to C\)`. Thus `\(A\sim C\)`, and "`$\sim"`" is [transitive][bookofproofs$572].
* Therefore, "`$\sim$`" is an [equivalence relation][bookofproofs$574], by definition.
