layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8514
orderid: 50
parentid: bookofproofs$8513
title: 
description: PROOF OF FUNDAMENTAL THEOREM OF DIFFERENCE CALCULUS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8404
keywords: fundamental theorem of difference calculus,proof
contributors: bookofproofs

---


---

* By hypothesis, `$F:D\to\mathbb C$` is an [antidifference][bookofproofs$8506] of a [complex-valued][bookofproofs$216]  [function][bookofproofs$592] `$f:C\to\mathbb C$`, `$D\subseteq\mathbb C.$` 
* Let `$a,b\in\mathbb C$` and let `$n\in\mathbb N$` be a [natural number][bookofproofs$718].
* By hypothesis, `$F$` equals the [indefinite sum][bookofproofs$8506] `$F(x)=\sum f(x).$` 
* Thus, its [difference operator][bookofproofs$8408] equals `$\Delta F(x)=f(x).$`
* By definition of the difference operator, we have `$\Delta F(x)=F(x+1)-F(x).$`
* Hence, `$$\begin{array}{lcl}
F(a+1)-F(a)&=&f(a)\\
F(a+2)-F(a+1)&=&f(a+1)\\
\vdots&=&\vdots\\
F(a+n-1)-F(a+n-2)&=&f(a+n-2)\\
F(a+n)-F(a+n-1)&=&f(a+n-1)\\
\end{array}$$`
* Adding up both sides of the above equations, we get
`$$F(a+n)-F(a)=\sum_{x=a}^{a+n-1}f(x).$$`
