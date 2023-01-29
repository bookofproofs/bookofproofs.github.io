layout: proposition
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$481
orderid: 600
parentid: bookofproofs$324
title: Multinomial Distribution
description: MULTINOMIAL DISTRIBUTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: distribution,multinomial,multinomial distribution
contributors: bookofproofs

---


---

Consider a [random experiment][bookofproofs$857] repeated `\(n\)` times, in which only one of the [collectively exhaustive and mutually exclusive events][bookofproofs$859] `\(A_1,A_2,\ldots,A_r\)` can occur. Assume that all repetitions are [mutually independent][bookofproofs$1808]. Furthermore, assume, in each repetition the event `\(A_i\)` can occur with the constant probability `\(p_i:=p(A_i)\)` for `\(i=1,\ldots,r\)`. Let `\(X_1,\ldots,X_r\)` be [random variables][bookofproofs$1813] counting the numbers `\(k_i\)` of the realizations of each event `\(A_i\)`, `\(i=1,\ldots,r\)`. Clearly, we have `\(k_i\ge 0\)` for and `\(k_1+k_2+\ldots+k_r=n\)`.

The probability of the event that we will observe the event `\(S_{k_1k_2\ldots k_r}\)` defined by 
`\[S_{k_1k_2\ldots k_r}:=\cases{A_1&\text{occurred }k_1\text{ times}\\\vdots\\A_r&\text{occurred }k_r\text{ times}\\}\]`

 is given by

`\[p(S_{k_1k_2\ldots k_r})=\binom {n}{k_1,k_2,\ldots,k_r}p_1^{k_1}p_2^{k_2}\ldots p_r^{k_r}.\quad\quad ( * )\]`

Therefore, the [probability mass function][bookofproofs$1824] of all random variables is given by

`\[p(X_1=k_1,\ldots,X_r=k_r)=\cases{\binom {n}{k_1,k_2,\ldots,k_r}p_1^{k_1}p_2^{k_2}\ldots p_r^{k_r}&\text{if } k_1+k_2+\ldots+k_r=n\\
0&\text{else}.}\]`

Because the probabilities `\(( * )\)` can be retrieved from the expansion of the [multinomial theorem][bookofproofs$1822].
`\[1=(p_1 + p_2 + \ldots + p_r)^n=\sum_{\substack{k_1+\ldots+k_r=n \\ k_1,\ldots,k_r}}\binom{n}{k_1,k_2\ldots,k_r}p_1^{k_1} p_2^{k_2}\ldots p_r^{k_r}.\]`

this kind of a distribution is called a **multinomial distribution**.
