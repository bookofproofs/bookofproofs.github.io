layout: proof
categories: branches,algebra
nodeid: bookofproofs$6826
orderid: 0
parentid: bookofproofs$6825
title: 
description: PROOF OF QUADRATIC FORMULA &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: formula,quadratic,proof
contributors: bookofproofs

---


---

### Context

* Let `$p(x)=ax^2 + bx +c$` be a [polynomial][bookofproofs$487] [over the field][bookofproofs$487] `$F[X]$`, i.e. where the coefficients `$a,b,c$` are elements of some [field][bookofproofs$557] `$(F, + , \cdot).$`
* Let `$a\neq 0$`, i.e. `$p$` be of [degree][bookofproofs$487] `$2$`.
 

### Hypothesis

* Suppose, `$x$` satisfies `$p(x)=0.$`

### Implications

* Since `$a\neq 0$` and since `$F$` is a field, there exists an `$a^{-1}:=\frac 1a$` and we have `$x^2+\frac bax +\frac ca = 0.$`
* Adding the term `$\frac{b^2}{4a^2}$` on both sides of the equation gives us  `$x^2+\frac bax +\frac ca + \frac{b^2}{4a^2}= \frac{b^2}{4a^2}.$`
* The [binomial theorem][bookofproofs$1397] for `$n=2$` shows that `$\left(x+\frac{b}{2a}\right)^2+\frac ca=\frac{b^2}{4a^2}.$`
* Then `$\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac ca=\frac{b^2-4ac}{4a^2}.$`
* This means that `$x+\frac b{2a}=\pm\sqrt{\frac{b^2-4ac}{4a^2}}=\pm\frac{\sqrt{b^2-4ac}}{2a}$`.
* Finally, this means that `$x=\frac{-b \pm\sqrt{b^2-4ac}}{2a}.$`

### Conclusion

* It follows that the formula `$p(x)=0$` has exactly two [roots][bookofproofs$6736] given by 
`$$x_1:=\frac{-b + \sqrt{b^2-4ac}}{2a},\quad x_2:=\frac{-b\; - \sqrt{b^2-4ac}}{2a}.$$`
