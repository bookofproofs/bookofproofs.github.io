layout: proof
categories: branches,topology
nodeid: bookofproofs$1130
orderid: 50
parentid: bookofproofs$1129
title: 
description:  Proof of UNIQUENESS OF THE LIMIT OF A SEQUENCE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$582
keywords: uniqueness of the sequence limit,limit of a sequence is unique,proof
contributors: bookofproofs

---


---

Assume, `\(x\neq x'\)`. In the [metric space][bookofproofs$617] `\((X,d)\)`, set `\(\epsilon=d(x,x')/2\)`. From the [definition of convergence][bookofproofs$148],:

1. it follows from `\(\lim_{n\rightarrow\infty} x_n=x\)` that there is an `\(N(\epsilon)\in\mathbb N\)` with `\(d(x_n,x) < \epsilon\)` for all `\(n > N(\epsilon)\)`.
1. it follows from `\(\lim_{n\rightarrow\infty} x_n=x'\)` that there is an `\(M(\epsilon)\in\mathbb N\)` with `\(d(x_n,x') < \epsilon\)` for all `\(n > M(\epsilon)\)`.

Therefore, for all `\(n > \max(N(\epsilon),M(\epsilon))\)` we have 
`\[d(x_n,x) < \epsilon\quad\quad\text{and}\quad\quad d(x_n,x') < \epsilon.\]`

It follows that 

`\[d(x,x')=\le d(x,x_n) + d(x_n,x') < 2\epsilon=d(x , x'),\]`

which would mean that `\(d(x,x') < d(x,x')\)`. This is a [contradiction][bookofproofs$744]. Therefore, the assumption `\(x \neq x'\)` must be wrong and both limits are identical, or `\(x=x'\)`.
