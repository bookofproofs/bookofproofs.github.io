layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3541
orderid: 50
parentid: bookofproofs$8200
title: 
description:  Proof of NUMBER OF QUADRATIC RESIDUES IN REDUCED RESIDUE SYSTEMS MODULO A PRIME &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1272
keywords: modulo,number,prime,quadratic,reduced,residue,residues,systems,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` is a [prime number][bookofproofs$473] and we consider a [reduced residue system modulo][bookofproofs$8174] `$p$`. Let's call it `$R.$` 
* `$R$` can be respresented by the `$p-1$` numbers `$n=1,\ldots,p-1.$`
* Let `$n\in R,$` and assume that `$n$` is a [quadratic residue modulo][bookofproofs$8196] `$p.$` 
* Since `$p\not\mid n,$` there is _at least one_ solution of the congruence `$x^2(p)=n(p)$` in `$R,$` and, by [counting the roots of a diophantine polynomial modulo `$p$`][bookofproofs$8184], there are _at most two_ solutions in `$R.$`
* Because `$(p-x)^2(p)\equiv (-x)^2(p)\equiv x^2(p)$`, if `$x$` solves the polynomial, so does `$p-x.$`
* Therefore, `$n$` must be congruent to _exactly one_ of the `$\frac{p-1}{2}$` numbers in `$R$` from the interval `$1\le x \le \frac{p-1}{2}.$`
* Hence, there are _exactly_ `$\frac{p-1}{2}$` [quadratic residues modulo][bookofproofs$8196] `$p,$` since the `$\frac{p-1}{2}$` numbers `$1^2,2^2,\ldots,\left(\frac{p-1}{2}\right)^2$` are all [incongruent][bookofproofs$8153].
* Since `$R$` has `$p-1$` elements, `$R$` contains `$p-1-\frac{p-1}{2}=\frac{p-1}{2}$` quadratic nonresidues modulo `$p.$`
