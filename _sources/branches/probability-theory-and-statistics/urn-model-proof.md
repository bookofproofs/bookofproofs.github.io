layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1798
orderid: 50
parentid: bookofproofs$1797
title: 
description:  Proof of URN MODEL WITHOUT REPLACEMENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: model,urn,without placing them back,proof
contributors: bookofproofs

---


---

According to the [probability of Laplace experiments][bookofproofs$975], we have to apply the formula

`\[p(A)=\frac{\text{# possible outcomes of }A}{\text{# possible outcomes of }\Omega}=\frac {|A|}{|\Omega|}.\quad\quad( * )\]`

Each outcome of the [Laplace experiment][bookofproofs$973] described in the urn model consists of `\(n\)` balls drawn from `\(N\)` balls, while the the order of balls drawn does not play any role. Therefore, the number of possible outcomes is given by the [binomial coefficient][bookofproofs$993].
`\[|\Omega|=\binom Nn.\]`

Similarly, the number of possible ways of drawing `\(k\)` black balls out of `\(M\)` black balls is given by `\(\binom Mk\)`. For each sample of `\(k\)` black balls chosen that way, there are `\(\binom {N-M}{n-k}\)` possible ways of drawing `\(n-k\)` white balls out of `\(N-M\)` white balls. Thus, according to the [fundamental counting principle][bookofproofs$111], the number of possible ways of drawing `\(k\)` black balls out of `\(M\)` black balls and, at the same time, drawing `\(n-k\)` white balls out of `\(N-M\)` white balls is given by

`\[|A|=\binom Mk\binom {N-M}{n-k}.\]`


It follows from `\(( * )\)` that

`\[p_k=p(A)=\frac{\binom Mk\binom {N-M}{n-k}}{\binom Nn}.\]`
