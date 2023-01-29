layout: definition
categories: branches,set-theory
nodeid: bookofproofs$7995
orderid: 700
parentid: bookofproofs$189
title: Special Elements of Ordered Sets
description: SPECIAL ELEMENTS OF ORDERED SETS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$979
keywords: maximal,greater,minimal,smaller,maximum,greatest,minimum,smallest,greater or equal,smaller or equal,upper bound,lower bound,upper bounds,lower bounds,supremum,infimum,maxima,minima,suprema,infima,least upper bound,greatest lower bound,special elements of ordered sets
contributors: bookofproofs


---


---

Let `$(V,\preceq )$` be a [poset][bookofproofs$576] or a [strictly ordered set][bookofproofs$7993] and let `$S\subseteq V$`. 

An element `$m\in S$` is called:


**maximal** in `$S$`  | no `$x\in S$` is [greater][bookofproofs$6190], formally `$\not\exists x\in S\; x\succ m$` 
:------------- |:-------------
 **minimal** in `$S$` | no `$x\in S$` is [smaller][bookofproofs$6190], formally `$\not\exists x\in S\; x\prec m$` 
 **maximum** of   **greatest** in) `$S$` | all `$x\in S$` are [smaller or equal][bookofproofs$6190], formally `$\forall x\in S\; x\preceq m$` 
 **minimum** of  **smallest** in) `$S$` | all `$x\in S$` are [greater or equal][bookofproofs$6190], formally `$\forall x\in S\; x\succeq m$` 

An element `$m\in V$` is called:

 **upper bound** of `$S$` | all `$x\in S$` are [smaller or equal][bookofproofs$6190], formally `$\forall x\in S\; x\preceq m$` 
 **lower bound** of `$S$` | all `$x\in S$` are [greater or equal][bookofproofs$6190], formally `$\forall x\in S\; x\succeq m$` 
 **supremum** of `$S$` | `$m$` is minimum of all upper bounds of `$S$`, formally `$m=\sup(S):=\min(\{n\in V\mid \forall x\in S\; x\preceq n\})$` 
 **infimum** of `$S$` | `$m$` is maximum of all lower bounds of `$S$`, formally `$m=\inf(S):=\max(\{n\in V\mid \forall x\in S\; x\succeq n\})$` 
