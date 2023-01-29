layout: proof
categories: branches,analysis
nodeid: bookofproofs$8441
orderid: 50
parentid: bookofproofs$8440
title: By Induction
description: PROOF OF TAYLOR'S FORMULA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: taylor's formula,proof
contributors: bookofproofs

---


---

* By hypothesis, `$I\subset\mathbb R$` is an [interval][bookofproofs$1153] and `$f:I\to\mathbb R$` is a [$(n+1)$ times continuously differentiable function][bookofproofs$6205] where `$n\ge 0$` is a [natural number][bookofproofs$718].
* Let `$a,x\in I,$` and `$n!$` denote the [factorial][bookofproofs$1005], and `$f^{\{n\}}$` denote the `$n$`-th derivative. We prove the statement [by induction][bookofproofs$657] on `$n.$`
* Base case `$n=0$`
   * The [fundamental theorem of calculus][bookofproofs$6807] gives us `$$f(x)=f(a)+\int_a^x f^{\prime}(t)dt.$$`
* Induction step `$n\to n+1$`
   * By the induction hypothesis and[^1] by [integration by parts][bookofproofs$8337] `$$\begin{align}
R_n(x)&=\frac 1{(n-1)!}\int_a^x (x-t)^{n-1}f^{\{n\}}(t)dt\nonumber\\
&=-\int_a^xf^{\{n\}}\frac{d}{dt}\left(\frac{(x-t)^n}{n!}\right)dt\nonumber\\
&=-f^{\{n\}}(t)\frac{(x-t)^n}{n !}\;\Rule{1px}{4ex}{2ex}^{t=b}_{t=a}+\int_a^x \frac{(x-t)^n}{n !}df^{\{n\}}(t)\nonumber\\
&=\frac{f^{\{n\}}(a)}{n !}(x-a)^n+\frac 1{n !}\int_a^x (x-t)^{n}f^{\{n+1\}}(t)dt\nonumber\\
&=R_{n+1}(x)\nonumber
\end{align}$$`
* It follows for all `$n\ge 0$` that
`$$f(x)=f(a)+\sum_{k=1}^n \frac{f^{\{k\}}(a)}{k!}(x-a)^k+R_{n+1}(x).$$`

[^1]: In the mnemonic notation of the partial integration, `$\int fdg=fg-\int gdf$` replace `$f$` by `$f^{\{n\}}$` and `$g$` by `$\frac{(x-t)^n}{n!}.$`
