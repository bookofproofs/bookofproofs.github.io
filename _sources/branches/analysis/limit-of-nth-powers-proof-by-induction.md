layout: proof
categories: branches,analysis
nodeid: bookofproofs$6896
orderid: 50
parentid: bookofproofs$6895
title: By Induction
description: PROOF BY INDUCTION Proof of LIMIT OF NTH POWERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: limit,nth,powers,proof
contributors: bookofproofs

---


---

### Context

* Let `$n\ge 1$` be a [natural number][bookofproofs$718].
* Let `$f:\mathbb R\to\mathbb R,$` `$f(x)=x^n$` be a [$n$-th power function][bookofproofs$6680].
* Let `$a\in\mathbb R$` be a [real number][bookofproofs$1105].
* It follows a proof by [induction][bookofproofs$657] on `$n$` for the [limit][bookofproofs$6683] `$$\lim_{x\to a }f(x)=\lim_{x\to a }x^n=a^n.$$`

### Base Case

* When `$n=1$`, the statement says that `$\lim_{x\to a}x^1=\lim_{x\to a} x = a$`. This follows from the [limit of the identify function][bookofproofs$6893].
### Hypothesis

* Assume that for some natural number `$k$`, `$\lim_{x\to a}x^k=a^k$` is true.

### Induction Step

* According to the [proposition of limit of the product][bookofproofs$6885], it follows that `$$\lim_{x\to a}x^{k+1}=\lim_{x\to a}x^{k}\cdot x=(\lim_{x\to a}x^k)\cdot (\lim_{x\to a}x)=a^k\cdot a=a^{k+1}.$$`
* Thus, the statement ist true for `$n=k+1.$`

### Conclusion

* By [induction][bookofproofs$657], `$$\lim_{x\to a }f(x)=\lim_{x\to a }x^n=a^n$$` is true for all `$n\ge 1.$`
