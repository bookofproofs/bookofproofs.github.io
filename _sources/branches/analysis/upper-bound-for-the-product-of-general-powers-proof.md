layout: proof
categories: branches,analysis
nodeid: bookofproofs$2918
orderid: 50
parentid: bookofproofs$6787
title: 
description: PROOF OF UPPER BOUND FOR THE PRODUCT OF GENERAL POWERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: upper bound for the product of general powers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$x,y$` are [positive numbers][bookofproofs$1107], and `$p,q\in(1,\infty)$` with `$\frac 1p+\frac 1q=1$`.
* The [second derivative][bookofproofs$1370] of the [natural logarithm][bookofproofs$1421] is [negative][bookofproofs$1107] `$\log^{\prime\prime}(x)=-\frac 1{x^2} < 0$` for all positive numbers `$x > 0.$` 
* Thus, the natural logarithm fulfills the [test for concaveness][bookofproofs$6786].
* Since by definition `$\frac 1p,\frac 1q\in(0,1),$` `$\frac 1p+\frac 1q=1,$` we get by [definition of concave][bookofproofs$6785] the following inequality `$$\log\left(\frac 1px+\frac 1qy\right)\ge \frac 1p\log(x)+\frac 1q\log(y).$$`
* Taking the [exponential function][bookofproofs$281] on both sides of the inequation[^1] yields 
`$$\frac xp+\frac yq\ge x^{1/p}\cdot y^{1/q}.$$`

[^1]: Note that the exponential function is the inverse function to the logarithm.
