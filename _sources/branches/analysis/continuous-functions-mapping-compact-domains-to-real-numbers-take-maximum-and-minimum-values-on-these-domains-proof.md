layout: proof
categories: branches,analysis
nodeid: bookofproofs$6605
orderid: 50
parentid: bookofproofs$6604
title: 
description:  Proof of CONTINUOUS FUNCTIONS MAPPING COMPACT DOMAINS TO REAL NUMBERS TAKE MAXIMUM AND MINIMUM VALUES ON THESE DOMAINS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$582
keywords: compact,continuous,domains,functions,mapping,maximum,minimum,numbers,real,take,these,values,proof
contributors: bookofproofs

---


---

* Let `$X$` be a [metric spaces][bookofproofs$617].
* Let `$D\subset X$` be a [compact][bookofproofs$6575] [subset][bookofproofs$552].
* Let `$f:D\mapsto \mathbb R$` be a [continuous function][bookofproofs$1205] mapping the domain `$D$` to the [real numbers][bookofproofs$1105] `$\mathbb R$`. 
* We have to show that there are points `\(p,q\in X\)`, for which the function `$f$` takes the [maximum][bookofproofs$6602] and the [maximum][bookofproofs$6603] values of the image `$f(D)$`, i.e. `$f(p)=\max(f(D))$` and `$f(q)=\min(f(D)).$`
   * Since `$f$` is [continuous][bookofproofs$1205] and `\(D\subset X\)` is [compact][bookofproofs$6575] by hypothesis, and since [real numbers form a metric space][bookofproofs$618], the [image][bookofproofs$592] `\(f( D)\subset \mathbb R\)`, is also compact, according to the [corresponding proposition][bookofproofs$143].
   * Because [compact subsets of real numbers contain their maxima and minima][bookofproofs$6598], it follows that `$\max(f(D))\in f(D)$` and `$\min(f(D))\in f(D)$`.
   * Therefore, the [fibers][bookofproofs$592] `$P:=f^{-1}(\max(f(D)))$` and `$Q:=f^{-1}(\min(f(D)))$` are not-empty [subsets][bookofproofs$552] `$P\subseteq X$` and `$Q\subseteq X$`.
   * It follows that `\(p,q\in X\)` exist.
