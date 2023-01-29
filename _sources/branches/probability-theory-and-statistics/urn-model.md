layout: proposition
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1797
orderid: 1000
parentid: bookofproofs$93
title: Urn Model Without Replacement
description: URN MODEL WITHOUT REPLACEMENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: model,urn,without placing them back
contributors: bookofproofs

---


---

An **urn** contains `\(N\)` colored balls, thereof `\(M\)` black balls with `\(1\le M\le N\)`, and `\(N-M\)` white balls. All balls are well-mixed together. We draw randomly `\(n\)` balls (`\(n\le N\)`) from the urn, **without placing them back** in the urn. We observe the colors of all balls drawn. 

Assuming that drawing each ball is an elementary [Laplace experiment][bookofproofs$973], the probability `\(p_k\)` of the event

`\[A:=\{\text{"If we draw }n\text{ balls in total, then we draw exactly }k\text{ black balls."}\}\]`

obeys the equation

`\[p_k=p(A)=\frac{\binom Mk\binom {N-M}{n-k}}{\binom Nn}\]`
