layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1800
orderid: 50
parentid: bookofproofs$1799
title: 
description:  Proof of URN MODEL WITH REPLACEMENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: and place them back,model,replacement,urn,proof
contributors: bookofproofs

---


---

According to the [probability of Laplace experiments][bookofproofs$975], we have to apply the formula

`\[p(A)=\frac{\text{# possible outcomes of }A}{\text{# possible outcomes of }\Omega}=\frac {|A|}{|\Omega|}.\quad\quad( * )\]`

Each outcome of the [Laplace experiment][bookofproofs$973] described in the urn model consists of drawing a ball `\(n\)` times, while each time there are `\(N\)` possible balls to be drawn. In order to better understand, what is happening in the experiment, imagine that the different symbols of an alphabet are written on the `\(N\)` balls in order to distinguish them. In this case, the outcome of such an experiment is a word from this alphabet, and there are exactly 

`\[|\Omega|=N^n\]`

[possible words (outcomes of drawing `\(n\)` letters from an alphabet of `\(N\)` symbols)][bookofproofs$996]. Now, among `\(n\)` such letters, the [binomial coefficient][bookofproofs$993] `\(\binom nk\)` gives us the number of ways of writing `\(k\)` letters in black ink (for a black ball drawn) and `\(n-k\)` letters in white ink (for a white ball drawn). In addition, the number of words of length `\(k\)`, which can be written in black ink from an alphabet with `\(M\)` symbols is `\(M^k\)` and the number of words of length `\(n-k\)`, which can be written in white ink from an alphabet with `\(N-M\)` symbols is `\((N-M)^{n-k}\)`. Thus, according to the [fundamental counting principle][bookofproofs$111], the number of outcomes of the event 

`\[A:=\{\text{"If we draw }n\text{ balls in total, then we draw exactly }k\text{ black balls."}\}\]`

is 
`\[|A|=\binom nk (M)^k(N-M)^{n-k}.\]`


It follows from `\(( * )\)` that

`\[p_k=p(A)=\binom nk \left(\frac MN\right)^k\left(1-\frac MN\right)^{n-k}.\]`
