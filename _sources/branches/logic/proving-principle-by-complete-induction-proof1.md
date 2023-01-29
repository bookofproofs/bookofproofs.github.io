layout: proof
categories: branches,logic
nodeid: bookofproofs$658
orderid: 50
parentid: bookofproofs$657
title:
description: Proof of PROVING PRINCIPLE BY COMPLETE INDUCTION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$656
keywords: proving principle by induction,complete induction,proof by induction,inductive proof,proving principle by complete induction,proof
contributors: bookofproofs

---


---

* If we succeed to prove the [expression][bookofproofs$186] `$p(m)$` for the base case [natural number][bookofproofs$664] `$m\in\mathbb N,$` then `$p(m)$` becomes true.
* Following the [Peano axioms][bookofproofs$504], `$n+1$` is the successor of the natural number `$n$`.
* If we succeed to prove the induction step `$p(n)\Rightarrow p(n+1)$`, then it means that given `$p(n)$` is true for some `$n\ge m$`, then `$p(n+1)$` is also true for the successor `$n+1\ge m$`.
* By the same argument, it means that given `$p(n+1)$` is true for some `$n+1\ge m$`, then `$p(n+2)$` is also true for the successor `$n+2\ge m$`.
* By the same argument, it means that given `$p(n+2)$` is true for some `$n+2\ge m$`, then `$p(n+3)$` is also true for the successor `$n+3\ge m$`.
* By the same argument, ... etc..
* It follows that `$p(n)$` is true for all `$n\ge m.$`
* By the definition of a [valid logical argument][bookofproofs$7915], the proving principle by complete induction is valid, since the conclusion is true, if the (infintely many premisses, starting with the base case `$m$` and following the induction steps `$n\rightarrow n+1$` for all `$n\ge m$` are all true.
