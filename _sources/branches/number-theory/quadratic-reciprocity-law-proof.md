layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3544
orderid: 50
parentid: bookofproofs$8205
title: 
description:  Proof of QUADRATIC RECIPROCITY LAW &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: law,quadratic,reciprocity,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` and `$q > 2$` are [odd][bookofproofs$8130] and distinct [prime numbers][bookofproofs$473].
* If `$q\ge 2,$` then we can set according to [division with quotient and remainder][bookofproofs$818] for `$1\le k\le \frac{p-1}2$` `$$\label{eq:E18755a}\tag{1}kq=q_kp+r_k,\quad 0 < r_k < p.$$` Note that `$r_k\neq 0,$` since `$q$` and `$p$` are distinct.
* Moreover, we have `$q_k=\left\lfloor\frac{kq}p\right\rfloor$` due to the [connection between quotient, remainder, modulo and floor function][bookofproofs$1284].
* In the proof of the [Gaussian lemma][bookofproofs$8208], we have seen (with the same notation as there) that the remainders `$a_s$`, `$p-b_t$` the same numbers as the numbers `$$1,2,\ldots,\frac{p-1}2,$$` apart from the order.
* Therefore, with `$a:=\sum_{s=1}^l a_s$` and `$b:=\sum_{t=1}^m b_t$`, we have the [sum][bookofproofs$261] `$$\sum_{k=1}^{\frac{p-1}2}r_k=a+b.$$`
* On the other hand, the [sum of arithmetic progression][bookofproofs$1117] gives us `$$\label{eq:E18755b}\tag{2}\frac{p^2-1}8=\frac{\frac{p-1}{2}\cdot \frac{p+1}{2}}{2}=\sum_{k=1}^{\frac{p-1}{2}}k=a+mp-b.$$`
* Adding the equations `$(\ref{eq:E18755a}),$` we get `$$\label{eq:E18755c}\tag{3}\frac{p^2-1}8q=p\sum_{k=1}^{\frac{p-1}{2}}q_k+\sum_{k=1}^{\frac{p-1}{2}}r_k=p\sum_{k=1}^{\frac{p-1}{2}}q_k+a+b.$$` 
* From  `$(\ref{eq:E18755b})$` and `$(\ref{eq:E18755c}),$` we get 
`$$\frac{p^2-1}8(q-1)=p\sum_{k=1}^{\frac{p-1}{2}}q_k-mp+2b,$$` 
and the [congruence][bookofproofs$8153].
`$$\label{eq:E18755d}\tag{4}\frac{p^2-1}8(q-1)\equiv \sum_{k=1}^{\frac{p-1}{2}}q_k+m\mod 2.$$` 
* For `$q=2$`, all `$q_k=0,$` and we have `$\frac{p^2-1}8\equiv m\mod 2$` and therefore according to the [Gaussian lemma][bookofproofs$8208], the formula for the [Legendre symbol][bookofproofs$8198].
 `$$\left(\frac 2p\right)=(-1)^m=(-1)^{\frac{p^2-1}8}.$$`
* Let `$q > 2.$` Then `$q-1$` is [even][bookofproofs$8130], and we have in `$(\ref{eq:E18755d})$` `$$\sum_{k=1}^{\frac{p-1}{2}}q_k\equiv m\mod 2.$$`
* Therefore, applying the [Gaussian lemma][bookofproofs$8208] once again, we get the formula
 `$$\label{eq:E18755e}\tag{5}\left(\frac qp\right)=(-1)^m=(-1)^{\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\frac{kq}p\right\rfloor}.$$`
* From symmetry reasons, the same holds for 
 `$$\label{eq:E18755f}\tag{6}\left(\frac pq\right)=(-1)^{\sum_{l=1}^{\frac{q-1}{2}}\left\lfloor\frac{lp}q\right\rfloor}.$$`
* `$(\ref{eq:E18755e})$` and `$(\ref{eq:E18755f})$` give us together the result `$$\left(\frac qp\right)\cdot \left(\frac pq\right)=(-1)^{\alpha}$$` with `$$\alpha=\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\frac{kq}p\right\rfloor+\sum_{l=1}^{\frac{q-1}{2}}\left\lfloor\frac{lp}q\right\rfloor.$$`
* It remains to be shown that `$$\alpha=\frac{p-1}{2}\cdot\frac{q-1}{2},$$` but this follows from the [reciprocity law for floor functions][bookofproofs$8210].