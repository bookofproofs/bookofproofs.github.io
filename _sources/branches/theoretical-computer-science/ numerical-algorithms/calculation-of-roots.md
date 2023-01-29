layout: chapter
categories: branches,theoretical-computer-science, numerical-algorithms
nodeid: bookofproofs$361
orderid: 200
parentid: bookofproofs$177
title: Calculation of Roots
description: CALCULATION OF ROOTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: calculation,roots
contributors: bookofproofs

---


---

The calculation of [roots][bookofproofs$6736] deals with the solution of equations of the type `$f(x)=0$`, where `$f$` is a (real-valued) [function][bookofproofs$592] defined on a [real interval][bookofproofs$1153]. In a few cases, the root of the function can be calculated using an explicit formula, like it is the case e.g. for quadratic polynomials. 

In the majority of cases, however, such an explicit formula does not exist. In these cases, a numerical solution is necessary. It usually makes use of [sequences][bookofproofs$875], whose terms can be calculated separately and which [converge][bookofproofs$141] to the exact solution.

A numerical algorithm is appropriate to solve a root equation if the convergence behavior is fast enough and if there is an approximation of the error made when calculating the successive terms of the convergent sequence. Given an allowed error bound, this approximation is then used to decide, when to abort the calculation.
