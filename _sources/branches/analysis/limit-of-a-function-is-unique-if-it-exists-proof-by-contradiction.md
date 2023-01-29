layout: proof
categories: branches,analysis
nodeid: bookofproofs$6904
orderid: 50
parentid: bookofproofs$6903
title: 
description: PROOF BY CONTRADICTION Proof of LIMIT OF A FUNCTION IS UNIQUE IF IT EXISTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: exists,function,limit,unique,proof
contributors: bookofproofs

---


---

### Context

* Let `$D\subseteq\mathbb R$` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105].
* Let `$f:D\to\mathbb R$` be a [function][bookofproofs$592].
* Let `$a\in\mathbb D.$`

### Hypothesis

* Assume, the [limit][bookofproofs$6683] `$\lim_{x\to a} f(x)$` exists, but it not unique, e.g. `$\lim_{x\to a} f(x)=L$` and `$\lim_{x\to a} f(x)=M$` but `$L\neq M.$`

### Implications

* Since `$L\neq M$`, then `$|M - L| > 0.$`
* By the [definition of limit][bookofproofs$6683], there is a `$\delta_1 > 0$` such that for all `$x\in D$` satisfying `$0 < |x - a| < \delta_1,$` it follows that `$|f(x) - L| < \frac{|M-L|}{2}.$`
* Similarly, there is a `$\delta_2 > 0$` such that for all `$x\in D$` satisfying `$0 < |x - a| < \delta_2,$` it follows that `$|f(x) - M| < \frac{|M-L|}{2}.$`
* Take the [minimum][bookofproofs$6603] `$\delta:=\min(\delta_1,\delta_2)$` and select `$x\in D$` with `$0 < |x-a| < \delta.$`
* Then it follows by the [triangle inequality][bookofproofs$588] that `$$\begin{array}{rcl}|M-L|&=&\frac{|M-L|}{2}+\frac{|M-L|}{2}\\
&>& |f(x) - L| + |f(x) - M|\\
&=&|f(x)-L| + |M-f(x)|\\
&\ge&|f(x)-L+M-f(x)|\\
&=&|M-L|.\end{array}$$`
* This leads to the [contradiction][bookofproofs$744] `$|M-L| > |M-L|.$` 

### Conclusion

* Therefore, `$L\neq M$` must be wrong and we have `$L=M.$`
