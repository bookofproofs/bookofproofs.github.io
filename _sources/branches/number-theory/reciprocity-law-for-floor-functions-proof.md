layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3549
orderid: 50
parentid: bookofproofs$8210
title: 
description:  Proof of RECIPROCITY LAW FOR FLOOR FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: floor,functions,law,reciprocity,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p,q\in\mathbb Z$` are [co-prime][bookofproofs$8093], [odd][bookofproofs$8130], and both `$ > 2.$`
* We consider the numbers `$lp-kq$` for `$k=1,\ldots,\frac{p-1}{2}$` and `$l=1,\ldots,\frac{q-1}{2}.$`
* None of these numbers equals `$0$`, otherwise we would have that `$lp=kq$` and `$q$` would be a [divisor][bookofproofs$700] of `$lp$` and since `$q$` and `$p$` are distinct, `$q$` would divide `$l$`, which is impossible due to `$l < \frac q2.$`
* According to the [creation of reduced residue systems from others][bookofproofs$8177], these numbers must therefore be all distinct.
* Therefore, there are `$\frac{p-1}{2}\cdot\frac{q-1}{2}$` different numbers `$lp-kq$` for `$k=1,\ldots,\frac{p-1}{2}$` and `$l=1,\ldots,\frac{q-1}{2}.$`
* Since for `$l=1,\ldots,\frac{q-1}{2}$` we have `$$k < \frac{lp}q,\quad k=1,\ldots,\frac{p-1}{2},$$` and since `$\frac{lp}q$` is not an integer, there are exactly `$\left\lfloor\frac{lp}q\right\rfloor$` solutions of `$ k=1,\ldots,\frac{p-1}{2},$` using [number of multiples of a given number less than another number][bookofproofs$8107].
* Therefore, there are `$$\sum_{l=1}^{\frac{q-1}{2}}\left\lfloor\frac{lp}q\right\rfloor$$` [positive integers][bookofproofs$1075] `$lp-kq$` for `$k=1,\ldots,\frac{p-1}{2}$` and `$l=1,\ldots,\frac{q-1}{2}.$`
* Since `$k < \frac{\frac{q}{2}p}{q}=\frac p2,$`  for symmetry reasons, we have `$$\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\frac{kq}p\right\rfloor$$` [negative integers][bookofproofs$1075] `$lp-kq$` for `$k=1,\ldots,\frac{p-1}{2}$` and `$l=1,\ldots,\frac{q-1}{2}.$`
* Altogether, we have `$$\frac{p-1}{2}\cdot\frac{q-1}{2}=\sum_{l=1}^{\frac{q-1}{2}}\left\lfloor\frac{lp}q\right\rfloor+\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\frac{kq}p\right\rfloor.$$`
