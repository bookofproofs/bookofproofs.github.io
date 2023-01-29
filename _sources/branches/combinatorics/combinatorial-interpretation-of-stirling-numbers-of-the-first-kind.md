layout: explanation
categories: branches,combinatorics
nodeid: bookofproofs$1004
orderid: 600
parentid: bookofproofs$293
title: Combinatorial Interpretation of Stirling Numbers of the First Kind
description: COMBINATORIAL INTERPRETATION OF STIRLING NUMBERS OF THE FIRST KIND ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$977
keywords: combinatorial interpretation of stirling numbers of the first kind
contributors: bookofproofs

---
The following interpretation of the [Stirling number of first type][bookofproofs$8425] is sometimes in the literature used for their definition:

---

Let `$n,r\ge 0$` be [integers][bookofproofs$844]. The [Stirling number of the first type][bookofproofs$8425] `$\left[\begin{array}{c}n\\r\end{array}\right]$` can be interpreted as the number of ways to arrange `$n$` objects into `$r$` [cycles][bookofproofs$8434]. In other words, the [Stirling number of first type][bookofproofs$8425] `$\left[\begin{array}{c}n\\r\end{array}\right]$` is the number of [permutations][bookofproofs$188] of `$n$` objects with exactly `$r$` [cycles][bookofproofs$8434].
### Examples

* `$\left[\begin{array}{c}4\\2\end{array}\right]=11,$` since there are `$11$` ways to arrange `$4$` objects into `$2$` cycles: `$$\begin{array}{ccc}
[a,b,c][d]&[a,b,d][c]&[a,c,d][b]\\
[b,c,d][a]&[a,c,b][d]&[a,d,b][c]\\
[a,d,c][b]&[b,d,c][a]\\
[a,b][c,d]&[a,c],[b,d]&[a,d][b,c]
\end{array}$$`
* `$\left[\begin{array}{c}n\\1\end{array}\right]=(n-1)!,$` since in every cycle `$[a_1,a_2\ldots,a_n]$` of the length `$n$` and a fixed element `$a_1$` we can arrange `$a_2,\ldots,a_n$` in the [factorial][bookofproofs$1005] `$(n-1)!$` ways.

### Convention
 `$\left[\begin{array}{c}n\\r\end{array}\right]$` can be verbalized as "$n$ cycle `$r$`."
