layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1818
orderid: 50
parentid: bookofproofs$450
title: 
description:  Proof of BINOMIAL DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: binomial,binomial distribution,distribution,proof
contributors: bookofproofs

---


---

Let `\(X\)` be the [random variable][bookofproofs$1813] counting the number `\(k\)` of the realizations of `\(A\)`. Because we repeat the experiment `\(n\)` times, each time the [event][bookofproofs$857] `\(A\)` will occur with the probability `\(p\)` and the [complement event][bookofproofs$861] `\(\overline{A}\)` will occur with the probability `\(1-p\)`. Imagine, in the first `\(k\)` repetitions, we observe only `\(A\)`, while in the remaining `\(n-k\)` repetitions we observe only `\(\overline{A}\)`. Then the joint event will be

`\[\underbrace{A,\ldots,A}_{k\text{ times}}\underbrace{\overline{A},\ldots,\overline{A}}_{n-k\text{ times}}.\quad\quad ( * )\]`

Because we conduct a [Bernoulli experiment][bookofproofs$1812], all repetitions are [mutually independent][bookofproofs$1808]. Therefore, their joint probability of observing exactly `\(( * )\)` is the product of all probabilities of each realization, which gives us the formula

`\[p^k(1-p)^{n-k},\quad\quad 0\le k\le n.\]`

Because the [binomial coefficient][bookofproofs$993] `\(\binom nk\)` is the number of possible words of length `\(n\)` with `\(k\)` letters `\(A\)` and `\(n-k\)` letters `\(\overline{A}\)`, in which the order of letters does not play any role, the joint probability of observing exactly `\(k\)` times the event `\(A\)` is given by

`\[p(X=k)=\binom nk p^k(1-p)^{n-k},\quad\quad 0\le k\le n.\]`

For all other real numbers `\(k\)`, we have the `\(p(X=k)=0\)`. Therefore, the [probability mass function][bookofproofs$1824] is 

`\[p(X = k)=\begin{cases}
\binom nk p^k(1-p)^{n-k}&\text{for }k=0,1,\ldots n\\\\
0&\text{else.}\end{cases}\]`


It follows that the [probability distribution][bookofproofs$1815] of the random variable `\(X\)` is given by

`\[\begin{array}{rcll}
p(X \le x)&=&0&\text{for }x < 0\\
p(X \le x)&=&\sum_{k=0}^{k=x}\binom nk p^k(1-p)^{n-k}&\text{for }0\le x < n\\
p(X \le x)&=&1&\text{for }x \ge n\\
\end{array}\]`
