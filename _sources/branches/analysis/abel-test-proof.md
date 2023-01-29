layout: proof
categories: branches,analysis
nodeid: bookofproofs$8366
orderid: 50
parentid: bookofproofs$8365
title: 
description: PROOF OF ABEL'S TEST ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: abel's test,abel test,abel's test proof,proof
contributors: bookofproofs

---


---

* By hypothesis, the [infinite series][bookofproofs$1109] `$\sum_{k=1}^\infty a_k$` is [convergent][bookofproofs$175] and the sequence `$(b_k)_{k\in\mathbb N}$` is [bounded][bookofproofs$1136] and [monotonic][bookofproofs$1155].
* Thus, the sequence `$(A_k)_{n\in\mathbb N}$` of [partial sums][bookofproofs$1109] `$A_k:=\sum_{j=1}^k a_j$` is [convergent][bookofproofs$141].
* Moreover, since [every monotonic bounded sequence is convergent][bookofproofs$197], `$(b_k)_{k\in\mathbb N}$` is convergent.
* Therefore, the [telescoping series][bookofproofs$8375] `$\sum_{k=1}^\infty (b_k-b_{k+1})$` is [convergent][bookofproofs$175], it is even [absolutely convergent][bookofproofs$198], since all of its terms are either `$\ge 0$` or `$\le 0.$`
* Since `$A_k$` are bounded, the series  `$\sum_{k=1}^\infty A_k(b_k-b_{k+1})$` is convergent and the series `$\sum_{k=1}^\infty A_kb_{k+1}$` is convergent.
* By the [Abel's lemma][bookofproofs$8363], the series  `$\sum_{k=1}^\infty a_kb_k$` is convergent.
