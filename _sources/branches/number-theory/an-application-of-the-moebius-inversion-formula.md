layout: section
categories: branches,number-theory
nodeid: bookofproofs$3244
orderid: 700
parentid: bookofproofs$232
title: An Application of the Möbius Inversion Formula
description: AN APPLICATION OF THE MöBIUS INVERSION FORMULA &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: application,formula,inversion,moebius
contributors: bookofproofs

---


---

As a first application of the [Möbius inversion][bookofproofs$8149], we want to calculate an explicit formula for the [Euler function][bookofproofs$8117] `$\phi.$` 

As a first step, we have to find a function `$f(n)$` with `$$f(n)=\sum_{d\mid n}\phi(d).$$`

Then, we will be able to apply the Möbius inversion formula, and get the sum `$$\phi(n)=\sum_{d\mid n}\mu(n)f\left(\frac{n}{d}\right).$$`

The last step will be to find an explicit formula for this sum.
