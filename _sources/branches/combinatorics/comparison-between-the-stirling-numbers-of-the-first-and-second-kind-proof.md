layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8437
orderid: 50
parentid: bookofproofs$8436
title: 
description: PROOF OF COMPARISON BETWEEN THE STIRLING NUMBERS OF THE FIRST AND SECOND KIND &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1112
keywords: comparison between the sterling numbers of the first and second kind,proof
contributors: bookofproofs

---


---

* Let `$n,r\ge 0$` be [integers][bookofproofs$844].
* The number of partitions of `$n$` objects into `$r$` [non-empty][bookofproofs$550] [subsets][bookofproofs$552] corresponds to the [Stirling numbers of the second kind][bookofproofs$8425] `$\left\{\begin{array}{c}n\\r\end{array}\right\}.$`
* Every partition of `$n$` objects into `$r$` non-empty subsets leads to at least one partition of `$n$` objects into `$r$` [cycles][bookofproofs$8434].
* Since the number of partitions of `$n$` objects into `$r$` cycles corresponds to the [Stirling numbers of the first kind][bookofproofs$8425] `$\left[\begin{array}{c}n\\r\end{array}\right],$` it follows `$\left[\begin{array}{c}n\\r\end{array}\right]\ge \left\{\begin{array}{c}n\\r\end{array}\right\}$` for all `$n,r\ge 0.$`
* The number of arrangements of `$n$` objects into `$n$` non-empty subsets and `$n$` cycles equal each other and is `$1$`
* Therefore, `$\left[\begin{array}{c}n\\n\end{array}\right]=\left\{\begin{array}{c}n\\n\end{array}\right\}=1.$`
* In any arrangement of `$n$` objects into `$n-1$` non-empty subsets there is exactly one subset with `$2$` elements and all remaining subsets are [singletons][bookofproofs$8034].
* Moreover, all these subsets with either `$1$` or `$2$` elements correspond to cycles and there are `$\binom n2=\frac{n(n-1)}{2}$` such arrangements.
* Therefore, `$\left[\begin{array}{c}n-1\\n\end{array}\right]=\left\{\begin{array}{c}n\\n-1\end{array}\right\}=\left(\begin{array}{c}n\\2\end{array}\right)=\frac{n(n-1)}{2}.$`
