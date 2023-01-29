layout: proof
categories: branches,logic
nodeid: bookofproofs$6847
orderid: 50
parentid: bookofproofs$6846
title: 
description:  Proof of ASSOCIATIVITY OF DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711
keywords: associativity,disjunction,proof
contributors: bookofproofs


---


---

* Let `$x,y,z$` be [propositions][bookofproofs$1307] and let  `$I$` be an [interpretation][bookofproofs$710] with the [valuation function][bookofproofs$710] `$[[]]_I$`.
* Based on the [truth table of disjunction][bookofproofs$713], we can construct a truth table for `$(x\vee y) \vee z$` and `$x\vee (y \vee z)$` independently for all possible semantics of `$x,y,z$`:


`$[[x]]_I$`  | `$[[y]]_I$`  | `$[[z]]_I$`  | `$[[x \vee y]]_I$` | `$[[y \vee z]]_I$` | `$[[(x \vee y)\vee z]]_I$` | `$[[x\vee (y \vee z)]]_I$`
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
 `$1$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$1$`| `$0$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$0$`| `$1$`| `$0$`| `$1$`| `$1$`| `$1$`
 `$1$`| `$1$`| `$0$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$0$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$1$`| `$0$`| `$0$`| `$1$`| `$0$`| `$1$`| `$1$`
 `$0$`| `$0$`| `$0$`| `$0$`| `$0$`| `$0$`| `$0$`

* Since the values in both columns to the right of the table are equal, it follows that the [disjunction][bookofproofs$713] operation is [associative][bookofproofs$668], i.e. `$(x\vee y) \vee z =x\vee (y \vee z)$`.
