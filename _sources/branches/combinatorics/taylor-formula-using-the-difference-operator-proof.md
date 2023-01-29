layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8488
orderid: 50
parentid: bookofproofs$8487
title: 
description: PROOF OF TAYLOR'S FORMULA USING THE DIFFERENCE OPERATOR &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8404
keywords: taylor's formula with the difference operator,newton's formula,proof
contributors: bookofproofs

---


---

* By hypothesis, `$f:D\to\mathbb C$` is a [factorial polynomial][bookofproofs$8418], i.e. `$f(x)=a_nx^{\underline{n}}+a_{n-1}x^{\underline{n-1}}+\ldots+a_1x^{\underline{1}}+a_0$` for some [complex numbers][bookofproofs$216] `$a_n,\ldots,a_1x^{\underline{1}}a_0\in\mathbb C.$` 
* For `$x=0$`, we have `$f(0)=a_0.$` 
* Taking the [difference operator][bookofproofs$8408] yields with the formula for the [difference operator of falling factorial powers][bookofproofs$8416] `$$\Delta f(x)=na_nx^{\underline{n-1}}+(n-1)a_{n-1}x^{\underline{n-2}}+\ldots+a_1$$` and `$\Delta f(0)=a_1.$` 
* Proceeding in this fashion, we get with the [kth difference operator][bookofproofs$8411] `$\Delta^k f(0)=k! \cdot a_k$` (with `$k!$` being the [factorial][bookofproofs$1005])
* Hence, 
`$$f(x)=\frac{\Delta^n f(0)}{n !} x^{\underline{n}}+\frac{\Delta^n f(0)}{(n-1) !} x^{\underline{n-1}}+ \ldots + \frac{\Delta^2 f(0)}{2 !} x^{\underline{2}} + \Delta f(0) x^{\underline{1}}+ f(0).$$`
