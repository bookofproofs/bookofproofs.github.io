layout: explanation
categories: branches,logic
nodeid: bookofproofs$6882
orderid: 800
parentid: bookofproofs$184
title: What does WLOG mean?
description: WHAT DOES WLOG MEAN? &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: does,mean,what,wlog,what does wlog mean,w.l.o.g.,w.l.o.g
contributors: bookofproofs

---


---

Proving mathematical theorems becomes sometimes technically unnecessarily complicated if one tries to make too general assumptions in the proof. In order to avoid such technicalities, mathematicians quite often make restrictions on these assumptions and narrow the generality of their assumptions concentrating on some special cases, and making the whole proof easier to follow.

When restricting assumptions in mathematical proofs, mathematicians use the phrase __"without loss of generality"__, which sometimes is abbreviated by __WLOG__. What does this phrase mean?

It means that even though the restriction is being placed on one of the assumptions made in the proof, if one can complete the proof for this special case, then it would be very easy to give a proof for similar, but different special cases, exhausting all cases necessary to prove the general case.

For instance, imagine that the assumption for a proof is, that we are given some [real numbers][bookofproofs$1105] `$a,b\in\mathbb R$` such that `$a\neq b,$` and that it is easier to prove a theorem following from the inequality `$a\neq b$` that, in addition, we restrict this inequality to the special case `$a < b.$`  If the reasoning in the proof does not depend on this special case and works also for `$b < a$`, while exchanging the denotations `$a$` and `$b$` in the whole proof, mathematicians could begin their proof with the following phrases:

* Given some [real numbers][bookofproofs$1105] `$a,b\in\mathbb R$` such that `$a\neq b.$`
* Assume __without loss of generality__ (this could be abbreviated by "Assume WLOG") that `$a < b.$`
* (here comes the remainder of the proof).
