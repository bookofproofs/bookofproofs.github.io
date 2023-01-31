layout: section
categories: branches,number-theory
nodeid: bookofproofs$8213
orderid: 700
parentid: bookofproofs$8194
title: Generalizations of the Legendre symbol - Jacobi and Kronecker Symbols
description: GENERALIZATIONS OF THE LEGENDRE SYMBOL - JACOBI AND KRONECKER SYMBOLS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: generalizations,jacobi,kronecker,legendre,symbol,symbols
contributors: bookofproofs


---


---

The [Legendre symbol][bookofproofs$8198] `$\left(\frac ap\right)$` is only defined for [odd][bookofproofs$8130] [prime numbers][bookofproofs$473] `$p > 2.$` It allows to master the question, whether, for a given [integer][bookofproofs$844] `$a,$` the [congruence][bookofproofs$8153] `$x^2(p)\equiv a(p)$` is solvable or not.

It turns out that it is possible to generalize the module `$p$` to odd, [positive integers][bookofproofs$1075] `$n > 0$` (_Jacobi symbol_) or even to _all_ integers `$n$` (_Kronecker symbol_), both symbols denoted by `$\left(\frac an\right).$` In this section, we will define both symbols and learn to calculate them, without knowing the [factorization][bookofproofs$803] of `$|n|.$` 

Even though we will be able to calculate the Jacobi or the Kronecker symbols, unfortunately, it will be no more as easy possible to decide, whether the congruence `$x^2(n)\equiv a(n)$` is solvable, as it was the case for the Legendre symbol, if the module `$n$` is a [composite][bookofproofs$8097]. Nevertheless, the Jacobi symbol has still many applications in modern _computational number theory_, especially in primality testing and cryptography (for algorithms, see part [semi-numerical algorithms][bookofproofs$156]). On the other hand, the Kronecker symbol has applications in the classical number-theoretic results of [Dirichlet][di] (1805 - 1859).

[di]:https://mathshistory.st-andrews.ac.uk/Biographies/Dirichlet/