layout: proof
categories: branches,analysis
nodeid: bookofproofs$6578
orderid: 50
parentid: bookofproofs$6577
title: 
description:  Proof of CONVERGENT SEQUENCE TOGETHER WITH LIMIT IS A COMPACT SUBSET OF METRIC SPACE &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$582
keywords: compact,convergent,limit,metric,sequence,space,subset,together,proof
contributors: bookofproofs

---


---

* Let `\((X,d)\)` be a   [metric space][bookofproofs$617].
* Let the points `\(x_n\)` of a [convergent][bookofproofs$148]  [sequence][bookofproofs$874] `\((x_n)_{n\in\mathbb N}\)` be all contained in `$X$`, i.e.   `\(x_n\in X\)`,  for all `\(n\in\mathbb N\)`. 
* Let the limit `$x=\lim_{n\to\infty} x_n$` be also contained in `\(X\)`.
* We have to show that `\(U:=\{x_n:~n\in\mathbb N\}\cup \{x\}\)` is a [compact][bookofproofs$6575]  [subset][bookofproofs$552] of `\(X\)`.
* For let an [open cover][bookofproofs$150] `$(U_i)_{i\in I}$` of `$U$` be given.
* Since `\(x\in U\)` by definition, there is an index `\(i^*\in I\)` with `$x\in U_{i^*}$`. 
* Because `$U_{i^*}$` is [open][bookofproofs$852],  `$U_{i^*}$` is a [neighborhood][bookofproofs$849] of `\(x\)`.
* Because `\((x_n)_{n\in\mathbb N}\)` [converges][bookofproofs$148]  against `$x$`, there is an index `\(N\in\mathbb N\)` such that `$x_n\in U_{i^*}$` for all `\(n > N\)`.
* Moreover, every sequence member `\(x_k\)` is covered by some open set `\(U_{i_k}\)` for the [finitely many][bookofproofs$985] indices `\(k=0,1,\ldots,N\)`.
* By construction, it follows that `\[U\subset U_{i_0}\cup U_{i_1}\cup\ldots\cup U_{i_N}\cup U_{i^*}.\]`
* Thus, we have found a finite subcover of `\(U\)` in the given open cover `$(U_i)_{i\in I}$`.
* Therefore, `\(U\)` is compact.
