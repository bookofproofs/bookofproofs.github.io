layout: definition
categories: branches,number-theory
nodeid: bookofproofs$700
orderid: 50
parentid: bookofproofs$77
title: Divisor, Complementary Divisor, Multiple
description: DIVISOR, COMPLEMENTARY DIVISOR, MULTIPLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: complementary,divisibility,divisor,multiple,non-trivial divisor,proper divisor,complementary definition,divisor definition,complementary meaning,divisor meaning,define divisor,definition of divisor,complimentary definition,divisible,multiples,divisors
contributors: bookofproofs

---


---

*Divisibility* is a [relation][bookofproofs$571] `$R\subseteq \mathbb Z \times \mathbb Z$` denoted by the sign "`$\mid$`" and defined as follows:

`$$d\mid n:=\Leftrightarrow\exists m\in\mathbb Z\;\; d\cdot m=n\wedge d\neq 0.\label{E18333}\tag{1}$$`

In other words, for two [integers][bookofproofs$844] `$n,d\in\mathbb Z$` with `$d\neq 0$` `$d$` is a **divisor** of `$n$`, denoted by `$d\mid n$` if and only if there is an `\(m\in\mathbb Z\)` with `\(dm=n\)`. In order to indicate that `\(d\)` is a divisor of `\(n\)` we write `\(d\mid n\)`, otherwise we write `\(d\not\mid n\)`. 

There are some related concepts, which shall be introduced here also:

* The integer `\(m=\frac nd\)` (if it exists) is unique and called **complementary divisor** of `\(d\)` with respect to `\(n\)`.
* The number `$n$` is called the **multiple** of `$d$` and `$m.$`[^1]
* A divisor `\(d\mid n\)` is called a **trivial divisor** of `\(n\)`, if `\(d=1\)` or `\(d=n\)`, otherwise, it is called a *non-trivial divisor*.
* A **proper divisor** of `\(n\)` is a non-trivial divisor `\(d\mid n\)` with `\(d\neq n.\)`

[^1]: Please note that multiples of `\(d=0\)` are undefined. Although `\(0\cdot m=0\)` is fulfilled for any `\(m\)`, we cannot say that `\(0\mid 0\)`, since `\(0\)` is not a divisor of any number (because by definition `$\ref{E18333},$` it cannot be for `$d=0$`). We want to have a definition of multiples which is complementary to the definition of divisors.
