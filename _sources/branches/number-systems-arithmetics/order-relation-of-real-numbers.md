layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1107
orderid: 500
parentid: bookofproofs$167
title: Order Relation of Real Numbers
description: ORDER RELATION FOR REAL NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: negative real number,numbers,order,order relation for real numbers,positive real number,real,relation,order of real numbers,order relation,real numbers definition,real number definition,positive real numbers,definition of real numbers,ordering real numbers,order relation on real numbers,non-negative,ordered,real numbers,positive numbers,negative
contributors: bookofproofs

---


---

According to the [definition of real numbers][bookofproofs$1105], any real number `\(x \in\mathbb R\)` can be represented as residue classes of [rational Cauchy sequences][bookofproofs$1485]:
`$$\begin{array}{ccl}
x&=&(x_n)_{n\in\mathbb N} + I.
\end{array}$$`

Based on the [order relation for rational numbers][bookofproofs$1076], we have tree cases of representing a real number, called:
* **positive real number** `$x > 0$`,  if and only if  there is an `$N\in\mathbb N$` such that `$x_n > 0$` for all `$n > N,$`[^1]
* [zero][bookofproofs$34] `$x=0$`, if and only if for all rational `$\epsilon > 0$` there is an `$N\in\mathbb N$` such that `$-\epsilon < x_n < \epsilon$` for all `$n > N,$` 
* **negative real number** `$x < 0$`, if and only if there is an `$N\in\mathbb N$` such that `$x_n < 0$` for all `$n > N.$`  

Using the [definition of subtraction of real numbers][bookofproofs$1588], we can define the **order relation for real numbers** as follows:
* `$x > y$` if and only if `$x-y > 0,$`
* `$x = y$` if and only if `$x-y = 0,$`
* `$x < y$` if and only if `$x-y < 0.$`

### Notation

* The set of all positive real numbers is denoted by `$\mathbb R^+.$`
* The set of all negative real numbers is denoted by `$\mathbb R^-.$`

[^1]: The first `$0$` in all three cases means the [real zero][bookofproofs$34], the second `$0$` is the [rational zero][bookofproofs$1473]).
