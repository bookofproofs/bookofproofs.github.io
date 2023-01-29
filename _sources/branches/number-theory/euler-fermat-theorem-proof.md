layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3535
orderid: 50
parentid: bookofproofs$8190
title: 
description:  Proof of EULER-FERMAT THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: euler,fermat,fermat's little theorem,theorem,proof
contributors: bookofproofs

---


---

* By hypothesis, `$m > 1$` is a [positive integer][bookofproofs$1075], `$a\perp m$` are [co-prime][bookofproofs$8093], and `$\phi(m)$` is the [Euler function][bookofproofs$8117] of `$m.$`  
* Let `$a_1,\ldots,a_{\phi(m)}$` be a [reduced residue system][bookofproofs$8174] modulo `$m.$`
* Since `$a\perp m$`, according to the [creation of reduced residue systems from others][bookofproofs$8177], the numbers `$aa_1,\ldots,aa_{\phi(m)}$` also build a reduced residue system.
* Therefore, the [product][bookofproofs$891] of the integers `$a_1,\ldots,a_{\phi(m)}$` and the product of the integers `$aa_1,\ldots,aa_{\phi(m)}$` are [congruent][bookofproofs$8154] modulo `$m.$`
* Therefore, the following equation holds `$$\left(1\cdot\prod_{n=1}^{\phi(m)}a_n\right)(m)\equiv\left(\prod_{n=1}^{\phi(m)}a a_n\right)(m)\equiv \left(a^{\phi(m)}\cdot \prod_{n=1}^{\phi(m)}a_n\right)(m).$$`
* By definition of a [reduced residue system][bookofproofs$8174] modulo `$m,$` the numbers `$a_1,\ldots,a_{\phi(m)}$` are all co-prime to `$m,$` and thus, the product `$\prod_{n=1}^{\phi(m)}a_n$` is also co-prime to `$m.$`
* Therefore, according to [cancellation of congruences eith factor co-prime to module][bookofproofs$8161], it follows `$$1(m)\equiv a^{\phi(m)}(m).$$`
