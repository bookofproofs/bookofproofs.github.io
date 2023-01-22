layout: proof
categories: branches,algebra
nodeid: bookofproofs$2885
orderid: 0
parentid: bookofproofs$8249
title: 1552
description: PROOF OF CONTINUANTS AND CONVERGENTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: continuants,convergents,proof
contributors: bookofproofs

---


---

By [induction][bookofproofs$657], the above definition of continuants, as well as [convergents][bookofproofs$8188]:

### Base Case `$k=1$`
 `$[q_0;q_1]=q_0+\frac{1}{q_1}=q_0+\frac{Q_0}{Q_1(q_1)}$`

### Induction step `$k\to k+1$`:

`$$\begin{array}{rcll}
[q_0;q_1,\ldots,q_{k+1}]&=&q_0+\frac{1}{[q_1;q_2,\ldots,q_k]}\\
&=&q_0+\cfrac{1}{q_1+\cfrac{Q_{k-1}(q_2,\ldots,q_{k+1})}{Q_k(q_2,\ldots,q_{k+1})}}&\text{by base case}\\
&=&q_0+\cfrac{Q_k(q_2,\ldots,q_{k+1})}{q_1Q_k(q_2,\ldots,q_{k+1})+Q_{k-1}(q_3,\ldots,q_{k+1})}.
\end{array}$$`
