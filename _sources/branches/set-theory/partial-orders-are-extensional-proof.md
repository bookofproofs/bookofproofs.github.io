layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8077
orderid: 50
parentid: bookofproofs$8074
title: By Contradiction
description:  Proof of PARTIAL ORDERS ARE EXTENSIONAL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: are,extensional,orders,partial,proof
contributors: bookofproofs

---


---

* Let `$(X,\preceq )$` be a [poset][bookofproofs$576].
* Assume that for `$x,y\in X$` the following subsets of a given  are equal: `$\{z\mid z\preceq x\}=\{z\mid z\preceq y\}\quad( * ).$`
* Assume that the [partial order][bookofproofs$576] "`$\preceq$`" is not [extensional][bookofproofs$8059].
* This means that `$x\neq y.$`
* Therefore, we have either `$x\npreceq y$` or `$y\npreceq x.$`
* Therefore, we have either `$x\not\in \{z\mid z\preceq y\}$` or `$y\not\in \{z\mid z\preceq x\}.$`
* This means by `$( * )$` that either `$x\not\in \{z\mid z\preceq x\}$` or `$y\not\in \{z\mid z\preceq y\}.$`
* This means that either `$x\npreceq x$` or `$y\npreceq y.$`
* But this [contradicts][bookofproofs$744] the [reflexivity][bookofproofs$572] of the partial order `$"\preceq".$`
* Therefore, `$x=y$` and "`$\preceq$`" is [extensional][bookofproofs$8059].