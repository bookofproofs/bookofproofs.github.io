layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8439
orderid: 50
parentid: bookofproofs$8438
title: 
description: PROOF OF INVERSION FORMULAS FOR STIRLING NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1112
keywords: inversion formulas for stirling numbers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$n,m\ge 0$` are [integers][bookofproofs$844].
* Using the lemma for the [stirling numbers and rising factorial powers][bookofproofs$8432] and because `$\left\{\begin{array}{c}k\\m\end{array}\right\}=0$` for `$m > k,$` we get `$$\begin{align}
x^\overline{n}&= \sum_{k=1}^n\left[\begin{array}{c}n\\k\end{array}\right]x^k\nonumber\\
&= \sum_{k=1}^n\left[\begin{array}{c}n\\k\end{array}\right]\sum_{r=1}^k\left\{\begin{array}{c}k\\r\end{array}\right\}(-1)^{k-r}x^\overline{r}\nonumber\\
&= \sum_{k=1}^n\left[\begin{array}{c}n\\k\end{array}\right]\sum_{m=1}^n\left\{\begin{array}{c}k\\m\end{array}\right\}(-1)^{k-m}x^\overline{m}\nonumber\\
&= \sum_{k=1,m=1}^n\left[\begin{array}{c}n\\k\end{array}\right]\left\{\begin{array}{c}k\\m\end{array}\right\}(-1)^{n-k}x^\overline{m}\nonumber\\
\end{align}$$`
* Because this holds for all `$x$`, it follows that the coefficients of the sum on the right are all `$0$` except those, for which `$m=n.$`
* Thus, using the [Iverson notation][bookofproofs$261] and since all summands for indices `$k$` exceeding `$\min(m,n)$` equal `$0$`, we can write `$$\sum_{k=0}^\infty \left[\begin{array}{c}n\\k\end{array}\right]\left\{\begin{array}{c}k\\m\end{array}\right\}(-1)^{n-k}=[m=n].$$`
* The proof of the other identity `$$\sum_{k=0}^\infty \left\{\begin{array}{c}n\\k\end{array}\right\}\left[\begin{array}{c}k\\m\end{array}\right](-1)^{n-k}=[m=n]$$` can be done analogously plugging the defining equation of [Stirling numbers of the first kind][bookofproofs$8425] `$$x^\underline{n}= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right](-1)^{n-r}x^r$$` into the equation of the [Stirling numbers of the second kind][bookofproofs$8425] `$$x^{n}= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}x^\underline{r}.$$`
