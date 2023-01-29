layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3526
orderid: 50
parentid: bookofproofs$8177
title: 
description: PROOF OF CREATION OF REDUCED RESIDUE SYSTEMS FROM OTHERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: reduced residue systems,create,proof
contributors: bookofproofs

---


---

* By hypothesis, `$m > 0$` is a [positive integer][bookofproofs$1075], `$n\perp m$` are [co-prime][bookofproofs$8093], and `$R=\{a_1,\ldots,a_{\phi(m)}\}$` is a [reduced residue system modulo `$m$`][bookofproofs$8174].
* Each of the `$a_i$`, `$i=1,\ldots,\phi(m)$` are co-prime to `$m$`, by definition of [reduced residue systems][bookofproofs$8174], ($\phi(m)$ being the [Euler function][bookofproofs$8117]).
* Therefore, also `$na_i$`, `$i=1,\ldots,\phi(m)$` are co-prime to `$m$`, for `$i=1,\ldots,\phi(m)$`, by definition of [coprimality][bookofproofs$8093].
* By the [creation of complete residue systems from others][bookofproofs$8175], all are pairwise not congruent, i.e. `$a_i(m)\not\equiv a_j(m)$`, if and only if `$i\neq j.$`
* That means that `$nR:=\{na_1,\ldots,na_{\phi(m)}\}$` is a reduced residue system modulo `$m.$`
