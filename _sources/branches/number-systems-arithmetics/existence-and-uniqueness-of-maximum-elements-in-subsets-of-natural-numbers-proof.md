layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1437
orderid: 50
parentid: bookofproofs$1436
title: 
description:  Proof of EXISTENCE AND UNIQUENESS OF GREATEST ELEMENTS IN SUBSETS OF NATURAL NUMBERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: elements,existence,greatest,natural,numbers,subsets,uniqueness,proof
contributors: bookofproofs

---


---

We will prove the proposition for the [poset][bookofproofs$576] `$(\mathbb N,\le).$` An analogous proof is possible for the strictly-ordered set `$(\mathbb N, < ),$` in which we have to replace the order relation "`$\ge$`" by the order relation "`$>$`" and the word [maximum][bookofproofs$7995] by the word [maximal element][bookofproofs$7995].

* Let `\(M\)` be a [non-empty][bookofproofs$550] and [finite][bookofproofs$985] [subset][bookofproofs$552] of [natural numbers][bookofproofs$664] `\(M\subseteq\mathbb N.\)`  
* Since `$M$` is non-empty, let `\(n_0\in M\)` be its element.
* We will construct an [maximum][bookofproofs$7995] of `$M$` as follows:
   * If for all `$m\in M$` we have `$m\ge n_0$` we set `\(m_0:=n_0\)`, since it is the maximum we were looking for.
   * Otherwise there exists an `$n_1\in M$` with `\(n_1 > n_0.\)` 
   * We ask wether for all `$m\in M$` we have `$m\ge n_1.$`  
   * If so, then we set `\(m_0:=n_1\)`, otherwise we find an `$n_2\in M$` with `\(n_2 > n_1.\)` and repeat the same procedure again.
   * Since `$M$` is finite, our searching process will be repeated at most `\(n_0 - m_0+1\)` times until we finally find the maximum of `\(M\)`.
* By construction `$m_0$` is unique.
