layout: solution
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1832
orderid: 50
parentid: bookofproofs$1831
title: Application of the Urn Model Without Replacement
description: Solution of  &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: application,model,replacement,urn,without
contributors: bookofproofs

---


---

We can apply the [urn model without replacement][bookofproofs$1797], in which for the event

`\[A:=\{\text{"If we draw }2\text{ items in total, then we draw exactly }k\text{ broken items."}\}\]`

the probability obeys the equation

`\[p_k=p(A)=\frac{\binom 4k\binom {10-4}{2-k}}{\binom {10}2}=\frac{\binom 4k\binom {6}{2-k}}{45}\quad\quad\text{for }k=0,1,2.\]`

It follows
`\[p_0=\frac{\binom 40\binom {6}{2-0}}{45}=\frac{1\cdot 15}{45}=\frac{5}{15}=\frac{1}{3},\]`
`\[p_1=\frac{\binom 41\binom {6}{2-1}}{45}=\frac{4\cdot 6}{45}=\frac{8}{15},\]`
`\[p_2=\frac{\binom 42\binom {6}{2-2}}{45}=\frac{6\cdot 1}{45}=\frac{2}{15}.\]`
