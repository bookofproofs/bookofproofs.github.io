layout: proof
categories: branches,analysis
nodeid: bookofproofs$8376
orderid: 50
parentid: bookofproofs$8375
title: 
description: PROOF OF CONVERGENCE TEST FOR TELESCOPING SERIES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$586
keywords: convergence test for telescoping series, telescoping series, telescoping sum,proof
contributors: bookofproofs

---


---

* The telescoping [partial sum][bookofproofs$1109] equals `$$\begin{array}{rcl}\sum_{k=0}^n (b_k-b_{k+1})&=&(b_0-b_1)+(b_1-b_2)+(b_2-b_3)+\ldots--b_{n}+(b_n-b_{n+1})\\&=&b_0+(-b_1+b_1)+(-b_2+b_2)+-b_3+\ldots+(-b_{n}+b_n)-b_{n+1}\\&=&b_0-b_{n+1}.\end{array}$$`
* Since, by hypothesis, `$(b_k)_{k\in\mathbb N}$` is [convergent sequence][bookofproofs$141], the infinite series `$\sum_{k=0}^\infty (b_k-b_{k+1})$` converges to the value `$b_0-\beta,$` where `$\beta:=\lim_{k\to\infty} b_k.$`
* If, in addition, `$(b_k)_{k\in\mathbb N}$` is [monotonic][bookofproofs$1155], the terms `$(b_k-b_{k+1})$` are either all `$\ge 0$` or all `$\le 0.$`
* In the case `$(b_k-b_{k+1})\ge 0$` we have that `$\sum_{k=0}^\infty |b_k-b_{k+1}|$` is [absolutely convergent][bookofproofs$198].
* In the case `$(b_k-b_{k+1})\le 0$` we have `$|b_k-b_{k+1}|=|b_{k+1}-b_k|=b_{k+1}-b_k.$`
* Therefore, `$\sum_{k=0}^\infty |b_k-b_{k+1}|$` is also [absolutely convergent][bookofproofs$198], since the infinite series `$\sum_{k=0}^\infty (b_{k+1}-b_k)$` converges to `$\beta-b_0.$`
