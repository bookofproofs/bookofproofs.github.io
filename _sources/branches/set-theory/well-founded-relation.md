layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8058
orderid: 500
parentid: bookofproofs$112
title: Well-founded Relation
description: WELL-FOUNDED RELATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: founded,relation,well
contributors: bookofproofs

---
The following definition is a generalization of the concept of [minimal][bookofproofs$7995] elements in a set and of a [well-order][bookofproofs$7997].
---

Let `$V$` be a [set][bookofproofs$550], and let `$R\subseteq V\times V$` be a binary [relation][bookofproofs$571]. The relation `$R$` is called *well-founded* if every non-empty subset `$S\subseteq V$` contains a [minimal][bookofproofs$7995] element `$m$` with respect to `$R$`. In other words, no element `$x\in S$` is in the left-sided relation `$xRm.$` Formally:

`$$\forall S\subseteq V\; \exists x\in S \Rightarrow \exists m\in S \quad \forall x\in S \quad (x,m)\not\in R.$$`
