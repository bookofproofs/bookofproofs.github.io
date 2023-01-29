layout: proof
categories: branches,analysis
nodeid: bookofproofs$6902
orderid: 50
parentid: bookofproofs$6901
title: 
description: PROOF BY CONTRADICTION Proof of PRESERVATION OF INEQUALITIES FOR LIMITS OF FUNCTIONS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$6823
keywords: functions,inequalities,limits,preservation,limits and inequalities,limit inequalities,proof
contributors: bookofproofs

---


---

### Context

* Let `$D\subseteq\mathbb R$` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105].
* Let `$a\in\mathbb R$` be a [real number][bookofproofs$1105].
* Let `$f:D\to\mathbb R$` be a [function][bookofproofs$592] with the [limit][bookofproofs$6683] `$\lim_{x\to a}f=L.$` 

### Case 1: Let `$f(x) > 0$`  for all `$x\in D.$`

   * Hypothesis:
      * Assume `$L < 0.$`
   * Implications
      * By the [definition of limit][bookofproofs$6683], for `$\epsilon=-L$` there is a `$\delta > 0$` such that for all `$x\in D$` satisfying `$0 < |x-a| < \delta,$` it follows that `$|f(x)-L| < - L.$`
      * For these values of `$x$` we have `$-L > |f(x)-L| = f(x) - L,$` implifying that `$f(x) > 0$` and `$L < 0.$`
      * This creates the [contradiction][bookofproofs$744] to `$f(x) < 0.$` 
   * Conclusion
      * It must be that `$L\ge 0.$`

### Case 2: Let `$f(x) < 0$`  for all `$x\in D.$`

   * Hypothesis:
      * Assume `$L > 0.$`
   * Implications
      * By the [definition of limit][bookofproofs$6683], for `$\epsilon=L$` there is a `$\delta > 0$` such that for all `$x\in D$` satisfying `$0 < |x-a| < \delta,$` it follows that `$|f(x)-L| < L.$`
      * For these values of `$x$` we have `$L > |f(x)-L| = -f(x) + L,$` implifying that `$f(x) < 0$` and `$L > 0.$`
      * This creates the [contradiction][bookofproofs$744] to `$f(x) > 0.$` 
   * Conclusion
      * It must be that `$L\le 0.$`
