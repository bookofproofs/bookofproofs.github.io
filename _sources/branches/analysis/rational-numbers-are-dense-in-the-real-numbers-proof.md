layout: proof
categories: branches,analysis
nodeid: bookofproofs$2952
orderid: 50
parentid: bookofproofs$6666
title: 
description: PROOF OF RATIONAL NUMBERS ARE DENSE IN REAL NUMBERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8311
keywords: rational numbers are dense,density of rational numbers,dense,proof
contributors: bookofproofs

---


---

* By hypothesis, `$x\in\mathbb R$` is a [real number][bookofproofs$1105] and `$\epsilon > 0$` any (arbitrarily small) [positive real number][bookofproofs$1107].
* We are going to find a [rational number][bookofproofs$1033] `$q\in\mathbb Q$` with `$q\in(x-\epsilon, x+\epsilon)$` using a constructed [convergent rational sequence][bookofproofs$1572].
   * First, we choose two [rational numbers][bookofproofs$844] `$\frac {a_0}1,\frac{b_0}1\in\mathbb Q$` with some [integers][bookofproofs$844] `$a_0 < x < b_0.$` This is possible because of the [Archimedean axiom][bookofproofs$1339].
   * Note that `$x\in [a_0,b_0],$` where `$[a_0,b_0]$` is a [closed interval][bookofproofs$1153].
   * Now, we construct for `$n=1,2,\ldots$` new closed intervals by the following rule:
      * if `$\frac{a_n+b_n}2 > x$`, we set `$a_{n+1}:=a_n$` and `$b_{n+1}=\frac{a_n+b_n}2,$`
      * otherwise, we set `$a_{n+1}:=\frac{a_n+b_n}2,$` and `$b_{n+1}:=b_n.$` 
   * By construction, the sequences `$(a_n)_{n\in\mathbb N}$` and `$(b_n)_{n\in\mathbb N}$` are [rational sequences][bookofproofs$1484] with `$x\in [a_{n},b_{n}]$` for all `$n:=1,2,\ldots.$`
   * Since the length of the `$n$`th interval is `$(b_0-a_0)/2^n,$` the sequences are also [real convergent sequences][bookofproofs$175] with the limit `$$x=\lim_{n\to\infty} a_n=\lim_{n\to\infty} b_n.$$` 
   * Although the limit `$x$` does not have to be a rational number[^1] itself, all sequence members `$a_n,b_n$` are, by construction, rational numbers for all `$n\in\mathbb N.$`
   * From the [definition of convergence][bookofproofs$175], it follows that, taking `$(a_n)_{n\in\mathbb N}$` as an example, there is an index `$N\in\mathbb N$` such that `$|a_n-x| < \epsilon$` for all `$n > N.$`
* By setting `$q:=a_N\in (x-\epsilon, x+\epsilon),$` we have found a rational number that lies arbitrarily [dense][bookofproofs$8581] with the real number `$x.$`

[^1]: Take `$x=\sqrt{2}$` as an example.
