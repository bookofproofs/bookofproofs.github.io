layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8544
orderid: 50
parentid: bookofproofs$8543
title: By Induction
description: PROOF OF CARTESIAN PRODUCTS OF COUNTABLE SETS IS COUNTABLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8311
keywords: cartesian product is countable,countable cartesian product,proof
contributors: bookofproofs

---


---

* By hypothesis, `$A_1,\ldots,A_n$` are [countable sets][bookofproofs$772] and `$A=A_1\times\ldots\times A_n$` is their [Cartesian product][bookofproofs$748].
* We prove [by induction][bookofproofs$657] that `$A$` is countable.
* Base Case `$n=2$`
   * ... is correct, since `$$A_1\times A_2=\bigcup_{a\in A_2}(A_1\times a)$$` and the [union of countably many countable sets is countable][bookofproofs$796].
* Induction step `$n\to n+1$`
   * Assume `$A_{n+1}$` is countable.
   * Then, `$$A_1\times \ldots\times A_n\times A_{n+1}=\left(\bigcup_{a\in A_{n+1}}(A_1\times \ldots\times A_n)\times a\right).$$` 
   * By induction hypothesis, `$A_1\times \ldots\times A_n$`  is countable.
   * Apply [union of countably many countable sets is countable][bookofproofs$796] once again.
