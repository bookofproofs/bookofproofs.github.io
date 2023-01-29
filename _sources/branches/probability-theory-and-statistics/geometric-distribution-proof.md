layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1827
orderid: 50
parentid: bookofproofs$429
title: 
description:  Proof of GEOMETRIC DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: distribution,geometric,geometric distribution,proof
contributors: bookofproofs

---


---

In a [Bernoulli experiment][bookofproofs$1812], let `\(X\)` be the [random variable][bookofproofs$1813] having the realization `\(k\)`, if and only if we observe the [event][bookofproofs$857] `\(A\)` for the first time at the `\(k\)`-th repetition of the experiment. The joint event `\(X=k\)` is given by

`\[B_k:=(\underbrace{\overline{A},\ldots,\overline{A}}_{k-1\text{ times}},A).\]`

Thus, `\(B_k\)` is the event of observing `\(k-1\)` times the complement event `\(\overline{A}\)` and observing the event `\(A\)` at the  `\(k\)`-th repetition. By hypothesis, the probability of observing `\(A\)` in each repetition is `\(p:=p(A)\)` and all repetitions are mutually independent. Therefore, the  [probability mass function][bookofproofs$1824] is given by 


`\[p(B_k)=p(X = k)=\begin{cases}
p(1-p)^{k-1}&\text{for }k=1,2,3,\ldots \\\\
0&\text{else.}\end{cases}\quad\quad ( * )\]`

The geometric distribution (i.e. the [probability distribution][bookofproofs$1815] of the random variable `\(X\)`) is given by

`\[\begin{array}{rcll}
p(X \le x)&=&0&\text{for }x < 1\\
p(X \le x)&=&\sum_{k=1}^{k=x}p(1-p)^{k-1}&\text{for }1\le x 
\end{array}\]`

We have the following cases:

### Case `\(p=0\)`

Then we have `\(p(B_k)=0\)` for all `\(k\ge 1\)`.

### Case `\(p=1\)`

It follows from `\( ( * )\)` that `\(p(B_1)=1\)`, and `\(p(B_k)=0\)` for all `\(k\ge 2\)`.

### Case `\(0 < p < 1\)`

Note that the probabilities `\(p(B_k)\)` are all positive, i.e. all mutually exclusive events `\(B_1,B_2,B_3,\ldots\)` can occur. On the other hand, it can happen that we will observe neither `\(B_1\)`, nor `\(B_2\)`, nor `\(B_3\)`, etc., for (in an extreme case) infinitely many times.

In this extreme case, the event 

`\[\bigcup_{k=1}^\infty B_k\]`  

has the probability following (among others) from [geometric progression][bookofproofs$1353] and the [convergence behavior][bookofproofs$1347] of the sequence `\((x^n)_{n\in\mathbb N}\)` for `\(|x| < 1\)`:

`\[\begin{array}{rcll}
p(\bigcup_{k=1}^\infty B_k)&=&\sum_{k=1}^\infty p(B_k)&\text{mutually exclusive events}\\
&=&\lim_{n\to\infty}\sum_{k=1}^n p(B_k)&\text{definition of infinite series}\\
&=&\lim_{n\to\infty}\sum_{k=1}^n p(1-p)^{k-1}&\text{by }( * )\\
&=&\lim_{n\to\infty}p\sum_{k=1}^n (1-p)^{k-1}&\text{distributivity law for real numbers}\\
&=&\lim_{n\to\infty}p\sum_{k=0}^{n-1} (1-p)^{k}&\text{change of summing index}\\
&=&\lim_{n\to\infty}p\frac{1-(1-p)^n}{1-(1-p)}&\text{geometric progression}\\
&=&\lim_{n\to\infty}p\frac{1-(1-p)^n}{p}&\text{distributivity law for real numbers}\\
&=&\lim_{n\to\infty}1-(1-p)^n&\text{cancelling }p\\
&=&1-0&\text{convergence of }(x^n)\text{ for }|x| < 1\\
&=&1
\end{array}\]`
