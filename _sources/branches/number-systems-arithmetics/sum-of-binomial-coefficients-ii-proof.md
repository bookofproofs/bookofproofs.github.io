layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1844
orderid: 50
parentid: bookofproofs$1843
title: 
description:  Proof of SUM OF BINOMIAL COEFFICIENTS II &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: binomial,coefficients,sum,proof
contributors: bookofproofs

---


---

Let `\(x\)` be an element of a [ring][bookofproofs$683] `\(x\in(R,+,\cdot) \)` and let `\(n\ge 1\)` be a [natural number][bookofproofs$718]. In the following calculation, we use the following mathematical concepts and theorems: 
* a [binomial identity for `\(k\)` times `\(n\)` choose `\(k\)` ][bookofproofs$1839],
* some [rules of calculation in a ring][bookofproofs$683], and
* the [sum of binomial coefficients (i) ][bookofproofs$1841]: 

`\[
\begin{array}{rcll}
\sum_{k=0}^nk\binom nk(1-x)^{n-k}x^k&=&\sum_{k=1}^nk\binom nk(1-x)^{n-k}x^k&\text{first summand can be ignored (multiplication by 0)}\\
&=&\sum_{k=1}^nn\binom{n-1}{k-1}(1-x)^{n-k}x^k&\text{binomial identity for k times n choose k}\\
&=&n\sum_{k=1}^n\binom{n-1}{k-1}(1-x)^{n-k}x^k&\text{distributivity law in the ring }R\\
&=&n\sum_{k=0}^{n-1}\binom{n-1}{k}(1-x)^{(n-1)-k}x^{k+1}&\text{change of summation index }k\to k-1\\
&=&nx\sum_{k=0}^{n-1}\binom{n-1}{k}(1-x)^{(n-1)-k}x^k&\text{distributivity law in the ring }R\\
&=&nx\cdot 1&\text{sum of binomial coefficients (i)}\\
&=&nx&\text{existence of identity in }R\\
\end{array}
\]`
