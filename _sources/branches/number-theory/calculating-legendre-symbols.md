layout: section
categories: branches,number-theory
nodeid: bookofproofs$8204
orderid: 600
parentid: bookofproofs$8194
title: Calculating Legendre Symbols
description: CALCULATING LEGENDRE SYMBOLS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: calculating,legendre,symbols,legendre symbol calculator,compute legendre symbol,calculate legendre symbol
contributors: bookofproofs

---


---

By definition, the [Legendre symbol][bookofproofs$8198] indicates, if the congruence `$x^2(p)\equiv a(p)$` is solvable for a given [odd][bookofproofs$8130] [prime number][bookofproofs$473] `$p$` and a given [integer][bookofproofs$844] `$a.$` It would be, therefore, very useful to have a universal way to calculate Legendre symbols.

We start the section with an observation. We have seen that the [Legendre symbol is multiplicative][bookofproofs$8202]. This means that if `$p$` is an [odd][bookofproofs$8130] [prime number][bookofproofs$473], then the [Legendre symbol][bookofproofs$8198] `$\left(\frac np\right)$` can be written as a product of Legendre symbols of the form `$$\left(\frac {-1}p\right),\label{eq:E18679a}\tag{1}$$`
`$$\left(\frac {2}p\right),\text{or}\label{eq:E18679b}\tag{2}$$`
`$$\left(\frac {q}p\right),\label{eq:E18679c}\tag{3}$$`
where in `$(\ref{eq:E18679c}),$` `$q$` denotes a prime number distinct from `$p.$` Therefore, knowing the [factorization][bookofproofs$803] of `$n$`, we can calculate the [Legendre symbol][bookofproofs$8198] `$\left(\frac np\right),$` using the fact that `$\left(\frac np\right)$` is multiplicative, if we know the values of `$(\ref{eq:E18679a})$` to `$(\ref{eq:E18679c}).$`  In this section, we will, therefore, deal with these three kinds of Legendre symbols and provide explicit formulae for them. The most famous formula is for the case `$(\ref{eq:E18679c}),$` and it is known as the _quadratic reciprocity law_. The other two cases are known `$(\ref{eq:E18679a}),$` and `$(\ref{eq:E18679b})$` as _supplementary laws to the quadratic reciprocity law_.
