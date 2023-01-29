layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$7833
orderid: 50
parentid: bookofproofs$7832
title: 
description:  Proof of ORDER RELATION FOR RATIONAL NUMBERS IS STRICT TOTAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: numbers,order,rational,relation,strict,total,transitivity,trichotomy,strict total order,total order relation,proof
contributors: bookofproofs

---


---

In order to avoid complicated distinctions of cases, we can without loss of generality assume the integers `$a,b,c,d,e,f\in Z$` to be all [positive integers][bookofproofs$1075].
We first show the trichotomy of the  [order relation][bookofproofs$1076] "`$<$`"  for [rational numbers][bookofproofs$1033] `\(\frac ab,\frac cd, \in\mathbb Q\)`:

* By the definition of the [order relation for rational numbers][bookofproofs$1076],
   * `$\frac ab < \frac cd$` is equivalent to `$\frac ab - \frac cd < 0$`,
   * `$\frac ab > \frac cd$` is equivalent to `$\frac ab - \frac cd > 0$`, and
   * `$\frac ab = \frac cd$` is equivalent to `$\frac ab - \frac cd = 0$`.
* Therefore, the order relation of rational numbers "`$<$`" can be reduced to the [order relation for integers][bookofproofs$1075] "`$<$`".
* Now, the trichotomy of the order relation for rational numbers follows from the [trichotomy of the order relation for integers][bookofproofs$7830].
* Therefore, only one of the cases `$\frac ab = \frac cd$`, or `$\frac ab < \frac cd$`, or `$\frac ab > \frac cd$` can occur at once.

We now show the transitivity.

* Let `$\frac ab < \frac cd$` and `$\frac cd < \frac ef$`.
* It follows `$\frac ab - \frac cd < 0$` and `$\frac cd - \frac ef < 0$`.
*  [Adding both sides of the inequations in the set of rational numbers][bookofproofs$1446] results in `$\frac ab- \frac cd + \frac cd- \frac ef  < 0$`.
* The [existence of inverse rational numbers with respect to additions][bookofproofs$1509] results in `$\frac ab- \frac ef  < 0$`.
* This means that `$\frac ab < \frac ef$`.
