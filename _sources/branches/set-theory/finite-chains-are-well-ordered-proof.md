layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8001
orderid: 50
parentid: bookofproofs$8000
title: 
description:  Proof of FINITE CHAINS ARE WELL-ORDERED &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979
keywords: are,chains,finite,ordered,well,proof
contributors: bookofproofs

---


---

* Suppose,  `$(V,\preceq )$`  is a finite [chain][bookofproofs$6191] and let `$S\subseteq V$`  be a non-empty, finite [subset][bookofproofs$552] of  `$V$`.
* By definition of a chain,  "`$\preceq$`"  is a [total order][bookofproofs$6191], which means that it is, in particular, [connex][bookofproofs$1308].
* If  `$x_0\in S$`  is the only element of  `$S$`, then  `$x_0$`  is its [minimum][bookofproofs$7995] and we are done. Therefore, suppose  `$S$`  has at least two elements.
* Since "`$\preceq$`" is connex, for any given  `$x\in S$` with  `$x\neq x_0$`  we have  `$x_0\preceq x$`  or  `$x\preceq x_0.$`
* Therefore, either  `$x_0$`  is a minimum of `$S$` or there is a smaller element  `$x_1\in S$`  with  `$x_1\preceq x_0.$`
* By the same argument, either  `$x_1$`  is a minimum of `$S$` or there is a [smaller][bookofproofs$6190] element  `$x_2\in S$`  with  `$x_2\preceq x_1.$`
* Since `$S$` is [finite][bookofproofs$985], this chain of arguments has to terminate at some `$x_i,$`  `$i\ge 0$`  which is the minimum of `$S.$`
* Therefore, `$V$` is [well-ordered][bookofproofs$7997], by definition.
