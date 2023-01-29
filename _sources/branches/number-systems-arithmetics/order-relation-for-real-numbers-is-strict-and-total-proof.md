layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$7835
orderid: 50
parentid: bookofproofs$7834
title: 
description:  Proof of ORDER RELATION FOR REAL NUMBERS IS STRICT AND TOTAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: numbers,order,real,relation,strict,total,transitivity,trichotomy,proof
contributors: bookofproofs

---


---

We first show that the  [order relation for real numbers][bookofproofs$1107] "$ < `$" is a trichotomy.

* Let `$x,y\in \mathbb R$` be any [real numbers][bookofproofs$1105] represented by the equivalence classes of some [rational Cauchy sequences][bookofproofs$1485] `$(x_n)_{n\in\mathbb N}+ I$` and  `$(y_n)_{n\in\mathbb N}+ I$`.
* It follows from the definition of the order relation for real numbers that
   * `$x < y$` is equivalent to `$x-y < 0$`, which is equivalent to the existence of some `$N\in\mathbb N$` such that `$x_n-y_n < 0$` for all `$n > N$`.
   * `$x > y$` is equivalent to `$x-y > 0$`, which is equivalent to the existence of some `$N\in\mathbb N$` such that `$x_n-y_n > 0$` for all `$n > N$`.
   * `$x = y$` is equivalent to  `$x-y = 0$`, which is equivalent to `$(x_n-y_n)_{n\in\mathbb N}$` being a rational Cauchy sequence converging to `$0$`.
* Please note that in the terms `$x_n-y_n < 0$` and `$x_n-y_n > 0$`  we have reduced the order relations of real numbers "`$x < y$`" and "`$x > y$`" to the [order relations of rational numbers][bookofproofs$1076] "$x_n < y_n$" and "$x_n > y_n$", respectively.
* Therefore, from the [trichotomy of the order relation for rational numbers][bookofproofs$7832], the trichotomy for the order relation for real numbers follows.
* Therefore, for any two given real numbers `$x,y$`, only one of the following cases can occure at once:
   * Either `$x=y$`, or
   * `$x > y$`, or
   * `$x < y.$`

Now, we show the transitivity.

* Let `$x < y$` and `$y < z$`.
* It follows `$x - y < 0$` and `$y - z < 0$`.
*  [Adding both sides of the inequations in the set of real numbers][bookofproofs$1514] results in `$x-y+y-z< 0$`.
* The [existence of inverse real numbers with respect to addition][bookofproofs$35] results in `$x- z  < 0$`.
* This means that `$x < y$`.
* The transitivity of "`$>$`", "`$\ge$`", and "`$\le$`" follows analogously.
