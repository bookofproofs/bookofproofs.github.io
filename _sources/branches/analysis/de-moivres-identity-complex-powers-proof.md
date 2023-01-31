layout: proof
categories: branches,analysis
nodeid: bookofproofs$8606
orderid: 50
parentid: bookofproofs$8605
title: By Induction
description: PROOF OF DE MOIVRE'S IDENTITY, COMPLEX POWERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: de moivre's identity,de moivre's formula,complex powers,proof
contributors: bookofproofs

---


---

* By hypothesis, `$\phi$` is a [real number][bookofproofs$1105].
* We prove the formula [by induction][bookofproofs$657].
* Base case `$n=1$` 
   * By the [multiplication of complex numbers using polar coordinates][bookofproofs$6751] (with `$r=1$`) `$$1=[\cos(\phi)+i\sin(\phi)].$$`
* Induction step
   * Assume, the formula `$[\cos(\phi)+i\sin(\phi)]^n=\cos(n\phi)+i\sin(n\phi)$` holds for all [natural numbers][bookofproofs$718] `$n\in\mathbb N$` not exceeding some number `$N.$`
   * Then, by [additivity theorems for cosine and sine][bookofproofs$6730]: `$$\begin{array}{rcl}[\cos(\phi)+i\sin(\phi)]^{n+1}&=&[\cos(\phi)+i\sin(\phi)]^n\cdot [\cos(\phi)+i\sin(\phi)]\\
&=&[\cos(n\phi)+i\sin(n\phi)]\cdot  [\cos(\phi)+i\sin(\phi)]\\
&=&\cos(n\phi)\cos(\phi)+i\sin(\phi)\cos(n\phi)-i\sin(n\phi)\cos(\phi)-\sin(n\phi)\sin(\phi)\\
&=&\cos((n+1)\phi)+i\sin((n+1)\phi)
\end{array}$$`
* In particular, if `$z=r\exp(i\phi)$` is a [complex number][bookofproofs$216] written in its [polar coordinates][bookofproofs$6750], then `$z^n=r^n\exp(in\phi),$` by [Euler's formula][bookofproofs$1783].