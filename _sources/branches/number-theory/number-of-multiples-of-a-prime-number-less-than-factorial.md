layout: theorem
categories: branches,number-theory
nodeid: bookofproofs$8111
orderid: 300
parentid: bookofproofs$232
title: Number of Multiples of a Prime Number Less Than Factorial
description: NUMBER OF MULTIPLES OF A PRIME NUMBER LESS THAN FACTORIAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: factorial,less,multiples,number,prime,than
contributors: bookofproofs

---
The following theorem reveals a remarkable formula for the [factorial][bookofproofs$1005] using [prime numbers][bookofproofs$473] and the [floor function][bookofproofs$280].
---

Let `$p\in\mathbb P$` be a [prime number][bookofproofs$473], `$n > 0$` be a [natural number][bookofproofs$718] and `$n!=n\cdot (n-1)\cdot (n-2)\cdot\ldots\cdot 2\cdot 1$` its [factorial][bookofproofs$1005]. The number `$k$` of [multiples][bookofproofs$700] of `$p$`, i.e. the numbers `$p,2p,3p,\ldots,kp$` with `$kp\le n!$` is given by the [sum][bookofproofs$261] using the [floor function][bookofproofs$280]:

`$$k=\sum_{m=1}^\infty\left\lfloor\frac n{p^m}\right\rfloor.\quad \quad ( * )$$`

In particular, the factorial `$n!$` can be written as a product of powers of all primes:

`$$n!=\prod_{p\in\mathbb P}p^{\sum_{m=1}^\infty\left\lfloor\frac n{p^m}\right\rfloor}.\quad \quad ( * * )$$`


### Example

For `$n=1000$`, and `$p=3$` we have 

`$$\begin{array}{c}\left\lfloor\frac {1000}{3}\right\rfloor=333,\quad\left\lfloor\frac {1000}{3^2}\right\rfloor=111,\quad \left\lfloor\frac {1000}{3^3}\right\rfloor=37,\\
\left\lfloor\frac {1000}{3^4}\right\rfloor=12,\quad\left\lfloor\frac {1000}{3^5}\right\rfloor=4,\quad\left\lfloor\frac {1000}{3^6}\right\rfloor=1\end{array}$$`
and the sum is `$333+111+37+12+4+1=498.$` Thus, in the [factorization][bookofproofs$803] of huge factorial number `$1000!$` the power `$3^{498}$` occurs. We would have got the same result at a significantly lower cost if we had applied a [property of floors][bookofproofs$8109] (the 7th there) that `$\left\lfloor\frac {x}{n}\right\rfloor=\left\lfloor\frac {\lfloor x\rfloor}{n}\right\rfloor.$` Because `$$\left\lfloor\frac {n}{p^{m+1}}\right\rfloor=\left\lfloor\frac {\left\lfloor \frac{n}{p^m}\right\rfloor}{p}\right\rfloor,$$`

we can calculate much simpler like this:

`$$\begin{array}{c}\left\lfloor\frac {1000}{3}\right\rfloor=333,\quad\left\lfloor\frac {333}{3}\right\rfloor=111,\quad \left\lfloor\frac {111}{3}\right\rfloor=37,\\
\left\lfloor\frac {37}{3}\right\rfloor=12,\quad\left\lfloor\frac {1000}{3}\right\rfloor=4,\quad\left\lfloor\frac {1000}{3}\right\rfloor=1.\end{array}$$`
