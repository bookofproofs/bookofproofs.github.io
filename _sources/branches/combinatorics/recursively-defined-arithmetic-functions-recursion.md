layout: proposition
categories: branches,combinatorics
nodeid: bookofproofs$8679
orderid: 60000
parentid: bookofproofs$264
title: Recursively Defined Arithmetic Functions, Recursion
description: RECURSIVELY DEFINED ARITHMETIC FUNCTIONS, RECURSION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$977
keywords: recursively defined function,recursion,recursively defined,recursively defined functions,recursions
contributors: bookofproofs

---


---

An [arithmetic function][bookofproofs$8112] `$f:\mathbb N\to\mathbb C$` can be defined by specifying
1. the **initial values** of `$f(m)$` for all `$m\le N$` and some [natural number][bookofproofs$718] `$N\in\mathbb N,$` and
1. the **recursion formula** `$f(n)=\mathcal R(f(m)\mid m < n)$` for all `$n > N.$`

### Examples

* [factorial][bookofproofs$1005] function `$f:\mathbb N\to\mathbb N:$`
   * `$N:=0,$`
   * initial value `$f(0):=1,$`
   * recursion formula `$f(n):=n\cdot f(n-1).$`
* [Fibonacci][bookofproofs$498] function `$f:\mathbb N\to\mathbb N:$`
   * `$N:=2,$`
   * initial values `$f(0):=0, f(1):=1, f(2):=1,$`
   * recursion formula `$f(n):=f(n-1)+f(n+2).$`
* Mandelbrot function `$f:\mathbb N\to\mathbb C:$`
   * `$N:=0,$`
   * initial value `$f(0):=0,$`
   * recursion formula `$f(n):=f(n-1)^2+c$` for some complex number `$c\in\mathbb C.$`
