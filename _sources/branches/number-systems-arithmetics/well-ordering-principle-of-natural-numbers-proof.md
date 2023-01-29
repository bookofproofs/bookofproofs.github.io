layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$699
orderid: 50
parentid: bookofproofs$698
title: 
description:  Proof of WELL-ORDERING PRINCIPLE OF NATURAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: well-ordering principle,well-order principle,well,proof
contributors: bookofproofs

---


---

We will prove the proposition for the [poset][bookofproofs$576] `$(\mathbb N,\le).$` An analogous proof is possible for the strictly-ordered set `$(\mathbb N, < ),$` in which we have to replace the order relation "`$\le$`" by the order relation "`$<$`" and the word [minimum][bookofproofs$7995] by the word [minimal element][bookofproofs$7995].

* Let `\(M\)` be a non-empty [subset][bookofproofs$552] of [natural numbers][bookofproofs$664] `\(M\subseteq\mathbb N.\)` 
* Since `$M$` is non-empty, let `\(n_0\in M\)` be its element.
* We will construct a [minimum][bookofproofs$7995] as follows:
   * If there is no [smaller][bookofproofs$697] element `\(m \le n_0\)` then we set `\(m_0:=n_0\)`, since it is the minimum we were looking for.
   * Otherwise there exists an `$n_1\in M$` with `\(n_1 < n_0.\)` 
   * We ask again if there is no [smaller][bookofproofs$697] element `\(m \le n_1\)`. 
   * If so, then we set `\(m_0:=n_1\)`, otherwise we find an `$n_2\in M$` with `\(n_2 < n_1.\)` and repeat the same search again.
   * Our searching process will be repeated at most `\(n_0 - m_0+1\)` times until we finally find the smallest element of `\(M\)`.
* This shows that `$M$` contains a minimum, which is by construction unique.
* We have shown that `$(\mathbb N,\le)$` is a [well-ordered][bookofproofs$7997] set.
