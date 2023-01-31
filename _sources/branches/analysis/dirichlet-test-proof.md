layout: proof
categories: branches,analysis
nodeid: bookofproofs$8368
orderid: 50
parentid: bookofproofs$8367
title: 
description: PROOF OF DIRICHLET'S TEST ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: dirichlet's test,proof
contributors: bookofproofs

---


---

* By hypothesis, the [sequence of partial sums][bookofproofs$1109] `$(A_n)_{n\in\mathbb N}$` with `$A_n:=\sum_{k=0}^n a_k$` is [bounded][bookofproofs$1136] and the [sequence][bookofproofs$875] `$(b_k)_{k\in\mathbb N}$` is [monotonic][bookofproofs$1155] and [convergent][bookofproofs$141] to zero `$\lim_{k\to\infty} b_k=0$`.
* Since `$(A_n)_{n\in\mathbb N}$` is bounded, it follows that `$\lim_{k\to\infty} A_kb_{k+1}=0.$` 
* Moreover, since the [telescoping series][bookofproofs$8375] `$\sum_{k=1}^\infty (b_k-b_{k+1})$` is [convergent][bookofproofs$175], the series `$\sum_{k=1}^\infty A_k(b_k-b_{k+1})$` is [convergent][bookofproofs$175].
* By the [Abel's lemma][bookofproofs$8363], the series  `$\sum_{k=1}^\infty a_kb_k$` is convergent.


