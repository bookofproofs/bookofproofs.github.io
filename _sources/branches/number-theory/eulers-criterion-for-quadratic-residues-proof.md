layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3542
orderid: 50
parentid: bookofproofs$8201
title: 
description:  Proof of EULER'S CRITERION FOR QUADRATIC RESIDUES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: criterion,eulers,quadratic,residues,euler's criterion,proof of euler's criterion,euler's criterion for quadratic residues,euler’s criterion,euler criterion,euler's criterion proof,eulers criterion,proof
contributors: bookofproofs

---


---

* By hypothesis, `$p > 2$` is a [prime number][bookofproofs$473] and `$n\in\mathbb Z$` is a given [integer][bookofproofs$844].
* Case 0: Assume `$p\mid n.$` 
   * Then `$n(p)\equiv 0(p).$` 
   * [Multiplying][bookofproofs$8156] the congruences, we have `$n^{\frac{p-1}{2}}(p)\equiv 0(p).$` 
   * Therefore, the postulated formula for the [Legendre symbol modulo][bookofproofs$8198] `$p$` is correct.
* Case 1: Now, assume `$p\not\mid n,$` and `$\left(\frac np\right)=1.$`
   * By definition of the [Legendre symbol modulo][bookofproofs$8198] `$p$`, the [congruence][bookofproofs$8153] `$x^2(p)\equiv n(p)$` has a solution.
   * According to the [necessary condition for an integer to be prime][bookofproofs$8191], we have `$$n^{\frac{p-1}{2}}(p)\equiv (x^2)^{\frac{p-1}{2}}(p)\equiv x^{p-1}(p)\equiv 1(p).$$`
   * Therefore, the postulated formula is again correct.
* Case 2: Now, assume `$p\not\mid n,$` and `$\left(\frac np\right)=-1.$`
   * According to [counting the roots of a diophantine polynomial modulo `$p$`][bookofproofs$8184], the [congruence][bookofproofs$8153] `$\left(x^{\frac{p-1}{2}}-1\right)(p)\equiv 0(p)\label{eq:E18698}\tag{1}$` has _at most_ `$\frac{p-1}{2}$` solutions.
   * By case 1 and according to the [number of quadratic residues in reduced residue systems modulo `$p$`][bookofproofs$8200], the congruence `$(\ref{eq:E18698})$` has _at least_ `$\frac{p-1}{2}$` solutions.
   * Therefore, the congruence `$(\ref{eq:E18698})$` has _exactly_ the `$\frac{p-1}{2}$` [quadratic residues modulo][bookofproofs$8196] `$p$` as solutions in the [reduced residue system modulo][bookofproofs$8174] `$p$`.
   * The number `$n$` as a quadratic nonresidue modulo `$p$` solves therefore the congruence `$\left(x^{\frac{p-1}{2}}+1\right)(p)\equiv 0(p).$`
   * Therefore, the postulated formula is again correct.
