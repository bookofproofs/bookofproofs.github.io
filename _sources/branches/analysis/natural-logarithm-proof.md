layout: proof
categories: branches,analysis
nodeid: bookofproofs$1600
orderid: 50
parentid: bookofproofs$1421
title: 
description:  Proof of NATURAL LOGARITHM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: natural logarithms,natural logarithm,logarithms,logarithm,proof
contributors: bookofproofs

---


---

Let `\(n\in\mathbb N\)`. From the [definition of the exponential function][bookofproofs$281], it follows that 

`\[\exp(n)=1+n+\frac {n^2}2+\ldots \ge 1+n.\quad \quad ( * )\]`

Due to the [reciprocity of exponential function][bookofproofs$1417], we get with `\( ( * ) \)` the approximation 

`\[\exp(-n)=\frac 1{\exp(n)}\le \frac 1{1+n}.\quad\quad ( * * )\]`

Since the [exponential function is strictly monotonically increasing][bookofproofs$1594] and  [is continuous][bookofproofs$1422], we can conclude from the [lemma about invertible functions][bookofproofs$1381] that the it is invertible on [closed real intervals][bookofproofs$1153] `\(\left[-n,n\right]\)`  for all `\(n\in\mathbb N\)`. Note that `\(\bigcup_{n\in\mathbb N}[-n,n]=\mathbb R\)`  and `\(\bigcup_{n\in\mathbb N}\left[\frac 1{n+1},n+1\right]=\mathbb R_+^*\)`, where `\(\mathbb R_+^*\)` denotes the set of [all positive real numbers][bookofproofs$1107]. Therefore, it follows that the  natural logarithm  
`\[\ln:\mathbb R_{+}^*\to\mathbb R\]`
is the inverse function of the exponential function and that it is also [continuous][bookofproofs$1260], [strictly monotonically increasing][bookofproofs$282].