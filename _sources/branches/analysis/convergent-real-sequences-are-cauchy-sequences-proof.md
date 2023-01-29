layout: proof
categories: branches,analysis
nodeid: bookofproofs$8678
orderid: 50
parentid: bookofproofs$8677
title: 
description: PROOF OF CONVERGENT REAL SEQUENCES ARE CAUCHY SEQUENCES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: convergent real sequences are cauchy sequences,proof
contributors: bookofproofs

---


---

* By hypothesis, a given [real sequence][bookofproofs$875] `$(a_n)_{n\in\mathbb N}$` is [convergent][bookofproofs$175] to the limit `$a\in\mathbb R.$` 
* This means that for a given `$\epsilon > 0$` there is an index `$N\in\mathbb N$` such that `$$|a_n-a| < \frac{\epsilon}2$$` for all `$n\ge N.$`
* Thus, by the [triangle inequality][bookofproofs$618] `$$\begin{align}|a_n- a_m|&=|a_n-a+a-a_m|\nonumber\\
&\le |a_n-a|+|a-a_m|\nonumber\\
&\le \frac{\epsilon}{2}+\frac{\epsilon}{2}\nonumber\\
&=\epsilon\nonumber\end{align}$$` for all `$n,m\ge N.$`
* It follows that `$(a_n)_{n\in\mathbb N}$` is a [real Cauchy sequence][bookofproofs$1704].