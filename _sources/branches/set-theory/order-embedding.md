layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8083
orderid: 1400
parentid: bookofproofs$189
title: Order Embedding
description: ORDER EMBEDDING &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979
keywords: embedding,order,order embedding
contributors: bookofproofs

---
When comparing ordered sets among each other, it is sometimes necessary to decide if their orders are similar or in essence "the same" kind of orders. The following definition states more precisely what is meant by that.

---

Let `$(X,\preceq)$` and `$(Y,\preccurlyeq)$` be two [posets][bookofproofs$576], [chains][bookofproofs$6191] or [strictly ordered sets][bookofproofs$7993]. An **order embedding** is an [injective function][bookofproofs$592] `$f:X\to Y$` with the property `$a\preceq b$` if and only if `$f(a)\preccurlyeq f(b)$` for all `$a,b\in X.$`

### Note

The concept of an order embedding is a generalization of a [monotonic function][bookofproofs$282] known from [analysis][bookofproofs$47]. Please also note that `$f$` must be injective. Otherwise, `$f(a)=f(b)$` could be possible, even if `$a\neq b,$` in contradiction to the definition of an order embedding.
