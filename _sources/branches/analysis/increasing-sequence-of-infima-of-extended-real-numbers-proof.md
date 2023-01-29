layout: proof
categories: branches,analysis
nodeid: bookofproofs$2998
orderid: 50
parentid: bookofproofs$6672
title: 
description: PROOF OF INCREASING SEQUENCE OF INFIMUM OF EXTENDED REAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: increasing sequence of infima of extended real numbers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(a_n)_{n\in\mathbb N}$` is a [real sequence][bookofproofs$875], `$D_n:=\{a_k:~k\ge n\}$` are[^1] [subsets][bookofproofs$552] of its [carrier set][bookofproofs$6658].
* Let `$\sup D_n$` be the [infimum of extended real numbers][bookofproofs$6670] for each `$D_n$`. 
* Case 1: `$(a_n)_{n\in\mathbb N}$` is [bounded below][bookofproofs$1136].
   * Then `$D_n$` are [bounded below][bookofproofs$584] for all `$n\in\mathbb N.$`
   * Note that:
      * `$D_{n+1}\subset D_n,$` 
      * and thus any [lower bound][bookofproofs$584] of `$D_{n}$` is also an lower bound of `$D_{n+1}.$`
   * Also note that, by definition of [infimum][bookofproofs$1755]:
      * `$\sup D_{n+1}$` is both, an [lower bound][bookofproofs$584] of `$D_{n+1}$` and [greater than or equal to][bookofproofs$1107] every lower bound of `$D_{n+1},$`
      * `$\sup D_{n}$` is both, an [upper bound][bookofproofs$584] of `$D_{n}$` and [greater than or equal to][bookofproofs$1107] every lower bound of `$D_{n},$`
      * By first note, `$\sup D_{n+1}\ge \sup D_n.$`
   * It follows, that the sequence `$(\sup D_n)_{n\in\mathbb N}$` is [monotonically increasing][bookofproofs$1155].
* Case `$(a_n)_{n\in\mathbb N}$` is [unbounded][bookofproofs$1136].
   * Then `$\sup D_n=+\infty$` for all `$n\in\mathbb N.$`
   * The order relation `$\sup D_{n+1}\ge \sup D_n$` is not defined in this case.
   * But formally, we assert the sequence  `$(\sup D_n)_{n\in\mathbb N}$` is [monotonically increasing][bookofproofs$1155].
[^1]: Note: `$D_n$` can be visualized as `$$\begin{array}{c|ccccc}
n&D_n&&&&\\
\hline
1&a_1&a_2&a_3&a_4&\ldots\\
2&&a_2&a_3&a_4&\ldots\\
3&&&a_3&a_4&\ldots\\
4&&&&a_4&\ldots\\
\vdots&&&&&\ddots\\
\end{array}$$`
