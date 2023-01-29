layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8088
orderid: 50
parentid: bookofproofs$8087
title: 
description:  Proof of STRICTLY, WELL-ORDERED SETS AND TRANSITIVE SETS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8055
keywords: ordered,sets,strictly,transitive,well,proof
contributors: bookofproofs

---


---

* Let `$(V,\prec)$` be a [strictly-ordered set][bookofproofs$7993], which is a [well-order][bookofproofs$7997].
* By definition "`$\prec$`" is [well-founded][bookofproofs$8058].
* Moreover, we have already shown that every [strict order is extensional][bookofproofs$8075], therefore "`$\prec$`" is [extensional][bookofproofs$8059].
* Since "`$\prec$`" is both, well-founded and extensional, we can apply the [Mostowski's theorem][bookofproofs$8085] which ensures the existence of a [transitive set][bookofproofs$720] `$X:=\pi[V],$` where `$\pi[V]$` is the [Mostowski collapse][bookofproofs$8079] of the [Mostowski function][bookofproofs$8079] `$\pi:V\to X$` defined by `$$\pi(x):=\{\pi(y)\mid y\in V\wedge y\prec x\}.$$` Moreover, `$\pi$` is [injective][bookofproofs$769] and fulfills the property `$$u\prec v\Longleftrightarrow \pi(u)\in_X\pi(v).$$` 
* Therefore, `$\pi$` is an [order embedding][bookofproofs$8083] between `$(V,\prec)$` and `$(X,\in_X).$`
* Thus, `$(X,\in_X)$` is also a strictly-ordered set which is well-ordered with respect to the [contained relation][bookofproofs$8066] `$\in_X.$`
