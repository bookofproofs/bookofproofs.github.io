layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3540
orderid: 50
parentid: bookofproofs$8199
title: 
description:  Proof of LEGENDRE SYMBOLS OF EQUAL RESIDUES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: equal,legendre,residues,symbols,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* By hypothesis, `$p > 2$` is a [prime number][bookofproofs$473], and `$n,m\in\mathbb Z$` belong to the same [congruence classes][bookofproofs$8154] modulo `$p.$`
* Obviously, `$p\mid n$` if and only if `$p\mid m,$` ($p$ is a [divisor][bookofproofs$700] of `$n$` if and only if `$p$` is a divisor of `$m$`).
* Therefore, if `$p\mid n$` then `$n(p)\equiv 0(p)\equiv m(p)$` and the [Legendre symbols][bookofproofs$8198] modulo `$p$` are equal: `$\left(\frac {n}p\right)=\left(\frac {m}p\right)=0.$`
* Similarly, if `$p\not\mid n$` then if `$x^2(p)\equiv n(p)$` is solvable, then `$x^2(p)\equiv m(p)$` is solvable, and vice versa.
* Therefore, if `$n$` is a [quadratic residue][bookofproofs$8196] (nonresidue) modulo `$p,$` so is `$m$`, and vice versa.
* It follows again `$\left(\frac {n}p\right)=\left(\frac {m}p\right).$`
