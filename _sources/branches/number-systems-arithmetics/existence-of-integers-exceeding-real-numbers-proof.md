layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$920
orderid: 50
parentid: bookofproofs$1342
title: 
description: Proof of EXISTENCE OF INTEGERS EXCEEDING REAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$577
keywords: unique integers exceeding real numbers,proof
contributors: bookofproofs

---


---

* Assume `$x=0$` ([real number][bookofproofs$1105]).
   * Then `$n=0$` ([integer][bookofproofs$844]) does the trick: `$0\le x < 1,$` because of the [its uniqueness][bookofproofs$1682].
* Assume `$x > 0$` is a [positive real number][bookofproofs$1107].
   * According to the [Archimedean principle][bookofproofs$1340] the set `$N:=\{k\in\mathbb N\mid k > x\}$` of [natural numbers][bookofproofs$718] `$k$` greater than `$x$` is not [empty][bookofproofs$550].
   * By the [well-ordering principle][bookofproofs$698], `$N$` contains a smallest element `$m.$`
   * Note that `$m > x > 0,$` therefore `$m\ge 1.$` 
   * Set `$n=m-1.$`
   * It follows `$n$` is the unique [integer][bookofproofs$844] with `$n\le x < n+1.$`
* Assume `$x < 0$` is a [negative real number][bookofproofs$1107].
   * Since `$-x > 0,$` we have already shown that there is a unique integer `$l$` with `$l\le -x < l + 1.$` 
   * Therefore, there is a unique integer `$-l$` with `$-l-1 < x \le -l.$`  
   * If `$x = -l,$` then `$-l\le x < -l+1$` with a unique `$l.$`
   * Else if `$x < -l,$` then `$-l-1\le x < l$` with a unique `$l.$`
