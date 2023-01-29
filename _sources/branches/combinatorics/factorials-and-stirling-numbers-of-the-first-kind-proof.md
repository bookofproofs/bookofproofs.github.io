layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1008
orderid: 50
parentid: bookofproofs$1007
title: 
description: Proof of FACTORIALS AND STIRLING NUMBERS OF THE FIRST KIND ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$977,bookofproofs$1112
keywords: factorials and stirling numbers of the first kind,proof
contributors: bookofproofs

---


---

* Let `$n\ge 0$` be an [integer][bookofproofs$844].
* For `$n=0$`, we have `$0!=\left[\begin{array}{c}0\\0\end{array}\right]=1.$` 
* Let `$n > 0.$` 
* By [definition of factorial][bookofproofs$1005] `$n!,$` it is the number of [permutations][bookofproofs$188] of `$n$` objects.
* By definition of permutations, every permutation `$\pi_1,\ldots,\pi_n$` of `$\{1,2,\ldots, n\}$` defines an arrangement of [cycles][bookofproofs$8434].
* For if we start with `$n_0=n$` and look at `$n_1=\pi_{n_0}, n_2=\pi_{n_1},\ldots,$` we eventually come at `$n_k=n_0.$`
* Conversely (and reversing the construction), every cycle arrangement defines a permutation.
* Since the [Stirling numbers of the first kind][bookofproofs$1004] `$\left[\begin{array}{c}n\\r\end{array}\right]$` can be interpreted as the number of ways to arrange `$n$` objects into `$r$` cycles, it is therefore also the number of permutations that contain exactly `$r$` cycles.
* Summing `$\left[\begin{array}{c}n\\r\end{array}\right]$` over all `$r=0,\ldots,n,$` we must get the total number of permutations of `$n$` objects, i.e. `$$n!=\sum_{r=0}^n \left[\begin{array}{c}n\\r\end{array}\right],\quad\quad(n\ge 0).$$`
