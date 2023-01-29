layout: proof
categories: branches,analysis
nodeid: bookofproofs$1785
orderid: 50
parentid: bookofproofs$1782
title: 
description:  Proof of CONTINUITY OF COSINE AND SINE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: continuity,cosine,sine,proof
contributors: bookofproofs

---


---

Let `\((x_n)_{n\in\mathbb N}\)` be a [convergent real sequence][bookofproofs$141] with `\[\lim_{n\to\infty}x_n=a\]` for some [real number][bookofproofs$1105] `\(a\in\mathbb R\)`. We want to show that [cosine][bookofproofs$1745] `\(\cos:\mathbb R\mapsto \mathbb R\)` and [sine][bookofproofs$1746] `\(\sin:\mathbb R\mapsto \mathbb R\)` are [continuous real functions][bookofproofs$1260], which means by definition that
`\[\begin{array}{rcl}\lim_{n\to\infty}\cos(x_n)&=&\cos(a)\\\lim_{n\to\infty}\sin(x_n)&=&\sin(a).\end{array}\]`

We use the fact that [real numbers are embedded in the complex numbers][bookofproofs$1243]. Therefore, we can consider all real sequence members `\(x_n\)` to be special [complex numbers][bookofproofs$216] with `\(x_n=\Re( x_n)\)`. Then `\((x_n)_{n\in\mathbb N}\)` is a [convergent complex sequence][bookofproofs$1700]. Due to the [rule of multiplying a complex sequence by a complex number][bookofproofs$1719] (here, we multiply all `\(x_n\)`  by the [imaginary unit][bookofproofs$1160] `\(i\)`, we get the result

`\[\lim_{n\to\infty}ix_n=ia.\]`

Because the [complex exponential function is continuous][bookofproofs$1743], we get in particular on the [unit circle][bookofproofs$1749] the next result

`\[\lim_{n\to\infty}\exp(ix_n)=\exp(ia).\]`

We also know that [a complex sequence is convergent if and only if its real and imaginary parts are convergent][bookofproofs$1702]. It follows from the [Euler's formula][bookofproofs$1783] that

`\[\lim_{n\to\infty}\exp(ix_n)=\lim_{n\to\infty}\cos(x_n)+i\lim_{n\to\infty}\sin(x_n)=\cos(a)+i\sin(a).\]`

By comparing the real and imaginary parts of the last equation, we get the desired result:

`\[\begin{array}{rcl}\lim_{n\to\infty}\cos(x_n)&=&\cos(a)\\\lim_{n\to\infty}\sin(x_n)&=&\sin(a).\end{array}\]`
