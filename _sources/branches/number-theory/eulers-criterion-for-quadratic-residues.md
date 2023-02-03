layout: proposition
categories: branches,number-theory
nodeid: bookofproofs$8201
orderid: 400
parentid: bookofproofs$8194
title: Euler's Criterion For Quadratic Residues
description: EULER'S CRITERION FOR QUADRATIC RESIDUES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: criterion,eulers,quadratic,residues,euler's criterion,proof of euler's criterion,euler's criterion for quadratic residues,euler’s criterion,euler criterion,euler's criterion proof,eulers criterion
contributors: bookofproofs


---
From a [necessary condition for an integer to be prime][bookofproofs$8191] it follows that `$n^{\frac{p-1}{2}}(p)\equiv\pm 1(p),$` since `$n^{p-1}(p)\equiv 1(p)$` if `$p\not\mid n$` and `$p$` is a [prime number][bookofproofs$473]. This motivates the following criterion, found by [Leonhard Euler](https://mathshistory.st-andrews.ac.uk/Biographies/Euler/).

---

Let `$p > 2$` be a [prime number][bookofproofs$473] and let `$n\in\mathbb Z$` be a given [integer][bookofproofs$844]. The [Legendre symbol modulo][bookofproofs$8198] `$p$` can be calculated using the formula

`$$\left(\frac np\right)(p)\equiv n^{\frac{p-1}{2}}(p).$$`

In particular:
* `$n$` is a [quadratic residue modulo][bookofproofs$8196] `$p$` if and only if `$p\not\mid n$` and `$n^{\frac{p-1}{2}}(p)\equiv 1(p),$`
* `$n$` is a quadratic nonresidue modulo `$p$` if and only if `$p\not\mid n$` and `$n^{\frac{p-1}{2}}(p)\equiv (p-1)(p)\equiv -1(p),$`
* otherwise, we have `$p\mid n$` and `$n^{\frac{p-1}{2}}(p)\equiv 0(p).$`
