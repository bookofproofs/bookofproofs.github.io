layout: proof
categories: branches,analysis
nodeid: bookofproofs$1338
orderid: 50
parentid: bookofproofs$590
title: By Induction
description: PROOF BY INDUCTION Proof of BERNOULLI'S INEQUALITY ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: bernoulli inequality,bernoulli's inequality,bernoulli's inequality proof,proof
contributors: bookofproofs

---


---

We prove by [induction][bookofproofs$657] that for all [real][bookofproofs$1105] `\(x \ge -1\)` and all [natural numbers][bookofproofs$718] `\(n\ge 2\)`, the following inequality holds:
`\[(1+x)^n \ge 1 + nx\quad\quad ( * ).\]`

* Base case `$n=0$` the inequality `\(( * )\)` is fulfilled: `$$(1+x)^0=1\ge 1+0x=1.$$`
* Induction step `$n\to n+1$` 
   * Assume, the inequality `\(( * )\)` is fulfilled for all `\(m \le n\)`. 
* Because `\(x \ge -1\)`, we have `\(1 + x\ge 0\)`, and we can multiply the inequality `\(( * )\)` by `\(1+x\)` and get
`\[\begin{align}(1+x)^{n+1}&\ge (1+nx)(1+x)\nonumber\\
&=1+(n+1)x+nx^2\nonumber\\
&\ge 1+(n+1)x.\nonumber\end{align}\]`
