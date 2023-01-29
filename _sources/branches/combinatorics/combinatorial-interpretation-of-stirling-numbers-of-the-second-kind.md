layout: explanation
categories: branches,combinatorics
nodeid: bookofproofs$8435
orderid: 700
parentid: bookofproofs$293
title: Combinatorial Interpretation of Stirling Numbers of the Second Kind
description: COMBINATORIAL INTERPRETATION OF STIRLING NUMBERS OF THE SECOND KIND ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1112
keywords: combinatorial interpretation of stirling numbers of the second kind
contributors: bookofproofs

---


---

Let `$n,r\ge 0$` be [integers][bookofproofs$844]. The [Stirling number of the second type][bookofproofs$8425] `$\left\{\begin{array}{c}n\\r\end{array}\right\}$` can be interpreted as the number of ways to arrange `$n$` objects into `$r$` [non-empty][bookofproofs$550] [subsets][bookofproofs$552].
### Examples

* `$\left\{\begin{array}{c}4\\2\end{array}\right\}=7,$` since there are `$7$` ways to split `$4$` objects into `$2$` non-empty subsets: `$$\begin{array}{cccc}
\{a,b,c\}\{d\}&\{a,b,d\}\{c\}&\{a,c,d\}\{b\}&\{b,c,d\}\{a\}\\
\{a,b\}\{c,d\}&\{a,c\},\{b,d\}&\{a,d\}\{b,c\}
\end{array}$$`
* `$\left\{\begin{array}{c}n\\1\end{array}\right\}=1,$` since there is only one way to split `$n$` objects into one non-empty subset.
* `$\left\{\begin{array}{c}n\\r\end{array}\right\}=0$` for `$r > n$` since there is no way to split `$n$` objects into a non-empty subset of `$r > n$` elements.
* `$\left\{\begin{array}{c}n\\0\end{array}\right\}=0$` for all `$n > 0$` since there is no way to split `$n$` objects into a non-empty subset of `$0$` elements.
* `$\left\{\begin{array}{c}0\\0\end{array}\right\}=1$` since there one way to split `$0$` objects into a non-empty subset of `$0$` elements.
* `$\left\{\begin{array}{c}n\\2\end{array}\right\}=2^{n-1}-1$` since if a set of `$n>0$` objects is split into two non-empty subsets, one of them contains the last element and some subset of the first `$n-1$` elements. There are `$2^{n-1}$` ways to choose a subset from the `$n-1$` first elements, but we want to exclude the subset containing all `$n-1$` elements, since otherwise the other split part would be empty. Therefore we have to subtract `$1.$`

### Convention
 `$\left\{\begin{array}{c}n\\r\end{array}\right\}$` can be verbalized as "$n$ subset `$r$`."
