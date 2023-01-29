layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1842
orderid: 50
parentid: bookofproofs$1841
title: 
description:  Proof of SUM OF BINOMIAL COEFFICIENTS I &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: binomial,coefficients,sum,proof
contributors: bookofproofs

---


---

Let `\(x\)` be an element of a [ring][bookofproofs$683] `\(x\in(R,+,\cdot) \)` and let `\(n\ge 1\)` be a [natural number][bookofproofs$718]. In the following calculation, we use the [binomial theorem][bookofproofs$1397] and some [rules of calculation in a ring][bookofproofs$683]:

`\[
\begin{array}{rcll}
\sum_{k=0}^n\binom nk(1-x)^{n-k}x^k&=&((1-x)+x)^{n}&\text{binomial theorem}\\
&=&(1-x+x)^{n}&\text{associativity of addition in }R\\
&=&(1+0)^{n}&\text{existence of negative inverse in }R\\
&=&1^{n}&\text{existence of zero in }R\\
&=&1&\text{existence of identity in }R\\
\end{array}
\]`
