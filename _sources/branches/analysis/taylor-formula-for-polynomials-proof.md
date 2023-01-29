layout: proof
categories: branches,analysis
nodeid: bookofproofs$8443
orderid: 50
parentid: bookofproofs$8442
title: 
description: PROOF OF TAYLOR'S FORMULA FOR POLYNOMIALS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: taylor's formula for polynomials,proof
contributors: bookofproofs

---


---

* By hypothesis, `$I\subset\mathbb R$` is an [interval][bookofproofs$1153], `$f:I\to\mathbb R$` is a [$(n+1)$ times continuously differentiable function][bookofproofs$6205] with `$f^{\{n+1\}}(x)=0$` for all `$x\in I.$` 
* In the [Taylor's formula][bookofproofs$8440], the remainder term vanishes `$$R_{n+1}(x)=\frac 1{n!}\int_a^x (x-t)^nf^{\{n+1\}}(t)dt=0$$` and we have `$$f(x)=f(a)+\sum_{k=1}^n \frac{f^{\{k\}}(a)}{k!}(x-a)^k$$` for all `$a,x\in I.$` 
* This means with the formula of [$n$th power][bookofproofs$6755], that `$f(x)$` is a [real polynomial][bookofproofs$199] of degree `$\le n.$`
