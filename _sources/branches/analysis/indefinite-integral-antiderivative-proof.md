layout: proof
categories: branches,analysis
nodeid: bookofproofs$1774
orderid: 50
parentid: bookofproofs$1768
title: 
description:  Proof of INDEFINITE INTEGRAL, ANTIDERIVATIVE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: antiderivative,indefinite,indefinite integral,integral,proof
contributors: bookofproofs

---


---

We want to show that on the [close interval][bookofproofs$1153] `\([a,x]\)`, the indefinite integral `\(F(x):=\int_a^x f(t)dt\)` of a [continuous real function][bookofproofs$1260] `\(f\)` is [differentiable][bookofproofs$1370], and that its derivative is `\(F'=f\)`. Note, that continuity is a [sufficient condition][bookofproofs$1766] for `\(f\)` to be [Riemann integrable][bookofproofs$1763]. Therefore, the integral `\(F(x):=\int_a^x f(t)dt\)` exists. 

Let `\(h\neq 0\)`. By definition, the derivative is given by  

`\[F'(x):=\lim_{h\to 0}\frac {F(x+h)-F(x)}{h}.\]` 

It follows from the [linearity of the Riemann integral][bookofproofs$1769].
`\[\frac {F(x+h)-F(x)}{h}=\frac 1h\left(\int_a^{x+h}f(t)dt-\int_a^xf(t)dt\right)=\frac 1h\int_x^{x+h}f(t)dt.\]`

Because `\(f\)` is continuous, the [mean value theorem for Riemann integrals][bookofproofs$1772] tells us that there exists `\(\xi_h\in[x,x+h]\)` (or `\(\xi_h\in[x+h,x]\)` for `\(h < 0\)`) with

`\[\int_x^{x+h}f(t)dt=hf(\xi_h).\]`

Note that `\(\xi_h\)` tends to `\(x\)`, as `\(h\)` tends to `\(0\)`. Because `\(f\)` is continuous, we get the required result:
`\[F'(x)=\lim_{h\to 0}\frac 1h\int_x^{x+h}f(t)dt=\lim_{h\to 0}\frac 1h(hf(\xi_h))=f(x).\]`
