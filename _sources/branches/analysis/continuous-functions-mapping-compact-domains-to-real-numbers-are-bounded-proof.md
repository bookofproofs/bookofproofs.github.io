layout: proof
categories: branches,analysis
nodeid: bookofproofs$6607
orderid: 50
parentid: bookofproofs$6606
title: 
description:  Proof of CONTINUOUS FUNCTIONS MAPPING COMPACT DOMAINS TO REAL NUMBERS ARE BOUNDED &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$582
keywords: are,bounded,compact,continuous,domains,functions,mapping,numbers,real,proof
contributors: bookofproofs

---


---

* Let `$X$` be a [metric spaces][bookofproofs$617].
* Let `$D\subset X$` be a [compact][bookofproofs$6575] [subset][bookofproofs$552].
* Let `$f:D\mapsto \mathbb R$` be a [continuous function][bookofproofs$1205] mapping the domain `$D$` to the [real numbers][bookofproofs$1105] `$\mathbb R$`. 
* We have to show that `$f$` is [bounded][bookofproofs$302].
   * According to the [corresponding theorem][bookofproofs$6604], there are points `\(p,q\in X\)`, for which the function `$f$` takes the [maximum][bookofproofs$6602] and the [maximum][bookofproofs$6603] value, i.e. `$f(p)=\max(f(D))$` and `$f(q)=\min(f(D))$`.
   * Take some real numbers `$P,Q\in\mathbb R$` with `$$Q\le f(q)\le f(x)\le f(p) \le P$$` for all `\(x\in D\)`.
   * It follows that `$P$` and `$Q$` are the [upper and the lower bounds][bookofproofs$584] of the [image][bookofproofs$592] `$f(D)$`, i.e. we have `$$ Q\le f(x) \le P$$` for all `$f(x)\in f(D)$`.
   * It follows from the [definition of bounded functions][bookofproofs$302] that `$f$` is bounded.
