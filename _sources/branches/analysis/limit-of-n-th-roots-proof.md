layout: proof
categories: branches,analysis
nodeid: bookofproofs$1625
orderid: 50
parentid: bookofproofs$1624
title: 
description:  Proof of LIMIT OF N-TH ROOTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: limit,roots,proof
contributors: bookofproofs

---


---

Note that the `\(n\)`-th roots can be [identified with the exponential function of some positive real base][bookofproofs$1622] `\(a > 0\)`:
`\[\sqrt[n]a=\exp_a\left(\frac 1n\right).\]`

Also note that the sequence `\(\left(\frac 1n\right)_{n\in\mathbb N}\)` is a [convergent real sequence][bookofproofs$141] with `\(\lim_{n\to\infty}\frac 1n=0\)`. Because the [exponential function of general base is continuous][bookofproofs$1610], it follows from the [definition of continuity][bookofproofs$219], the [definition of the exponential function of general base][bookofproofs$1603] and the [corresponding proposition][bookofproofs$1423] that 

`\[\lim_{n\to\infty} \sqrt[n]a=\lim_{n\to\infty} \exp_a\left(\frac 1n\right)=\exp_a(0)=\exp(0\cdot \ln(a))=\exp(0)=1.\]`
