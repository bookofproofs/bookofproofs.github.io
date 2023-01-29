layout: proof
categories: branches,analysis
nodeid: bookofproofs$8646
orderid: 50
parentid: bookofproofs$8645
title: By Induction
description: PROOF OF GENERALIZED TRIANGLE INEQUALITY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: generalized triangle inequality,proof
contributors: bookofproofs

---


---

We provide a [proof by induction][bookofproofs$657] for [natural numbers][bookofproofs$718] `$n\ge 1$` and [absolute value of real numbers][bookofproofs$583] (respectively [absolute value of complex numbers][bookofproofs$1247]).
* Base case: `$n=1$`
`$$\left|\sum_{k=1}^1 a_k\right|=|a_1|\le|a_1|=\sum_{k=1}^1|a_k|.$$`
* Induction step `$n\to n+1$`
   * Assume, `$$\left|\sum_{k=1}^n a_k\right|\le\sum_{k=1}^n |a_k|$$` holds for some `$n\ge 1.$`
   * Then, by the [triangle inequality][bookofproofs$588] `$$\begin{align}\left|\sum_{k=1}^{n+1} a_k\right|&\le \left|\sum_{k=1}^{n} a_k\right|+|a_{n+1}|\nonumber\\
&\le\sum_{k=1}^{n} |a_k|+|a_{n+1}|\quad\text{(by assumption)}\nonumber\\
&= \sum_{k=1}^{n+1} |a_k|.\nonumber\end{align}$$`
