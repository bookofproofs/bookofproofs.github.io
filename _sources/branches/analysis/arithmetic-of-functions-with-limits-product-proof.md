layout: proof
categories: branches,analysis
nodeid: bookofproofs$6889
orderid: 50
parentid: bookofproofs$6885
title: 
description:  Proof of ARITHMETIC OF FUNCTIONS WITH LIMITS - PRODUCT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: arithmetic,functions,limits,product,proof
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
   * there is a `$\delta_1 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_1,$` then `$|f(x)-L|\le \frac \epsilon{2(|H|+1)},$` and 
   * there is a `$\delta_2 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_2,$` then `$|g(x)-H|\le \frac \epsilon{2(|L|+1)}.$`
   * Moreover, there is a `$\delta_3 > 0$` sucht that if `$x\in D$` and `$0 < |x-a| < \delta_3,$` then `$|f(x)-L| < 1.$` Thus, by the [triangle inequality][bookofproofs$588], `$|f(x)|=|L-(f(x)-L)|\le |L|+|f(x)-L| < |L| + 1.$`
* Get the [minimum][bookofproofs$6603] `$\delta=\min(\delta_1,\delta_2,\delta_3).$`
* Note that `$\delta > 0.$`
* Since `$f\cdot g:D\to\mathbb R,$` we have that if `$x\in D$` with `$0 < |x-a| < \delta,$` then by the [triangle inequality][bookofproofs$588].
`$$\begin{array}{rcl}|(f(x)\cdot g(x))-(L\cdot H)|&=&|f(x)g(x)-f(x)H+f(x)H-LH)|\\
&=&|(f(x)(g(x)-H)+H(f(x)-L)|\\
&\le&|(f(x)(g(x)-H)|+|H(f(x)-L)|\\
&=&|(f(x)|\cdot |(g(x)-H)|+|H|\cdot |(f(x)-L)|\\
&=&||L|+1|\cdot\frac{\epsilon}{2(|L|+1)}+|H|\cdot\frac{\epsilon}{2(|H|+1)}\\
& < & \frac \epsilon2 + \frac \epsilon2\\
&=&\epsilon\end{array}.$$`


### Conclusion

* By the [definition of limit][bookofproofs$6683], this shows that the limit of the [product][bookofproofs$1532] of both functions is given by `$\lim_{x\to a}(f(x)\cdot g(x))=L\cdot H.$`
