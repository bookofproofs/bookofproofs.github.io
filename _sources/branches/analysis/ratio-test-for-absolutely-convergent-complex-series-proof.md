layout: proof
categories: branches,analysis
nodeid: bookofproofs$1730
orderid: 50
parentid: bookofproofs$1729
title: By Induction
description:  Proof of RATIO TEST FOR ABSOLUTELY CONVERGENT COMPLEX SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: absolutely,complex,convergent,ratio,series,test,proof
contributors: bookofproofs

---


---

Note that changing a [finite number][bookofproofs$985] of the sequence members of any [infinite complex series][bookofproofs$1724] `\(\sum_{k=0}^\infty a_k\)` does not change its convergence behavior. Therefore, by changing the first `\(K\)` (if any) sequence members `\(a_k\)`, we can assume that 

1. `\(a_k\neq 0\)` for all `\(k \in\mathbb N\)` (i.e. all sequence members `\(a_k\)` are different from [complex zero][bookofproofs$1662] `\(0\)`),
1. there exists a [real number][bookofproofs$1105] `\(\theta\)` with `\(0 < \theta < 1\)` such that `\(\left|\frac{a_{k+1}}{a_k}\right|\le \theta\)` for all `\(k \in \mathbb N.\)`

It follows from the [proving principle by induction][bookofproofs$657] that (base case)
`\[|a_1|\le |a_0|\theta^0=|a_0|\cdot 1,\]`
and that (induction step), given `\(|a_k|\le |a_0|\theta^{k-1},\)`
`\[|a_{k+1}|\le |a_k|\cdot \theta\le  |a_0|\theta^{k}.\]` 

From this result, it follows that the series `\(\sum_{k=0}^\infty |a_0|\theta^{k}\)` is a majorant of the series `\(\sum_{k=0}^\infty a_k\)`. Due to the [convergence of the infinite geometric series][bookofproofs$1353].
`\[\sum_{k=0}^\infty |a_0|\theta^{k}=|a_0|\sum_{k=0}^\infty \theta^{k}=\frac{|a_0|}{1-\theta}\]`
it follows from the [majorant criterion for complex series][bookofproofs$1727] that  `\(\sum_{k=0}^\infty a_k\)` is an [absolutely convergent complex series][bookofproofs$1725].