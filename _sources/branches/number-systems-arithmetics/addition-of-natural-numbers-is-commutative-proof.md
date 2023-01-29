layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1431
orderid: 50
parentid: bookofproofs$1430
title: By Induction
description:  Proof of ADDITION OF NATURAL NUMBERS IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,commutative,natural,numbers,proof
contributors: bookofproofs

---


---

The proof is in two steps:

### Step `\((1)\)` Showing [by induction][bookofproofs$657] of `\(n\)` that `\(n+0=0+n\)` for all `\(n\in\mathbb N\)`.

It follows from the [definition of addition][bookofproofs$842] that
`\[0+0=0+0\text{       (Base case)}.\]`
Now, let assume that `\(n_0+0=0+n_0\)` has been proven for all `\(n_0\le n\)`, where we use "`\(\le\)`" as the [order relation of natural numbers][bookofproofs$697]. Then it follows again from the definition of addition that
`\[n^+ + 0=n^+\]`
Here, `\(n^+\)` denotes the unique successor of `\(n\)`. Because by assumption `\(n=0+n\)`, we have that `\[n^+=(0+n)^+=0+n^+.\]`
This proves the commutativity law `\(n+0=0+n\)` for all `\(n\in\mathbb N\)`.

### Step `\((2)\)` Showing [by induction][bookofproofs$657] of `\(m\)` that `\(n+m=m+n\)` for all `\(m\in\mathbb N\)`.

It follows from the step `\((1)\)` that 
`\[n+0=0+n\text{       (Base case)}.\]`
Now, let assume that `\(n+m_0=m_0+n\)` has been proven for all `\(m_0\le m\)`. Then it follows from the definition of addition that
`\[n+m^+=(n+m)^+\]`
Because by assumption `\(n+m=m+n\)`, we have that `\[(n+m)^+=(m+n)^+=m+n^+.\]`
These two steps prove the commutativity law `\(n+m=m+n\)` for all `\(n,m\in\mathbb N\)`.
