layout: proof
categories: branches,analysis
nodeid: bookofproofs$6888
orderid: 50
parentid: bookofproofs$6884
title: 
description:  Proof of ARITHMETIC OF FUNCTIONS WITH LIMITS - DIFFERENCE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: limit of difference,proof
contributors: bookofproofs

---


---

### Context

* Let `$D\subseteq R$` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105] with an [accumulation point][bookofproofs$174] `$a.$` 
* Let `$f,g:D\to\mathbb R$` be [functions][bookofproofs$592].
### Hypothesis

* Let `$f,g$` have the limits `$\lim_{x\to a}f(x)=L$` and `$\lim_{x\to a}g(x)=H.$` 
* Given `$\epsilon > 0.$`

### Implications

* By the [definition of limit][bookofproofs$6683]:
   * there is a `$\delta_1 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_1,$` then `$|f(x)-L|\le \frac \epsilon2,$` and 
   * there is a `$\delta_2 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_2,$` then `$|g(x)-H|\le \frac \epsilon2.$`
* Get the [minimum][bookofproofs$6603] `$\delta=\min(\delta_1,\delta_2).$`
* Note that `$\delta > 0.$`
* Since `$f-g:D\to\mathbb R,$` we have that if `$x\in D$` with `$0 < |x-a| < \delta,$` then by the [triangle inequality][bookofproofs$588].
`$$\begin{array}{rcl}|(f(x)-g(x))-(L-H)|&=&|(f(x)-L)-(g(x)-H)|\\
&=&|(f(x)-L)+(-g(x)+H)|\\
&\le&|f(x)-L|+|-(g(x)-H)|\\
&=&|f(x)-L|+|g(x)-H|\\
& < & \frac \epsilon2 + \frac \epsilon2\\
&=&\epsilon\end{array}.$$`

### Conclusion

* By the [definition of limit][bookofproofs$6683], this shows that the limit of the [difference][bookofproofs$1588] of both functions is given by `$\lim_{x\to a}(f(x)-g(x))=L-H.$`
