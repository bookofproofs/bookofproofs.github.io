layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3545
orderid: 50
parentid: bookofproofs$8206
title: 
description: PROOF OF FIRST SUPPLEMENTARY LAW TO THE QUADRATIC RECIPROCITY LAW &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: first,law,quadratic,reciprocity,supplementary,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` is an [odd][bookofproofs$8130] [prime number][bookofproofs$473].
* By the [Euler's criterion for quadratic residues][bookofproofs$8201] we have the [congruence][bookofproofs$8153]  `$\left(\frac {-1}p\right)(p)\equiv (-1)^{\frac{p-1}{2}}(p).$`
* Now, the difference `$\left(\frac {-1}p\right)-(-1)^{\frac{p-1}{2}}$` equals one of the integers `$0$`, `$-2$` or `$2.$`
* Because `$p$` is odd, only `$0$` is possible.
* It remains to be shown that the identity `$\left(\frac {-1}p\right)=(-1)^{\frac{p-1}{2}}$` is equivalent to 
`$$\left(\frac {-1}p\right)=\begin{cases}1&\text{if }p\equiv 1\mod 4,\\-1&\text{if }p\equiv -1\mod 4.\end{cases}$$`
   * If `$p(4)\equiv 1(4)$` then `$p=4k+1$` for some `$k\in\mathbb Z.$` 
      * Then `$\frac{p-1}2=2k$` is [even][bookofproofs$8130] and `$(-1)^{2k}=1.$`
      * Thus, in this case `$\left(\frac {-1}p\right)=1,$` as required.
   * If `$p(4)\equiv -1(4)$` then `$p=4k-1$` for some `$k\in\mathbb Z.$`
      * Then `$\frac{p-1}2=2k-1$` is [odd][bookofproofs$8130] and `$(-1)^{2k-1}=-1.$`
      * Thus, in this case `$\left(\frac {-1}p\right)=-1,$` as required.
   * Since `$p$` is odd, no other congruence classes modulo `$4$` except `$\pm 1$` exist.
