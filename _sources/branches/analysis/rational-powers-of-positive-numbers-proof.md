layout: proof
categories: branches,analysis
nodeid: bookofproofs$1623
orderid: 50
parentid: bookofproofs$1622
title: 
description:  Proof of RATIONAL POWERS OF POSITIVE NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: numbers,positive,powers,rational,proof
contributors: bookofproofs

---


---

Let `\(a > 0\)` be a [positive real number][bookofproofs$1107]. The [exponential function of general base][bookofproofs$1603] `\(a\)` with the [rational][bookofproofs$1033] exponent `\(\frac pq\in\mathbb Q\)`, (`\(q\neq 0\)`), is well-defined, since it is defined for all real numbers `\(x\in\mathbb R\)`, and every rational number `\(\frac pq\)` is also a real number. 

It remains to be shown that indeed
`\[a^{\frac pq}=\sqrt[q]{a^p}=\exp_a\left(\frac pq\right).\quad\quad( * )\]`
For an integer `\(p\in\mathbb Z\)`, the `\(p\)`-th power function [has been identified with the exponential function of general base to the exponent][bookofproofs$1620] `\(p\)`:
`\[a^p=\exp_a(p).\quad\quad( * * )\]`
Note that for `\(q\in\{-1,1\}\)`, `\( ( * ) \)`  and `\( ( * * ) \)` are identical. For all integers `\(q\)`, with `\(|q|\ge 2\)`, the `\(q\)`-th root of the positive base `\(b\)` is [defined as an inverse function][bookofproofs$46] to the `\(q\)`-th power function:
`\[\sqrt[q] b\quad \text{is inverse to}\quad b^q\quad\text{for all integers }q\text{ with }|q|\ge 2.\]`
It follows from `\( ( * * ) \)` and for `\(b=a^p\)` that
`\[a^p=\exp_a(p)=\exp_a\left(q\cdot \frac pq\right)=\left(\exp_a\left(\frac pq\right)\right)^q,\]` which is equivalent to `\( ( * ) \)`.
