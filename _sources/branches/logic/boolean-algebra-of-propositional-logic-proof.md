layout: proof
categories: branches,logic
nodeid: bookofproofs$7912
orderid: 50
parentid: bookofproofs$187
title: 
description:  Proof of BOOLEAN ALGEBRA OF PROPOSITIONAL LOGIC &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$711
keywords: algebra,boolean,logic,propositional,proof
contributors: bookofproofs

---


---

Let `$B$` be the set of [Boolean terms][bookofproofs$1307]. We want to show that `$(B,\wedge,\vee,1,0)$` is a [Boolean algebra][bookofproofs$7872] with respect to the [conjunction][bookofproofs$712] [$\wedge$", the "disjunction][bookofproofs$713] "$\vee$":
* It follows from the syntax of [Boolean terms][bookofproofs$1307] that `$B$` contains the Boolean constants `$1$` and `$0$` and is closed under the operations "$\wedge$" and "$\vee$".
* It is, therefore, sufficient to demonstrate that `$(B,\wedge,\vee,1,0)$` is a Boolean algebra by verifying all required properties:
1. The [conjunction `$\wedge$` is associative][bookofproofs$6844] as well as the [disjunction `$\vee$` is associative][bookofproofs$6846], i.e. for all `\(x,y,z\in B\)` `$$\begin{array}{c}x\wedge(y\wedge z)=(x\wedge y)\wedge z,\\x\vee (y\vee z)=(x\vee y)\vee z.\end{array}$$`
1. The [conjunction `$\wedge$` is commutative][bookofproofs$1834] and the [disjunction `$\vee$` is commutative][bookofproofs$1835],  i.e. for all `\(x,y \in B\)` `$$\begin{array}{c}x\wedge y=y \wedge x,\\x\vee y=y\vee x.\end{array}$$` 
1. "`\(\wedge \)`" and "`\(\vee \)`" are [distributive over each other][bookofproofs$7910], i.e. for all `\(x,y,z\in B\)` `$$\begin{array}{c}x\wedge (y\vee z)=(x\wedge y)\vee (x\wedge z),\\x\vee (y\wedge z)=(x\vee y)\wedge (x\vee z).\end{array}$$`
1. The [Boolean constants][bookofproofs$1307] `$1$` and `$0$` have with respect to the conjunction and the disjunction the following properties:
   * `$0\in B$` is the "smallest" element: `$0\wedge x=0$` and `$x\vee 0=x$` for all Boolean terms `$x.$`
   * `$1\in B$` is the "greatest" element: `$1\wedge x=x$` and `$x\vee 1=1$` for all Boolean terms `$x.$`
1. Finally, the [negation][bookofproofs$714] `$\neg x$` is the "complent element": `$x\wedge \neg x=0$` and `$x\vee \neg x=1$`  for all Boolean terms `$x.$`


* It follows that `$B$` is a [Boolean algebra][bookofproofs$7872] `$(B,\wedge,\vee,1,0).$`
