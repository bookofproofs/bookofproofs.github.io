layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8202
orderid: 500
parentid: bookofproofs$8194
title: Multiplicativity of the Legendre Symbol
description: MULTIPLICATIVITY OF THE LEGENDRE SYMBOL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: legendre,multiplicativity,symbol
contributors: bookofproofs

---


---

Let `$p > 2$` be a [prime number][bookofproofs$473].
The [Legendre symbols][bookofproofs$8198] are [completely multiplicative][bookofproofs$505], i.e. for any two [integers][bookofproofs$844] `$n,m\in\mathbb Z$` we have `$$\left(\frac{nm}{p}\right)=\left(\frac{n}{p}\right)\cdot\left(\frac{m}{p}\right).$$`

In other words:
* The [congruence][bookofproofs$8153] `$x^2(p)\equiv nm(p)$` is solvable if and only if the congruences `$x^2(p)\equiv n(p)$` and `$x^2(p)\equiv m(p)$` are solvable.

Yet in other words:
* If `$n$` and `$m$` are both [quadratic residues][bookofproofs$8196] (respectively both quadratic nonresidues) modulo `$p$`, then their product `$nm$` is a quadratic residue modulo `$p.$`
* If one of the numbers `$n$` and `$m$` is a quadratic residue modulo `$p$` and the other a quadratic nonresidue modulo `$p$`, then their product `$nm$` is a quadratic nonresidue modulo `$p.$`

In general, if `$p > 2$`, `$r\ge 2,$` and `$n_1,\ldots,n_r$` are integers, then 
`$$\left(\frac{n_1\cdots n_r}{p}\right)=\left(\frac{n_1}{p}\right)\cdots\left(\frac{n_r}{p}\right).$$`
