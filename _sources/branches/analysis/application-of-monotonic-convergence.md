layout: application
categories: branches,analysis
nodeid: bookofproofs$6869
orderid: 100
parentid: bookofproofs$197
title: Application of Monotonic Convergence
description: APPLICATION OF MONOTONIC CONVERGENCE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6823
keywords: application of monotonic convergence
contributors: bookofproofs

---
The [theorem of monotonic convergence][bookofproofs$197] is very useful to prove that a given [sequence][bookofproofs$875] is [convergent][bookofproofs$141], without having to find the actual limit of the convergent sequence. The following example demonstrates this.

---

* Consider a sequence `$(a_n)_{n\in\mathbb N}$` defined by
`$$a_0:=2,\quad\quad a_{n+1}:=\sqrt{a_n + 12}$$`
for all `$n\ge 0.$` 
* Then, `$a_0=2 < \sqrt{14} < a_1.$` 
   * Suppose that for some _fixed_ `$n\ge 0$` we have `$a_n < a_{n+1}$`.
   * Then it follows from `$a_n + 12 < a_{n+1} + 12$` that `$\sqrt{a_n + 12} < \sqrt{a_{n+1} + 12}$`, i.e. that `$a_{n+1} < a_{n+2}$`. 
   * By [induction][bookofproofs$744], this means that `$a_n < a_{n+1}$` _for all_ `$n\ge 0.$` 
   * Thus, the sequence `$(a_n)_{n\in\mathbb N}$` is [strictly monotonically increasing][bookofproofs$1155].
* Similarly, `$a_0=2 < 4.$` 
   * Suppose that _for some fixed_ `$n\ge 0$` we have `$a_n < 4$`. 
   * Then it follows from `$a_{n+1}=\sqrt{a_n + 12} < \sqrt{4 + 12} = \sqrt{16} = 4.$` 
   * By [induction][bookofproofs$744], this means that `$a_n < 4$` _for all_ `$n\ge 0.$` 
   * Thus, the sequence `$(a_n)_{n\in\mathbb N}$` is [bounded from above][bookofproofs$1136].
* Now, the [theorem of monotonic convergence][bookofproofs$197] tells us that the sequence `$(a_n)_{n\in\mathbb N}$` is [convergent][bookofproofs$141], even though we haven't calculated its limit.[^1]

[^1]: It can be proven that its limit is actually the number `$4$`, which has been used as the upper bound to show that the sequence is bounded from above.
