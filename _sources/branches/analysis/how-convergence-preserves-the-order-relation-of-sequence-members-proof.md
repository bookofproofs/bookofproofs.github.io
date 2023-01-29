layout: proof
categories: branches,analysis
nodeid: bookofproofs$1146
orderid: 50
parentid: bookofproofs$1144
title: 
description:  Proof of HOW CONVERGENCE PRESERVES THE ORDER RELATION OF SEQUENCE MEMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: convergence preserves order relation,convergence preserves order,proof
contributors: bookofproofs

---


---

By assumption, `\((a_n)_{n\in\mathbb N}\)` and `\((b_n)_{n\in\mathbb N}\)` are [convergent real sequences][bookofproofs$141] with the limits `\(\lim_{n\rightarrow\infty} a_n=a\)` and `\(\lim_{n\rightarrow\infty} b_n=b\)`. We have to show the following:

### `\( ( 1 ) \)` If `\(a_n \le b_n\)` for all `\(n\in\mathbb N\)`, then `\(a \le b\)`.

Using the [definition of the order relation for real numbers][bookofproofs$1107], the relations "`\(\le\)`" and "`\( > \)`" are mutually exclusive. Thus, let assume that `\(a_n \le b_n\)` for all `\(n\in\mathbb N\)`, but `\(a > b\)`. Set `\(\epsilon:=(a-b)/2 > 0\)`. Since there are indices `\(N_a(\epsilon),N_b(\epsilon)\in\mathbb N\)` such that 

`\[|a_n-a| < \epsilon~\forall n\ge N_a(\epsilon)\quad\quad\text{and}\quad\quad|b_n-b| < \epsilon~\forall n\ge N_b(\epsilon),\]`

then, for all `\(n\ge\max(N_a(\epsilon),N_b(\epsilon))\)`, it follows 

`\[a_n > a - \epsilon\quad\quad\text{and}\quad\quad b_n  < b + \epsilon .\]`

By construction, we have `\(a - \epsilon=b +\epsilon\)`, so it follows `\(a_n > b_n\)` for all `\(n\ge \max(N_a(\epsilon),N_b(\epsilon))\)`. But `\(a_n \le b_n\)` by assumption, which is a [contradiction][bookofproofs$744].
### `\( ( 2 ) \)` From `\(a_n < b_n\)` for all `\(n\in\mathbb N\)` it does not (!) follow that `\(a < b\)`.

It is sufficient to find only one counterexample, for which `\(a_n < b_n\)` for all `\(n\in\mathbb N\)`, but `\(a \not < b\)`. This counterexample can be given for the sequences `\(a_n = 0\)` and `\(b_n=1/n\)` for all `\(n\in\mathbb N\)`, for which we have

`\[\lim_{n\rightarrow\infty} a_n=\lim_{n\rightarrow\infty} 0= 0 = \lim_{n\rightarrow\infty} \frac 1n=\lim_{n\rightarrow\infty} b_n\]`
