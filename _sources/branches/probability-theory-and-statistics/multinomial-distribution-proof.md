layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1826
orderid: 50
parentid: bookofproofs$481
title: 
description:  Proof of MULTINOMIAL DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: distribution,multinomial,multinomial distribution,proof
contributors: bookofproofs

---


---

Imagine, during the `\(n\)` repetitions we first observe `\(k_1\)` realizations of the event `\(A_1\)`, next we observe  `\(k_2\)` realizations of the event `\(A_2\)`, etc. and at the end we observe `\(k_r\)` realizations of the event `\(A_r\)`. Then we will observe the joint event of the ordered occurrence of the realizations

`\[C=(\underbrace{A_1,\ldots,A_1}_{k_1\text{ times}},\underbrace{A_2,\ldots,A_2}_{k_2\text{ times}},\ldots,\underbrace{A_r,\ldots,A_r}_{k_r\text{ times}}).\]`

Clearly, we have `\(k_i\ge 0\)` for and `\(k_1+k_2+\ldots+k_r=n\)`. Because all repetitions of the [random experiment][bookofproofs$857] are [mutually independent][bookofproofs$1808] by hypothesis, we have for the probability of `\(C\)`:

`\[p(C )=p(A_1)^{k_1}p(A_2)^{k_2}\ldots p(A_r)^{k_r}.\]`

Now, without taking into account the order of observed realizations of events `\(A_i\)`, we define the event `\(S_{k_1k_2\ldots k_r}\)` by 
`\[S_{k_1k_2\ldots k_r}:=\cases{A_1&\text{occurred }k_1\text{ times}\\\vdots\\A_r&\text{occurred }k_r\text{ times}\\}\]`

`\(S_{k_1k_2\ldots k_r}\)` can be retrieved from `\(C\)` by rearranging the order of its realizations, while the probability of each rearrangement does not change. The number of such rearrangements is given by the [multinomial coefficient][bookofproofs$1819]. Thus, we have 

`\[p(S_{k_1k_2\ldots k_r})=\binom {n}{k_1,k_2,\ldots,k_r}p_1^{k_1}p_2^{k_2}\ldots p_r^{k_r}.\]`

Therefore, the [probability mass function][bookofproofs$1824] of all random variables is given by

`\[p(X_1=k_1,\ldots,X_r=k_r)=\cases{\binom {n}{k_1,k_2,\ldots,k_r}p_1^{k_1}p_2^{k_2}\ldots p_r^{k_r}&\text{if } k_1+k_2+\ldots+k_r=n\\
0&\text{else},}\]`

where `\(X_1,\ldots,X_r\)` are [random variables][bookofproofs$1813] counting the numbers `\(k_i\)` of the realizations of each event `\(A_i\)`, `\(i=1,\ldots,r\)`.

Because all events `\(A_1,A_2,\ldots,A_r\)` are [collectively exhaustive and mutually exclusive events][bookofproofs$859], we have

`\[A_1\cup A_2\cup\ldots\cup A_r=\Omega.\]`

Therefore, it follows from the [multinomial theorem][bookofproofs$1822].
`\[p(\Omega)=1=(p_1 + p_2 + \ldots + p_r)^n=\sum_{\substack{k_1+\ldots+k_r=n \\ k_1,\ldots,k_r}}\binom{n}{k_1,k_2\ldots,k_r}p_1^{k_1} p_2^{k_2}\ldots p_r^{k_r}.\]`
