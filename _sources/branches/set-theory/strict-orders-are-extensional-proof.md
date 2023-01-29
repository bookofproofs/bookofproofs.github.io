layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8078
orderid: 50
parentid: bookofproofs$8075
title: By Contradiction
description:  Proof of STRICT ORDERS ARE EXTENSIONAL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: are,extensional,orders,strict,proof
contributors: bookofproofs

---


---

* Let `$(X,\prec)$` be a [strictly ordered set][bookofproofs$7993].
* To see this, assume that for `$x,y\in X$` the following subsets are equal: `$\{z\mid z\prec x\}=\{z\mid z\prec y\}\quad ( * )$`.
* Further assume that the strict order "`$\prec$`" is not [extensional][bookofproofs$8059].
* This means that `$x\neq y.$`
* Therefore, we have either `$x\prec y$` or `$y\prec x$`.
* Therefore, we have either `$x\in \{z\mid z\prec y\}$` or `$y\in \{z\mid z\prec x\}$`.
* This means by `$( * )$` that either `$x\in \{z\mid z\prec x\}$` or `$y\in \{z\mid z\prec y\}$`.
* This means that either `$x\prec x$` or `$y\prec y$` which [contradicts][bookofproofs$744] the [irreflexivity][bookofproofs$575] of the strict order "`$\prec$`".
* Therefore, `$x=y$` and  "`$\prec$`" is [extensional][bookofproofs$8059].
