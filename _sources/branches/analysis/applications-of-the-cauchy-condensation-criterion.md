layout: example
categories: branches,analysis
nodeid: bookofproofs$8349
orderid: 50
parentid: bookofproofs$286
title: Applications of the Cauchy Condensation Criterion
description: APPLICATIONS OF THE CAUCHY CONDENSATION CRITERION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: applications of the condensation criterion
contributors: bookofproofs

---
We provide some example applications of the [Cauchy condensation criterion][bookofproofs$286].
---

### Example 1

The generalized [harmonic series][bookofproofs$237] `$\sum \frac{1}{n^\alpha}$` is divergent for `$\alpha\le 1$` and convergent for `$\alpha > 1.$`

### Proof

* By the Cauchy condensation criterion, the series  `$$\sum_{n=0}^\infty \frac{1}{n^\alpha}$$` is convergent if and only if the series `$$\sum_{n=0}^\infty\frac{2^n}{(2^n)^\alpha}$$` is convergent.
* Since `$\frac{2^n}{(2^n)^\alpha}=2^n\cdot 2^{-n\alpha}=2^{n(1-\alpha)}=\left(\frac{1}{2^{1-\alpha}}\right)^n$` we have two cases:
   * Case 1: if `$\alpha\le 1$` then `$\alpha - 1\le 0$` and `$2^{\alpha-1}\le 1$`. Therefore `$\frac{1}{2^{1-\alpha}}\ge 1.$` and the above harmonic series diverges.
   * Case 2: if `$\alpha > 1$` then `$\alpha - 1 > 0$` and `$2^{\alpha-1} > 1$`. Therefore `$\frac{1}{2^{1-\alpha}} < 1$` and the above harmonic series converges, since it is the convergent [geometric series][bookofproofs$1353].
### Example 2

The series `$\sum \frac{1}{n(\log(n))^\alpha}$` is divergent for `$\alpha\le 1$` and convergent for `$\alpha > 1.$`

### Proof

* By the Cauchy condensation criterion, the series  `$$\sum_{n=0}^\infty \frac{1}{n(\log(n))^\alpha}$$` is convergent if and only if the series `$$\sum_{n=0}^\infty\frac{2^n}{2^n(\log(2^n))^\alpha}$$` is convergent.
* Since `$\frac{2^n}{2^n(\log(2^n))^\alpha}=\frac{1}{(n\log(2))^\alpha}=\log(2)^{-\alpha}\cdot \frac {1}{n^\alpha},$`  the convergence behavior is the same as in the case 1 except the constant value `$\log(2)^{-\alpha}.$`
