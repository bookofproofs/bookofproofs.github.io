layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8036
orderid: 50
parentid: bookofproofs$8035
title: By Induction
description: PROOF OF CIRCULAR REFERENCES OF SELF-CONTAINED SETS ARE FORBIDDEN &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: are,circular,contained,forbidden,references,self,sets,proof
contributors: bookofproofs

---


---

We conduct a proof by [induction][bookofproofs$657].
### Base Case `$n=0$`

* We have to show that `$X_0\not\in X_0.$`
* By the [axiom of foundation][bookofproofs$717], the [singleton][bookofproofs$8034] `$\{X_0\}$` contains an element that is disjoint from itself. 
* This can only be the set `$X_0$`. 
* Since `$X_0\cap \{X_0\}=\emptyset$`, we have `$X_0\not\in X_0.$`

### Induction step `$n\rightarrow n+1$`

* By the base case there is no such chain which fulfills `$X_0\in X_1\in\ldots\in X_{n-1}\in X_n\in X_0.$`
* If a chain `$X_0\in X_1\in\ldots\in X_n\in X_{n+1}\in X_0$`  existed, then there would be a set `$X_{n+1}$` with `$X_{n+1}\in X_0$` and `$X_n\in X_{n+1}$`.
* Therefore, we cound replace `$X_n$` by `$X_{n+1}$` and get the chain `$X_0\in X_1\in\ldots\in X_{n-1}\in X_{n+1}\in X_0.$`
* But this is a [contradiction][bookofproofs$744] to the base case.
