layout: lemma
categories: branches,algebra
nodeid: bookofproofs$8249
orderid: 2
parentid: bookofproofs$234
title: Continuants and Convergents
description: CONTINUANTS AND CONVERGENTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$8186,bookofproofs$8189
keywords: continuants,convergents
contributors: bookofproofs

---
By writing a [continued fraction][bookofproofs$8188] `$[q_0;q_1,q_2,\ldots]$`  as a usual [rational number][bookofproofs$1033], we get the results

`$$\begin{array}{rcl}
[q_0]&=&q_0\\
[q_0;q_1]&=&q_0+\frac{1}{q_1}\\
[q_0;q_1,q_2]&=&q_0+\cfrac{1}{q_1+\cfrac{1}{q_2}}=q_0+\frac{q_2}{q_1q_2+1}\\
[q_0;q_1,q_2,q_3]&=&q_0+\cfrac{1}{q_1+\cfrac{1}{q_2+\cfrac{1}{q_3}}}=q_0+\frac{1}{q_1+\frac{q_3}{q_2q_3+1}}=\frac{q_2q_3+1}{q_1q_2q_3+q_1+q_3}\\
\end{array}$$`
This motivates the following definition and lemma:

---

Let `$[q_0;q_1,q_2,\ldots,]$` be a given [continued fraction][bookofproofs$8188]. Then we can write the `$k$`-th [convergent][bookofproofs$8188] as `$$[q_0;q_1,q_2,\ldots,q_k]=q_0+\frac{Q_{k-1}(q_2,\ldots,q_k)}{Q_{k}(q_1,q_2,\ldots,q_k)}$$`
with the so-called `$k$`-th **continuant** [function][bookofproofs$592] `$Q:\mathbb Z^k\to\mathbb Z$` defined recursively by `$$Q_k(x_1,\ldots,x_k):=\begin{cases}0&\text{if }k=-1,\\1&\text{if }k=0,\\x_1&\text{if }k=1,\\q_1Q_{k-1}(x_2,\ldots,x_k)+Q_{k-2}(x_3,\ldots,x_k)&\text{else.}\end{cases}$$`
