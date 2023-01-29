layout: proof
categories: branches,number-theory
nodeid: bookofproofs$2944
orderid: 50
parentid: bookofproofs$8154
title: 
description:  Proof of CONGRUENCE CLASSES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8152
keywords: congruence class,residue class,congruence classes,residue classes,proof
contributors: bookofproofs

---


---

* Let `$m > 0$` be a [positive integer][bookofproofs$1075] and let `$a\equiv b(m)$` (two [integers][bookofproofs$844] `$a,b$` being [congruent][bookofproofs$8153] modulo `$m$`).
* We show three properties, applying the definitions of [congruence][bookofproofs$8153] and [divisors][bookofproofs$700]:
   * Reflexivity: `$m\mid (a-a)=0$`, therefore `$a\equiv a(m).$`
   * Symmetry: `$m\mid (a-b)\Leftrightarrow m\mid (b-a),$` therefore `$a\equiv b(m)\Leftrightarrow b\equiv a(m).$`
   * Transitivity: 
      * If `$a\equiv b(m)$` and `$b\equiv c(m)$`, then `$m\mid(a-b)$` and `$m\mid(b-c).$`
      * But then `$m\mid (a-b)+(b-c)=(a-c)$`
      * It follows `$a\equiv c(m).$`  
* Altogether, it follows that that the [relation][bookofproofs$571] `$[\equiv(m)"\subset \mathbb Z\times\mathbb Z$` is an "equivalence relation][bookofproofs$574].