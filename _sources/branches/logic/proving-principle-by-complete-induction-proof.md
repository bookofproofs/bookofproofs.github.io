layout: proof
categories: branches,logic
nodeid: bookofproofs$8636
orderid: 50
parentid: bookofproofs$657
title: By Induction
description: PROOF OF THE PROVING PRINCIPLE BY COMPLETE INDUCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8635
keywords: proving principle by induction,complete induction,proof by induction,inductive proof,proving principle by complete induction,proof
contributors: bookofproofs

---


---

The following proof does without the Peano axioms. Instead, it uses the [well-ordering principle][bookofproofs$698] of [set-theoretical definition of natural numbers][bookofproofs$718].
* Let a premise `$p(n)$` be given which can be proven by the principle of complete induction to be [true][bookofproofs$707] for all natural numbers `$n\ge m,$` given some base case natural number `$m.$`
* Assume, the [set][bookofproofs$550] `$N$` of all [natural numbers][bookofproofs$718] `$k\ge m,$` for which the premise `$p(k)$` is [false][bookofproofs$707] is not empty, `$N\neq\emptyset.$`
* Because of the [well-ordering principle][bookofproofs$698], `$N$` contains a [minimum][bookofproofs$7995] `$k_0.$`
* But then `$p(m)$` was true for all `$m < k_0,$` which is a [contradiction][bookofproofs$744] to the minimality of `$k_0.$`
