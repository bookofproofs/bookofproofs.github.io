layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8510
orderid: 50
parentid: bookofproofs$8509
title: 
description: PROOF OF BASIC CALCULATIONS INVOLVING INDEFINITE SUMS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: calculations involving indefinite sums,proof
contributors: bookofproofs

---


---

### Ad `$(1)$`

* Let `$f$` be a [complex-valued][bookofproofs$216] [function][bookofproofs$592] `$f:\mathbb C\to C$` and let `$\lambda\in\mathbb C$` be a constant. 
* Choose an [antidifference][bookofproofs$8506] `$F:\mathbb C\to\mathbb C$`, that is `$\Delta F(x)=f(x)$`.
* It follows `$\lambda\cdot \Delta F(x)=c\cdot f(x)=\Delta (cF)(x),$` applying basic [calculations involving the difference operator][bookofproofs$8409] (no. 1). 
* Summing on both sides  yields `$\sum cf(x)=cF(x)=c\sum f(x).$`

### Ad `$(2)$`

* Chose the antiderivatives `$F,G:\mathbb C\to\mathbb C$` of `$f,g$`, i.e. `$\Delta F(x)=f(x)$` and `$\Delta G(x)=g(x)$`.
* Applying basic [calculations involving the difference operator][bookofproofs$8409] (no. 2), we get `$\Delta (F(x)\pm G(x))=\Delta F(x)\pm \Delta G(x).$` 
* Summing on both sides yields `$(F(x)\pm G(x))=F(x)\pm G(x).$`
* This means `$\sum (f(x)\pm g(x))=\sum f(x)\pm \sum g(x).$` 

### Ad `$(3)$`

* The [product rule][bookofproofs$8409] of the difference operator, can be re-written for suitable complex-valued functions `$f,g$` as follows: `$g(x)\Delta f(x)=\Delta (fg)(x)-f(x+1)\Delta g(x).$`
* Summing on both sides yields `$\sum g(x)\Delta f(x)=f(x)g(x)-\sum f(x+1)\Delta g(x).$`
