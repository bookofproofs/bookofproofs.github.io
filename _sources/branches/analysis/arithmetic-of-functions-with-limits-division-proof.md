layout: proof
categories: branches,analysis
nodeid: bookofproofs$6890
orderid: 50
parentid: bookofproofs$6886
title: 
description:  Proof of ARITHMETIC OF FUNCTIONS WITH LIMITS - DIVISION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: arithmetic,division,functions,limits,proof
contributors: bookofproofs

---


---

### Context

* Let `$D\subseteq R$` be a [subset][bookofproofs$552] of [real numbers][bookofproofs$1105] with an [accumulation point][bookofproofs$174] `$a.$` 
* Let `$f,g:D\to\mathbb R$` be [functions][bookofproofs$592].
### Hypothesis

* Let `$f,g$` have the limits `$\lim_{x\to a}f(x)=L$` and `$\lim_{x\to a}g(x)=H.$` 
* Let `$H\neq 0.$`
* Given `$\epsilon > 0.$`

### Implications

* By the [definition of limit][bookofproofs$6683]:
   * there is a `$\delta_1 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_1,$` then `$|g(x)-H| < \frac {|H|}{2}.$` For these `$x$` it follows from the [triangle inequality][bookofproofs$588] that 
`$$\begin{array}{rcl}|g(x)| + \frac{|H|}2 & > & |g(x)|+|g(x)-H|\\
&=&|g(x)|+|H-g(x)|\\
&\ge &|g(x)+(H-g(x))|\\
&=&|H|,\end{array}$$` 
which implies `$|g(x)| > \frac{|H|}2,$` and 
   * there is a `$\delta_2 > 0$` such that if `$x\in D$` and `$0 < |x-a| < \delta_2,$` then `$|f(x)-L| < \frac {\epsilon\cdot |H|}{4}.$`
   * Moreover, there is a `$\delta_3 > 0$` sucht that if `$x\in D$` and `$0 < |x-a| < \delta_3,$` then `$|g(x)-H| < \frac{\epsilon\cdot H^2}{4(|L|+1)}.$` 
* Get the [minimum][bookofproofs$6603] `$\delta=\min(\delta_1,\delta_2,\delta_3).$`
* Note that `$\delta > 0.$`
* Since `$\frac fg:D\to\mathbb R,$` we have that if `$x\in D$` with `$0 < |x-a| < \delta,$` then by the [triangle inequality][bookofproofs$588].
`$$\begin{array}{rcl}\left|\frac{f(x)}{g(x)}-\frac LH\right|&=&\left|\frac{f(x)\cdot H-L\cdot g(x)}{g(x)\cdot H}\right|\\
&=&\left|\frac{f(x)\cdot H-L\cdot H+L\cdot H-L\cdot g(x)}{g(x)\cdot H}\right|\\
&=&\left|\frac{(f(x)-L)\cdot H+L\cdot(H-g(x))}{g(x)\cdot H}\right|\\
&\le&\frac{|(f(x)-L)}{|g(x)|}+\left|\frac{L(g(x)-H)}{g(x)\cdot H}\right|\\
& < & \frac{e\cdot |H|}{4}\cdot \frac{2}{|H|} + \frac{\epsilon\cdot H^2}{4(|L|+1)}\cdot\frac{2|L|}{H^2}\\
& < & \frac \epsilon2 + \frac \epsilon2\\
&=&\epsilon\end{array}.$$`


### Conclusion

* By the [definition of limit][bookofproofs$6683], this shows that the limit of the [quotient][bookofproofs$6635] of both functions is given by `$\lim_{x\to a}\frac{f(x)}{g(x)}=\frac LH.$`
