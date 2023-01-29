layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3543
orderid: 50
parentid: bookofproofs$8202
title: 
description:  Proof of MULTIPLICATIVITY OF THE LEGENDRE SYMBOL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: legendre,multiplicativity,symbol,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` is a [prime number][bookofproofs$473] and `$r\ge 2$`, `$m,n_1,\ldots,n_r$` are [integers][bookofproofs$844].
* Obviously, if `$p$` is a [divisor][bookofproofs$700] of any of the integers, then, by definition, the corresponding [Legendre symbol modulo][bookofproofs$8198] `$p$` equals `$0.$` 
* Therefore, any product of Legendre symbols involving such an integers also trivially equals `$0.$` 
* We shall therefore assume that `$p$` does not divide any of the integers and look at the non-trivial cases:
* Case `$r=2.$`
   * According to the [Euler's criterion for quadratic residues][bookofproofs$8201], the [Legendre symbol modulo][bookofproofs$8198] `$p$` of the [product][bookofproofs$8157] `$nm$` fulfils the following [congruence][bookofproofs$8153] modulo `$p$`:
`$$\left(\frac{nm}{p}\right)\equiv (nm)^{\frac {p-1}2}\equiv (n)^{\frac {p-1}2}\cdot  (m)^{\frac {p-1}2}\equiv \left(\frac{n}{p}\right)\cdot\left(\frac{m}{p}\right)\mod p.$$`
   * Now, observe that the [difference][bookofproofs$1585] `$\left(\frac{nm}{p}\right)-\left(\frac{n}{p}\right)\left(\frac{m}{p}\right)$` can only take one of the values `$0,$` `$-2,$` or `$2.$`
   * But since `$p$` is [odd][bookofproofs$8130], the above congruence holds if and only if `$$\left(\frac{nm}{p}\right)-\left(\frac{n}{p}\right)\left(\frac{m}{p}\right)=0.$$`
* Case `$r > 2.$`
   * This case follows by [induction][bookofproofs$657] from the case `$r=2.$`
* Altogether, we have shown that the [Legendre symbol modulo][bookofproofs$8198] `$p$` is a [completely multiplicative][bookofproofs$505] [arithmetic function][bookofproofs$8112].