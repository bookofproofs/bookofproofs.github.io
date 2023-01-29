layout: proof
categories: branches,analysis
nodeid: bookofproofs$2997
orderid: 50
parentid: bookofproofs$6671
title: 
description: Proof of DECREASING SEQUENCE OF SUPREMA OF EXTENDED REAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: decreasing sequence of suprema of extended real numbers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(a_n)_{n\in\mathbb N}$` is a [real sequence][bookofproofs$875], `$D_n:=\{a_k:~k\ge n\}$` are[^1] [subsets][bookofproofs$552] of its [carrier set][bookofproofs$6658].
* Let `$\sup D_n$` be the [supremum of extended real numbers][bookofproofs$6669] for each `$D_n$`. 
* Case 1: `$(a_n)_{n\in\mathbb N}$` is [bounded above][bookofproofs$1136].
   * Then `$D_n$` are [bounded above][bookofproofs$584] for all `$n\in\mathbb N.$`
   * Note that:
      * `$D_{n+1}\subset D_n,$` 
      * and thus any [upper bound][bookofproofs$584] of `$D_{n}$` is also an upper bound of `$D_{n+1}.$`
   * Also note that, by definition of [supremum][bookofproofs$1754]:
      * `$\sup D_{n+1}$` is both, an [upper bound][bookofproofs$584] of `$D_{n+1}$` and [less than or equal to][bookofproofs$1107] every upper bound of `$D_{n+1},$`
      * `$\sup D_{n}$` is both, an [upper bound][bookofproofs$584] of `$D_{n}$` and [less than or equal to][bookofproofs$1107] every upper bound of `$D_{n},$`
      * By first note, `$\sup D_{n+1}\le \sup D_n.$`
   * It follows, that the sequence `$(\sup D_n)_{n\in\mathbb N}$` is [monotonically decreasing][bookofproofs$1155].
* Case `$(a_n)_{n\in\mathbb N}$` is [unbounded][bookofproofs$1136].
   * Then `$\sup D_n=+\infty$` for all `$n\in\mathbb N.$`
   * The order relation `$\sup D_{n+1}\le \sup D_n$` is not defined in this case.
   * But formally, we assert the sequence  `$(\sup D_n)_{n\in\mathbb N}$` is [monotonically decreasing][bookofproofs$1155].
[^1]: Note: `$D_n$` can be visualized as `$$\begin{array}{c|ccccc}
n&D_n&&&&\\
\hline
1&a_1&a_2&a_3&a_4&\ldots\\
2&&a_2&a_3&a_4&\ldots\\
3&&&a_3&a_4&\ldots\\
4&&&&a_4&\ldots\\
\vdots&&&&&\ddots\\
\end{array}$$`
