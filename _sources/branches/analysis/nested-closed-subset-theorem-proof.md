layout: proof
categories: branches,analysis
nodeid: bookofproofs$6587
orderid: 50
parentid: bookofproofs$127
title: 
description:  Proof of NESTED CLOSED SUBSET THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$582
keywords: nested closed subset theorem,nested subset theorem,proof
contributors: bookofproofs

---


---

* Let `$(X,d)$` be a [metric space][bookofproofs$617].
* We will first show that there is at most one point of intersection.
   * Because for the [sequence][bookofproofs$874] of non-empty [subsets][bookofproofs$552] of `\(X\)` with  `$$A_0\supset A_1\supset A_2\supset A_3\supset \ldots\quad ( * )$$` the corresponding sequence of [diameters][bookofproofs$6581] `\((\operatorname{diam}(A_n))_{n\in\mathbb N}\)` is [converging][bookofproofs$141] against `$0$`, formally `$$\lim_{n\to\infty}\operatorname{diam}(A_n)=0,\quad ( * * )$$`
there are more than one point in the [intersection][bookofproofs$552] `$$\bigcap_{n=0}^\infty A_n$$`.
   * Otherwise, let `\(x\)` and `\(y\)` be at least two points in the intersection.
   * Because `$X$` is a [metric space][bookofproofs$617], it is also a [Hausdorff space][bookofproofs$850].
   * Therefore, because `\(x\neq y\)`, we would have `\(d(x,y) > 0\)`, [contradicting][bookofproofs$744] `$( * * )$`.
   * Therefore, there is at least one point of intersection.
* It remains to be shown that such single point of intersection exists.
   * Choose a point `\(x_n\in A_n\)`. 
   * Because `\[d(x_n,x_m)\le \operatorname{diam}(A_N)\quad\text{ for }n,m\ge N,\]`
the sequence `$(x_n)_{n\in\mathbb N}$` is a [Cauchy sequence][bookofproofs$1052] in `\(X\)`.
   * Because `\(X\)` is [complete][bookofproofs$377] by hypothesis, the Cauchy sequence has a [limit][bookofproofs$148] `\(x\in X\)`. 
   * Because `\(x_n\in A_n\)` for all `\(n\in\mathbb N\)`, it follows from the [characterization of closed sets by limits of convergent sequences][bookofproofs$6585] that `\(x \in A\)`.
