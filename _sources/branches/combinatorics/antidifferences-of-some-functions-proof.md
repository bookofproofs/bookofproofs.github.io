layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8512
orderid: 50
parentid: bookofproofs$8511
title: 
description: PROOF OF ANTIDIFFERENCES OF SOME FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8404
keywords: antidifferences of some functions,proof
contributors: bookofproofs

---


---

### Ad `$(1)$`

* In [difference operators of some functions][bookofproofs$8424], we saw that `$\Delta x^{\underline {n+1}}=(n+1)x^{\underline n}$`.
* For `$n\neq -1$`, we get `$x^{\underline n}=1/(n+1)\cdot \Delta x^{\underline {n+1}}.$`
* Summing both sides yields with [the linearity of indefinite sums][bookofproofs$8509] to the formula `$$\sum x^{\underline{n}}=\frac{x^{\underline{n+1}}}{n+1}.$$`

### Ad `$(2)$`

* Again, [difference operators of some functions][bookofproofs$8424] show that `$\Delta a^x=a^x(a-1).$` 
* For `$a\neq 1$`, we get `$a^x=1/(a-1)\cdot\Delta a^x.$`
* Summing both sides yields with [the linearity of indefinite sums][bookofproofs$8509] to the formula `$$\sum a^x=\frac{a^x}{a-1}.$$`

### Ad `$(3)$`

* Similarly, summing both sides of the result `$\Delta 2^x=2^x$` yields `$$\sum 2^x=2^x.$$`

### Ad `$(4)$`

* We calculate the [difference operator][bookofproofs$8408] `$\Delta\cos(ax+b)=-2\sin(a/2)\sin(ax+b+a/2).$`
* Set `$b=-a/2.$`
* It follows `$\cos(ax-a/2)=-2\sin(a/2)\sin(ax).$`
* Thus, for `$a\neq 2n\pi$`: `$$\sum\sin(ax)=-\frac{\cos(a(x-1/2))}{2\sin(a/2)}.$$`

### Ad `$(5)$`

* Similarly, from `$\Delta\sin(ax+b)=-2\sin(a/2)\cos(ax+b+a/2),$` we deduce for `$a\neq 2n\pi$`: `$$\sum\cos(ax)=\frac{\sin(a(x-1/2))}{2\sin(a/2)}.$$`


### Ad `$(6)$`

* In [difference operators of some functions][bookofproofs$8424], we saw that `$\Delta(a+bx)^{\underline {n+1}}=b(n+1)$`.
* For `$n\neq -1$`, we get `$(a+bx)^\underline{n}=1/(b(n+1))\cdot \Delta(a+bx)^{\underline {n+1}}.$`
* Summing both sides yields with [the linearity of indefinite sums][bookofproofs$8509] to the formula `$$\sum(a+bx)^{\underline{n}}=\frac{(a+bx)^{\underline{n+1}}}{b(n+1)}.$$`
