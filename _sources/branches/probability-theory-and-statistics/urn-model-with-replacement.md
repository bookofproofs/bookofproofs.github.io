layout: proposition
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1799
orderid: 1100
parentid: bookofproofs$93
title: Urn Model With Replacement
description: URN MODEL WITH REPLACEMENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: and place them back,model,replacement,urn
contributors: bookofproofs

---


---

An **urn** contains `\(N\)` colored balls, thereof `\(M\)` black balls with `\(1\le M\le N\)`, and `\(N-M\)` white balls. All balls are well-mixed together. We draw randomly `\(n\)` balls (`\(n\le N\)`) from the urn, **and place them back** in the urn. We observe the colors of all balls drawn. 

Assuming that drawing each ball is an elementary [Laplace experiment][bookofproofs$973], the probability `\(p_k\)` of the event

`\[A:=\{\text{"If we draw }n\text{ balls in total, then we draw exactly }k\text{ black balls."}\}\]`

obeys the equation

`\[p_k=p(A)=\binom nk \left(\frac MN\right)^k\left(1-\frac MN\right)^{n-k}.\]`
