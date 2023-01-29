layout: proof
categories: branches,analysis
nodeid: bookofproofs$8374
orderid: 50
parentid: bookofproofs$8373
title: By Induction
description: PROOF OF INEQUALITY BETWEEN THE GEOMETRIC AND THE ARITHMETIC MEAN ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$586
keywords: inequality between geometric and arithmetics mean, geometric and arithmetic means,proof
contributors: bookofproofs

---


---

* By hypothesis, `$a_1,\ldots,a_n$` are [non-negative positive real numbers][bookofproofs$1107].
* If at least one `$a_i=0$`, then the whole product `$a_1\cdots a_n=0$` and the inequation between the [geometric mean][bookofproofs$8372] and their [arithmetic mean][bookofproofs$8369] `$\sqrt[n]{a_1\cdots a_n}\le \frac{a_1+\cdots+a_n}n$` is trivial.
* Therefore, we assume `$a_1\cdots a_n > 0$` and prove the equivalent inequation `${a_1\cdots a_n}\le \left(\frac{a_1+\cdots+a_n}n\right)^n$` by [induction][bookofproofs$657] on `$n.$`
* Base Case: 
   * For `$n=1$` the inequation is true: `$a_1 \le \left(\frac{a_1}{1}\right)^1=a_1.$` 
* Induction Step: 
   * Assume, the inequation `${a_1\cdots a_n}\le \left(\frac{a_1+\cdots+a_n}n\right)^n$` is true for `$n$` numbers.
   * For `$n+1$` [positive][bookofproofs$1107] numbers `$a_1,\ldots,a_n,a_{n+1}$` we can assume without loss of generality that `$a_{n+1}\ge a_i$` for `$i=1,\ldots,n.$` 
   * It follows from the [inequality for weighted arithmetic mean][bookofproofs$8370] that `$\alpha:=\frac{a_1+\cdots+a_n}n\le a_{n+1}$`, which means that `$a_{n+1}-\alpha\ge 0$` and it follows (since `$(n+1)\alpha$` is positive) `$$x:=\frac{a_{n+1}-\alpha}{(n+1)\alpha}\ge 0.$$`
   * Note that `$(n+1)\alpha+a_{n+1}-\alpha=a_1+\cdots+a_{n+1}.$` Therefore we get with [Bernoulli's inequality][bookofproofs$590] `$$\begin{array}{rcl}\left(\frac{a_1+\cdots+a_{n+1}}{(n+1)\alpha}\right)^{n+1}&=&\left(\frac{(n+1)\alpha}{(n+1)\alpha}+\frac{a_{n+1}-\alpha}{(n+1)\alpha}\right)^{n+1}\\&=&(1+x)^{n+1}\\&\ge& 1+(n+1)x\\&=&\frac{a_{n+1}}{\alpha}\end{array}.$$`
   * This is equivalent to `$$\begin{array}{rcl}\left(\frac{a_1+\cdots+a_{n+1}}{(n+1)}\right)^{n+1}&\ge&\alpha^{n+1}\frac{a_{n+1}}{\alpha}=\alpha^n a_{n+1}\end{array}.$$`
   * Since by the induction assumption `$\alpha^n\ge a_1\cdots a_n,$` we get finally `$$\begin{array}{rcl}\left(\frac{a_1+\cdots+a_{n+1}}{(n+1)}\right)^{n+1}&\ge&a_1\cdots a_n a_{n+1}\end{array}.$$`
