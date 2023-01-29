layout: theorem
categories: branches,combinatorics
nodeid: bookofproofs$8529
orderid: 500
parentid: bookofproofs$264
title: Inclusion-Exclusion Principle (Sylvester's Formula)
description: INCLUSION-EXCLUSION PRINCIPLE SYLVESTER'S FORMULA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577
keywords: inclusion-exclusion principle,sylvester's formula
contributors: bookofproofs


---
The following formula is due to "James Sylvester":https://www.bookofproofs.org/history/james-joseph-sylvester (1814 - 1897).

---

Let `$B_1,\ldots,B_\rho$` be [sets][bookofproofs$550]. The [cardinality][bookofproofs$980] of their [union][bookofproofs$6827] `$$B:=\bigcup_{r=1}^\rho B_r$$` can be calculated using the so-called *inclusion-exclusion principle*:
`$$\begin{align}|\mathbf{B}|&=\sum_{r=1}^\rho|B_r|\nonumber\\
&-\sum_{1\le r<s\le\rho}|(B_r\cap B_s)|\nonumber\\
&+\sum_{1\le r<s<t\le\rho}|(B_r\cap B_s\cap B_t)|\nonumber\\
&\vdots\nonumber\\
&+(-1)^{\rho-1}|(B_1\cap\ldots\cap B_\rho)|\nonumber\end{align}$$`
