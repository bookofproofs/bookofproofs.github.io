layout: proof
categories: branches,analysis
nodeid: bookofproofs$2932
orderid: 50
parentid: bookofproofs$6805
title: By Induction
description: PROOF OF INTEGRALS ON ADJACENT INTERVALS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: riemann integral on adjacent intervals,adjacent intervals,proof
contributors: bookofproofs

---


---

In the following, `$[a,c]$` is a [closed real interval][bookofproofs$1153] with a real value `$b$` inbetween `$a < b < c.$` 

### "`$\Rightarrow$`"

* By hypothesis, the [function][bookofproofs$592] `$f:[a,b]\cup[b,c]\to\mathbb R$` is [Riemann-integrable][bookofproofs$1763] on the adjacent intervals `$[a,b]$` and `$[b,c].$` 
* By the [necessary and sufficient condition for integrable functions][bookofproofs$1764] this means that for every `$\epsilon > 0$` there are [step functions][bookofproofs$1751] `$\phi:[a,b]\cup[b,c]\to\mathbb R$` and `$\psi:[a,b]\cup[b,c]\to\mathbb R$` such that 
`$$\phi \le f \le \psi\quad\wedge\quad\int_a^b\psi(x)dx-\int_a^b\phi(x)dx\le\frac{\epsilon}{2}\quad\wedge\quad\int_b^c\psi(x)dx-\int_b^c\phi(x)dx\le\frac{\epsilon}{2}$$`
* But the [union][bookofproofs$6827] of the intervals is `$[a,b]\cup[b,c]$`=$[a,c].$
* Therefore, for the given `$\epsilon > 0$` there are step functions `$\phi:[a,c]\to\mathbb R$` and `$\psi:[a,c]\to\mathbb R$` such that 
`$$\int_a^c\psi(x)dx-\int_a^c\phi(x)dx=\int_a^b\psi(x)dx-\int_a^b\phi(x)dx+\int_b^c\psi(x)dx-\int_b^c\phi(x)dx=\le\epsilon.$$`
* By the same [necessary and sufficient condition for integrable functions][bookofproofs$1764] this means that `$f:[a,c]\to\mathbb R$` is Riemann-integrable with 
`$$\int_a^c f(x)dx=\int_a^b f(x)dx+\int_b^c f(x)dx.$$`

### "`$\Leftarrow$`"

The converse of the statement can be proven analogously.
