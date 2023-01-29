layout: proof
categories: branches,analysis
nodeid: bookofproofs$8379
orderid: 50
parentid: bookofproofs$8378
title: 
description: PROOF OF GAMMA FUNCTION INTERPOLATES THE FACTORIAL ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: gamma function,gamma functions,gamma,proof,proof
contributors: bookofproofs

---


---

* By hypothesis, `$x > 0$` is a [positive real number][bookofproofs$1107].
* Assume `$R > \epsilon > 0.$`
* By definition of the [gamma function][bookofproofs$457], `$\Gamma(x+1):=\int_0^\infty \exp(-t)t^{x}dt.$`
* In particular, the [improper integral][bookofproofs$8343] of the Gamma function `$G(x+1)$` is the [limit][bookofproofs$6683] `$\epsilon\searrow 0,$` and `$R\to\infty$` of the [Riemann integral][bookofproofs$1763] `$\int_\epsilon^R \exp(-t)t^{x}dt.$`
* By [partial integration][bookofproofs$8337] `$$\int_\epsilon^R \exp(-t)t^{x}dt=\underbrace{-\exp(-t)t^{x}\;\Rule{1px}{4ex}{2ex}^{t=R}_{t=\epsilon}}_{=:A}+x\int_\epsilon^R \exp(-t)t^{x-1}dt.$$`
* For `$\epsilon\searrow 0,$` and `$R\to\infty$`, the term `$A$` converges to `$$\lim_{\substack{\epsilon\searrow 0,\\ R\to\infty}}=-\frac{R^x}{\exp( R)}+\frac{\epsilon^x}{\exp(\epsilon)}=-0+0=0,$$` and this yields the functional equation `$$\Gamma(x+1)=x\Gamma(x).$$`
* Because `$$\Gamma(1)=\lim_{R\to\infty}\int_0^R\exp(-t)dt=\lim_{R\to\infty}(-\exp(-R)+1)=1,$$` for all [natural numbers][bookofproofs$718] `$n\in\mathbb N$` the above functional equation yields the interpolation of the [factorial][bookofproofs$1005].
`$$\Gamma(n+1)=n\Gamma(n)=n(n-1)\Gamma(n-1)=n(n-1)\cdots 1\cdot\Gamma(1)=n!.$$`
