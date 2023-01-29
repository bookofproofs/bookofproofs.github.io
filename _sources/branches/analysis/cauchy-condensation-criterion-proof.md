layout: proof
categories: branches,analysis
nodeid: bookofproofs$8346
orderid: 50
parentid: bookofproofs$286
title: 
description: PROOF OF CAUCHY CONDENSATION CRITERION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$586
keywords: cauchy condensation criterion,proof
contributors: bookofproofs

---


---

By hypothesis, `$\sum_{k=0}^\infty x_k$` is an [infinite series][bookofproofs$1109] `$\sum_{k=0}^\infty x_k$` with a [monotonically decreasing][bookofproofs$1155] [real sequence][bookofproofs$875] `$(x_k)_{k\in\mathbb N}$` of [non-negative][bookofproofs$1107] members `$x_k\ge 0.$`

### "`$\Rightarrow$`"

* Assume, `$\sum_{k=0}^\infty x_k$` is [convergent][bookofproofs$175].
* By definition, there is a real number `$s:=\sum_{k=0}^\infty x_k.$`
* Since `$x_k\ge 0$` and `$x_k \ge x_{k+1}$` for all `$k\in\mathbb N,$` we have `$$\begin{array}{rcl}s&\ge&x_1+x_2+(x_3+x_4)+(x_5+\cdots+x_8)+\cdots+(x_{2^{k-1}+1}+\cdots+x_{2^k})\\&\ge& \frac{x_1}{2}+x_2+2x_4+4x_8+\cdots+2^{k-1}x_{2^k}.\end{array}$$`
* It follows `$$s_k:=x_1+2x_2+4x_4+16x_8+\cdots+2x_{2^k}\le 2s$$`
* Therefore, the [real sequence][bookofproofs$875] of [partial sums][bookofproofs$1109] of the "condensed series"  `$s_k=\sum_{n=0}^k 2^nx_{2^n}$` consists of non-negative terms and constitutes a [bounded sequence][bookofproofs$1136].
* By the [monotony criterion][bookofproofs$1158], the "condensed series" `$$\sum_{n=0}^\infty 2^n x_{2^n}$$` is [convergent][bookofproofs$175].
### "`$\Leftarrow$`"

* Now, assume `$\sum_{n=0}^\infty 2^n x_{2^n}$` is [convergent][bookofproofs$175] and let `$t:=\sum_{n=0}^\infty 2^n x_{2^n}.$`
* If `$2^k\ge n$`, then `$$\begin{array}{rcl}x_1+x_2+\ldots+x_n&\le&x_1+(x_2+x_3)+(x_4+\cdots+x_7)+\cdots+(x_{2^k}+\cdots+x_{2^{k+1}-1})\\ &\le & x_1+2x_2+4x_4+\cdots+2^kx_{2^k}\\&\le& t.\end{array}$$`
* Therefore, the [real sequence][bookofproofs$875] of [partial sums][bookofproofs$1109] of the series `$u_n=\sum_{k=0}^n x_k$` consists of non-negative terms and constitutes a [bounded sequence][bookofproofs$1136].
* By the [monotony criterion][bookofproofs$1158], the series `$$\sum_{k=0}^\infty x_k$$` is [convergent][bookofproofs$175].