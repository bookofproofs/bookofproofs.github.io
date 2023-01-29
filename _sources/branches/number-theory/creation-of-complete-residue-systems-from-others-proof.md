layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3524
orderid: 50
parentid: bookofproofs$8175
title: 
description:  Proof of CREATION OF COMPLETE RESIDUE SYSTEMS FROM OTHERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: creation of complete residue systems,proof
contributors: bookofproofs

---


---

* By hypothesis, `$m > 0$` is a [positive integer][bookofproofs$1075], `$n\perp m$` are [co-prime][bookofproofs$8093], and `$C=\{a_1,\ldots,a_m\}$` is a [complete residue system modulo `$m$`][bookofproofs$8173].
* Since `$C$` is complete, `$a_i(m)\not\equiv a_j(m)$` if and only if `$i\neq j.$`
* For any given pair of indices `$i,j$` with `$i\neq j$` and by [contraposition][bookofproofs$1330] to the [cancellation of congruences with factor co-prime to module][bookofproofs$8161], we have that `$a_i(m)\not\equiv a_j(m)\Longrightarrow (a_in)(m)\not \equiv (a_jn)(m)$`, provided `$n\perp m.$`
* Because [any representative of `$a(m)$` is either co-prime or not co-prime to `$m$`][bookofproofs$8176] we have `$(a_in)(m)\not \equiv (a_jn)(m)$` if and only if `$i\neq j.$`
* That means that `$nC:=\{na_1,\ldots,na_m\}$` is a complete residue system modulo `$m.$`
