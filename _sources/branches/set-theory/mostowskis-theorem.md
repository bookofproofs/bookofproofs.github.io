layout: theorem
categories: branches,set-theory
nodeid: bookofproofs$8085
orderid: 400
parentid: bookofproofs$8079
title: Mostowski's Theorem
description: MOSTOWSKI'S THEOREM &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: mostowskis,theorem
contributors: bookofproofs


---
The observations made above about the [Mostowski function][bookofproofs$8079] and [their relation to transitive sets][bookofproofs$726] as well as [their relation to order embeddings][bookofproofs$8084] could be valid only for the shown examples, but not in general. Therefore, we want to summarize these observations in a theorem and prove that indeed the observations hold also in every case. This _theorem_ was first proven by [Mostowski][mo] (1913 - 1975).

[mo][https://mathshistory.st-andrews.ac.uk/Biographies/Mostowski/]
---

Let `$U$` be a [universal set][bookofproofs$7984], `$(V,\prec)$` with a [well-founded][bookofproofs$8058] relation "`$\prec$`".

Then the corresponding [Mostowski function][bookofproofs$8079] defined by `$\pi(x):=\{\pi(y)\mid y\in V\wedge y\prec x\}$` exists and its [Mostowski collapse][bookofproofs$8079] `$\pi[V]\subseteq U$` is a [transitive set][bookofproofs$720].
Moreover, if "`$\prec$`" is, in addition, [extensional][bookofproofs$8059], then the function `$\pi$` is an [order embedding][bookofproofs$8083], i.e. it fulfills the property `$x\prec y\Longleftrightarrow \pi(x)\in\pi(y).$`
