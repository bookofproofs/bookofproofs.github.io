layout: proof
categories: branches,analysis
nodeid: bookofproofs$1269
orderid: 50
parentid: bookofproofs$1268
title: 
description:  Proof of CONVERGENCE BEHAVIOUR OF ABSOLUTELY CONVERGENT SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: absolutely,behaviour,convergence,convergent,series,proof
contributors: bookofproofs

---


---

### Proof "absolute convergent" `$\Rightarrow$` "convergent"

Let `\(\sum_{k=0}^\infty x_k\)` be an [absolutely convergent series][bookofproofs$198]. Since, be definition, `\(\sum_{k=0}^\infty |x_k|\)` is [convergent][bookofproofs$175], we can apply [Cauchy's general criterion for convergent series][bookofproofs$1148] and conclude that for every `\(\epsilon  > 0\)` there is an index `\(N(\epsilon)\in\mathbb N\)` such that

`\[\left|\sum_{k=m}^n |x_k|\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

According to the [triangle inequality][bookofproofs$588], we have that


`\[\left|\sum_{k=m}^n x_k\right| \le \left|\sum_{k=m}^n |x_k|\right| < \epsilon\quad\quad \text{for all}\quad n\ge m\ge N(\epsilon).\]`

Applying [Cauchy's general criterion for convergent series][bookofproofs$1148] once again, we get that the series `\(\sum_{k=0}^\infty x_k\)` is [convergent][bookofproofs$175] (in the usual sense).

### Proof "convergent" `$\not\Rightarrow$` "absolute convergent"

(to be done: got the proof - become a co-author?)
