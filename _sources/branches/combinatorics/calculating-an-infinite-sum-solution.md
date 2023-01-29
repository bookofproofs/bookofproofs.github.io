layout: solution
categories: branches,combinatorics
nodeid: bookofproofs$8521
orderid: 50
parentid: bookofproofs$8520
title: 
description: SOLUTION OF CALCULATING AN INFINITE SUM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8404
keywords: calculating an infinite sum,solution
contributors: bookofproofs

---


---

* Changing the indices in the infinite sum, and using the definition of the [falling factorial powers][bookofproofs$1399] yields `$$\sum_{x=1}^\infty\frac{1}{x(x+1)}=\sum_{x=0}^\infty\frac{1}{(x+1)(x+2)}=\sum_{x=0}^\infty x^{\underline{-2}}.$$`
* We have to evaluate the [limit][bookofproofs$141] of the [partial sums][bookofproofs$1109] `$$S_n:=\sum_{x=0}^n x^{\underline{-2}}$$` for `$n\to\infty.$`
* Applying the [fundamental theorem of the difference calculus][bookofproofs$8513] we get `$$S_n=\frac{x^{\underline {-1}}}{-1}\;\Rule{1px}{4ex}{2ex}^{n+1}_{0}=-\frac{1}{x+1}\;\Rule{1px}{4ex}{2ex}^{n+1}_{0}=1-\frac{1}{n+2}.$$`
* And `$$\lim_{n\to\infty} S_n=1.$$`
