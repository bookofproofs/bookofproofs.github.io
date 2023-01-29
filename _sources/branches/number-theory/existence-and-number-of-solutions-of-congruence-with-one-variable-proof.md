layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3527
orderid: 50
parentid: bookofproofs$8178
title: By Induction
description: PROOF OF EXISTENCE AND NUMBER OF SOLUTIONS OF CONGRUENCE WITH ONE VARIABLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: congruence,existence,number,one,solutions,variable,proof
contributors: bookofproofs

---


---

By hypothesis, `$a,b$` are [integers][bookofproofs$844], `$m > 0$` is a [positive integer][bookofproofs$1075]. We first show that the solvability of the [congruence][bookofproofs$8153] is equivalent to `$\gcd(a,m)\mid b.$`

### "`$\Rightarrow$`"

* Assume, the congruence with one variable `$(ax-b)(m)\equiv 0(m)$` is solvable.
   * Therefore, we have also `$(ax-b)(\gcd(a,m))\equiv 0(\gcd(a,m)).$`
   * Since the [greatest common divisor][bookofproofs$1280] `$\gcd(a,m)$` is a [divisor][bookofproofs$700] of both, `$a$` and `$m$`, we `$(-b)(\gcd(a,m)) \equiv 0(\gcd(a,m)).$`
   * It follows `$\gcd(a,m)\mid b.$`

### "`$\Leftarrow$`"

* Assume, `$\gcd(a,m)\mid b.$`
   * Consider the congruence with one variable `$$\frac{a}{\gcd(a,m)}x\equiv\frac{b}{\gcd(a,m)}\mod \frac{m}{\gcd(a,m)}.\label{eq:E18453}\tag{1}$$`
   * Note that `$\frac{a}{\gcd(a,m)}\perp \frac{m}{\gcd(a,m)}$` are [co-prime][bookofproofs$8093], by [generating co-prime numbers knowing the `$\gcd$`][bookofproofs$1289].
   * According to [congruences and division with quotient and remainder][bookofproofs$8155] (see also [explanation][bookofproofs$585]), the integers `$0,1,\ldots,m-1$` build a [complete residue system modulo `$m$`][bookofproofs$8173].
* According to [creation of complete residue systems from others][bookofproofs$8175], this holds also for the system `$c\cdot 0,c\cdot 1,\ldots,c\cdot(m-1)$` with `$c:=\frac{a}{\gcd(a,m)}.$`
* Therefore, the congruence with one variable `$(\ref{eq:E18453})$` has exactly one solution.
* With [multiplication of congruences with a positive factor][bookofproofs$8170], it follows that also the congruence `$(ax)(m)\equiv b(m)$` is solvable.

It remains to be shown that the congruence has exactly `$\gcd(a,m)$` different solutions. 
* The congruence with one variable `$(\ref{eq:E18453})$` has exactly one solution modulo `$\frac{m}{\gcd(a,m)}.$`
* Since `$\gcd(a,m)\mid m$`, there are `$\gcd(a,m)$` as many solutions modulo `$m.$`
