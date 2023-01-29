layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1840
orderid: 50
parentid: bookofproofs$1839
title: 
description: Proof of SIMPLE BINOMIAL IDENTITIES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$856
keywords: identities of binomial coefficients,proof
contributors: bookofproofs

---


---

### Ad `\((1)\)`

* From the [closed formula for binomial coefficients][bookofproofs$1400] and the [definition of rational numbers][bookofproofs$1033]  it follows for `\(k\ge 1\)`:
`\[\begin{array}{rcll}
k\binom nk&=&\cancel {k}\cdot \frac{n(n-1)\cdot\ldots\cdot(n-k+1)}{\cancel {k}(k-1)\cdot\ldots \cdot 2\cdot 1}&\text{definition of binomial coefficients, cancellation of }k\\
&=&n\cdot \frac{(n-1)\cdot \ldots\cdot (n-k+1)}{(k-1)\cdot\ldots \cdot 2\cdot 1}&\text{extraction of a factor from the nominator}\\
&=&n\binom{n-1}{k-1}&\text{definition of binomial coefficients}.
\end{array}\]`

### Ad `\((2)\)`

* From the [closed formula for binomial coefficients][bookofproofs$1400], the [definition of rational numbers][bookofproofs$1033], and the [distributivity law for rational numbers][bookofproofs$1491], it follows for `\(k\ge 2\)`:

`\[\begin{array}{rcll}
k^2\binom nk&=&(k+k(k-1))\binom nk&\text{rewriting }k^2\\
&=&k\binom nk+k(k-1)\binom nk&\text{"distributivity law for rational numbers}\\
&=&k\binom nk+\cancel {k(k-1)}\cdot \frac{n(n-1)(n-2)\cdot\ldots\cdot(n-k+1)}{\cancel {k(k-1)}(k-2)\cdot\ldots \cdot 2\cdot 1}&\text{definition of binomial coefficients, cancellation of }k(k-1)\\
&=&k\binom nk+n(n-1)\cdot \frac{(n-2)\cdot \ldots\cdot (n-k+1)}{(k-2)\cdot\ldots \cdot 2\cdot 1}&\text{extraction of a factor from the nominator}\\
&=&k\binom nk+n(n-1)\binom{n-2}{k-2}&\text{definition of binomial coefficients}.
\end{array}\]`

### Ad `$(3)$`

* By the [closed formula for binomial coefficients][bookofproofs$1400] `$$\binom nk=\frac{n !}{k !\cdot (n-k) !}.$$`
* The formula is symmetric by replacing `$k$` by `$(n-k)$`.
