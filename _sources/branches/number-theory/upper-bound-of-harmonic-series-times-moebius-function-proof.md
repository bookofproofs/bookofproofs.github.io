layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8148
orderid: 50
parentid: bookofproofs$8147
title: 
description:  Proof of UPPER BOUND OF HARMONIC SERIES TIMES MöBIUS FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: bound,function,harmonic,moebius,series,times,upper,proof
contributors: bookofproofs

---


---

* Let `$x \ge 1$` be a [real number][bookofproofs$1105], for which we want to estimate the [partial sum][bookofproofs$1109].
`$$\left|\sum_{n=1}^x\frac{\mu(n)}{n}\right|\le ?.$$`
* By definition of the [floor function][bookofproofs$280], we have the estimation `$$0\le\frac{x}{n}-\left\lfloor\frac{x}{n}\right\rfloor\begin{cases}
< 1&\text{ for }1\le n < x\\
=0&\text{ for }n = x.\end{cases}$$`
* Multiplying these terms by the [Möbius function][bookofproofs$8116] `$\mu(n)$` and building the [sum][bookofproofs$261] for `$n\le x$` gives us with the lemma about [Möbius and floor functions combined][bookofproofs$8144]:
`$$\sum_{n=1}^x\mu(n)\left(\frac{x}{n}-\left\lfloor\frac{x}{n}\right\rfloor\right)=x\sum_{n=1}^x\frac{\mu(n)}{n}-\sum_{n=1}^x\mu(n)\left\lfloor\frac{x}{n}\right\rfloor=x\sum_{n=1}^x\frac{\mu(n)}{n}-1.$$`
* With the [triangle inequality][bookofproofs$588] and because `$\mu(n)\le 1$` for all `$n\ge 1,$` we get the estimation
`$$\begin{array}{rcl}
\left|x\sum_{n=1}^x\frac{\mu(n)}{n}-1\right|&=&\left|\sum_{n=1}^x\mu(n)\left(\frac{x}{n}-\left\lfloor\frac{x}{n}\right\rfloor\right)\right|\\
&\le&\sum_{n=1}^x\left(\frac{x}{n}-\left\lfloor\frac{x}{n}\right\rfloor\right)\\
&\le&x-1.
\end{array}$$`
* Bringing the term `$-1$` on the other side of the inequation results in
`$$\begin{array}{rcl}
\left|x\sum_{n=1}^x\frac{\mu(n)}{n}\right|&\le&1+(x-1)=x.
\end{array}$$`
* Dividing both sides of the inequation by `$x$` results in the required [upper bound][bookofproofs$584].
`$$\begin{array}{rcl}
\left|\sum_{n=1}^x\frac{\mu(n)}{n}\right|&\le&1.
\end{array}$$`
* This upper bound holds for all partial sums depending on `$x\ge 1,$` therefore also for the whole infinite series.[^1]

[^1]: The existence of such an upper bound means that the above series either converges or oscillates in the real interval `$[-1,1].$` Which of these two cases is true, can be proven but requires more sophisticated methods we will introduce in [analytic number theory][bookofproofs$72]. Anticipating the right answer, the series converges and its limit is `$0.$`
