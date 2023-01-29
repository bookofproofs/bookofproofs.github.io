layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8682
orderid: 50
parentid: bookofproofs$8681
title: 
description: PROOF OF TRANSITIVE RECURSION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8635
keywords: transitive recursion,transitive recursions,proof
contributors: bookofproofs

---


---

* By hypothesis, `$X$` is a [set][bookofproofs$550] and `$\Omega$` is the proper [class of all ordinals][bookofproofs$8091] and `$\omega\in\Omega$` is a given [ordinal number][bookofproofs$723].
* It is sufficient to show that the [function][bookofproofs$592] `$f:\mathbb \Omega\to X$` defined by specifying the value of `$f(\alpha)$` for all `$\alpha\subseteq \omega$` and for all `$\beta\supset\omega$` with a **recursion formula** `$f(\beta)=\mathcal R(f(\alpha)\mid \alpha \subset\beta)$` is well-defined (i.e. unique) for all [ordinal numbers][bookofproofs$723].
* Assume, `$f$` defined like this is not well-defined for some ordinal numbers.
   * Since [ordinal numbers][bookofproofs$723] are [well-ordered][bookofproofs$7997], there is the smallest ordinal number `$\omega_0\in\mathbb \Omega$` for which `$f$` is not well-defined.
   * But then for `$\alpha \subset \omega_0$` the values `$f(\alpha)$` are well-defined and `$f(\omega_0)=\mathcal R(f(\alpha)\mid \alpha \subset \omega_0).$`
   * This is a [contradiction][bookofproofs$744].
* Therefore, `$f$` is well-defined for all [ordinal numbers][bookofproofs$723].