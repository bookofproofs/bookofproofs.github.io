layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1344
orderid: 100
parentid: bookofproofs$373
title: Euler's Constant
description: EULER'S CONSTANT &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: constant,euler's constant,eulers
contributors: bookofproofs

---


---

The *Euler's constant* `\(e\)` is the value of the [exponential function][bookofproofs$281] at the argument `\(1\)`:

`\[e:=\exp(1)=\sum_{n=0}^\infty \frac{1}{n!}=2.718~281~828~459...\]`

Practically, it can be calculated using the first `\(N\)` terms of the exponential series
`\[\sum_{n=0}^N \frac{x}{n&#33;}=\frac{x^N}{N&#33;}+\frac{x^{N-1}}{(N-1)&#33;}+\ldots+ x + 1\]`
and considering them as a [real polynomial][bookofproofs$199] of degree `\(N\)`. We can then significantly reduce the number of multiplications required to calculate it by regrouping this polynomial using the [Horner scheme][bookofproofs$1358] and getting

`\[\sum_{n=0}^N \frac{x}{n!}=\left(\left(\ldots\left(\left(\frac xN + 1\right)\frac{x}{N-1}+1\right)\frac{x}{N-2}+\ldots\right)\frac x2 + 1 \right)+ x + 1.\]`

For `\(x=1\)` we get the expression

`\[e=\sum_{n=0}^\infty \frac{1}{n!}=\left(\left(\ldots\left(\left(\frac 1N + 1\right)\frac{1}{N-1}+1\right)\frac{1}{N-2}+\ldots\right)\frac 12 + 1 \right)+ 1 + 1 + r_{N+1}\]`

with some remainder term `\( r_{N+1}\)`, which [can be estimated][bookofproofs$1361]  by
`\[r_{N+1}\le \frac 2{(N+1)!}.\]`

For `\(N=15\)` we have `\(r_{16}\le \frac 2{16!} < 10^{-13}\)` the estimation 

`\[e=2.718~281~828~459\pm 2\cdot 10^{-13}.\]`
