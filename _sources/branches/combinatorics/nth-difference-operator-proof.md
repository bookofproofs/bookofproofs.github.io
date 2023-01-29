layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8412
orderid: 50
parentid: bookofproofs$8411
title: By Induction
description: PROOF OF NTH DIFFERENCE OPERATOR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1591
keywords: nth difference operator,proof
contributors: bookofproofs

---


---

* By hypothesis, `$f:D\to\mathbb R$` is a [function][bookofproofs$592] with `$D\subseteq\mathbb R.$` Moreover, let `$n\in\mathbb N,$` `$x, x+1,\ldots, x+n\in D.$`
* The statement can be proved by [induction][bookofproofs$657].
* Base case `$n=1$`
   * The formula `$$\Delta f(x)=f(x+1)-f(x)=\sum_{k=0}^1 f(x+k)\cdot (-1)^{n-k}\cdot\binom nk$$` is true, by definition of the [difference operator][bookofproofs$8408] and the definition of [binomial coefficients][bookofproofs$993].
* Induction step `$n\to n+1$`
   * Inductin premise: Assume `$n\ge 1$` and let the formula `$$\Delta^m f(x)=\sum_{k=0}^m f(x+k)\cdot (-1)^{m-k}\cdot\binom mk$$` be true for all `$m\le n.$`
   * By the induction step premise, and [basic calculations involving the difference operator][bookofproofs$8409] (no. 1 and no. 2) it follows `$$\begin{align}\Delta^{n+1} f(x)&=\Delta (\Delta^n f(n))\\
&=\Delta\left( \sum_{k=0}^n f(x+k)\cdot (-1)^{n-k}\cdot\binom nk\right)\\
&=\sum_{k=0}^n(f(x+k+1)-f(x+k))\cdot (-1)^{n-k}\cdot\binom nk\\
&=\sum_{k=0}^n f(x+k+1)\cdot (-1)^{n-k}\cdot\binom nk-\sum_{k=0}^n f(x+k)\cdot (-1)^{n-k}\cdot\binom nk\\
&=\sum_{k=0}^n f(x+k+1)\cdot (-1)^{n-k}\cdot\binom nk+\sum_{k=0}^n f(x+k)\cdot (-1)^{n+1-k}\cdot\binom nk\\
\end{align}$$`
   * Changing the index `$k+1\to k$` in the left sum allows combining both sums together:
`$$\begin{align}
&=\sum_{k=1}^{n+1} f(x+k)\cdot (-1)^{n-(k-1)}\cdot\binom n{k-1}+\sum_{k=0}^n f(x+k)\cdot (-1)^{n+1-k}\cdot\binom nk\\
&=f(x+n+1)+\sum_{k=1}^{n} f(x+k)\cdot (-1)^{(n+1)-k}\cdot\binom n{k-1}\cdot \binom nk+f(x)\cdot (-1)^{n+1}\\
\end{align}$$`
   * With the [recursive formula for the binomial coefficient][bookofproofs$994], it follows
`$$\begin{align}&=f(x+n+1)+\sum_{k=1}^{n} f(x+k)\cdot (-1)^{(n+1)-k}\cdot\binom {n+1}{k}+f(x)\cdot (-1)^{n+1}\\
&=\sum_{k=0}^{n+1} f(x+k)\cdot (-1)^{(n+1)-k}\cdot\binom {n+1}{k}.
\end{align}$$`
