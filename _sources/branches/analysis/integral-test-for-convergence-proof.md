layout: proof
categories: branches,analysis
nodeid: bookofproofs$8345
orderid: 50
parentid: bookofproofs$8344
title: 
description: PROOF OF INTEGRAL TEST FOR CONVERGENCE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: integral test for convergence,integral test,proof
contributors: bookofproofs

---


---

By hypothesis, `$N\in\mathbb N$` is a non-negativ [natural number][bookofproofs$718] ($N\ge 1$) and `$f:[N,\infty)\to\mathbb R$` is a [monotonically decreasing][bookofproofs$282] and [non-negative][bookofproofs$1107] function.

### "`$\Rightarrow$`"

* Assume, the [infinite series][bookofproofs$1109] `$$\sum_{n=N}^\infty f(n)$$` is [convergent][bookofproofs$175].
* By definition of [monotonically decreasing real-valued function][bookofproofs$282] for all natural numbers `$n\ge N$` we have that if `$n-1\ge x\ge n$` then `$f(n)\le x\le f(n-1).$` 
* With `$s:=\sup\{f(x)\mid n-1\ge x\ge n\}$` we get the estimation `$$f(n)\le\int_{n-1}^n f(x)dx\le s\cdot 1\le f(n-1).$$`
* The [sum][bookofproofs$261] for `$n=N+1,\ldots M$` yields `$$\sum_{n=N+1}^Mf(n)\le\int_{N}^M f(x)dx\le \sum_{n=N}^{M-1}f(n).\label{eq:E20282}\tag{1}$$`
* By assumption, the right side of the inequation `$(\ref{eq:E20282})$` converges to a constant for `$M\to\infty$`. Therefore, for all `$M\ge N$`, the [real sequence][bookofproofs$875] `$(r_M)_{M\in\mathbb N}$` of [Riemann integrals][bookofproofs$1763] `$$r_M:=\int_{N}^M f(x)dx$$` is [bounded above][bookofproofs$1136] by this constant. 
* Moreover, the left side of the inequation `$(\ref{eq:E20282})$` shows that the sequence `$(r_M)_{M\in\mathbb N}$` is [monotonically increasing][bookofproofs$1155], since all `$f(n)$` are by definition [non-negative][bookofproofs$1107].
* Since [every bounded monotonic sequence is convergent][bookofproofs$197] it follows that the [improper integral][bookofproofs$8343] `$$\int_{N}^\infty f(x)dx$$` is convergent.

### "`$\Leftarrow$`"

* Assume, `$\int_{N}^\infty f(x)dx$` is [convergent][bookofproofs$8343]. 
* Then, the left side of the inequation `$(\ref{eq:E20282})$` shows that the sequence `$(s_M)_{M\in\mathbb N}$` of the [partial sums][bookofproofs$1109] `$$s_M:=\sum_{n=N+1}^Mf(n)$$` is  [bounded above][bookofproofs$1136].
* Moreover, it is [monotonically increasing][bookofproofs$1155], since all `$f(n)$` are by definition [non-negative][bookofproofs$1107].
* It follows that it is a [convergent real sequence][bookofproofs$141].
* By definition of [convergent real series][bookofproofs$175], the series `$\sum_{N+1}^\infty f(n)$` is convergent and so is the series `$$\sum_{N}^\infty f(n).$$`
