layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1438
orderid: 50
parentid: bookofproofs$1435
title: By Induction
description:  Proof of MULTIPLICATION OF NATURAL NUMBERS IS COMMUTATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: commutative,multiplication,natural,numbers,proof
contributors: bookofproofs

---


---

The proof is in two steps:

### Step `\((1)\)` Showing [by induction][bookofproofs$657] of `\(n\)` that `\(n\cdot 0=0\cdot n\)` for all `\(n\in\mathbb N\)`.

It follows from the [definition of multiplication][bookofproofs$876] that
`\[0\cdot 0=0\cdot 0\text{       (Base case)}.\]`
Now, let assume that `\(n_0\cdot 0=0\cdot n_0\)` has been proven for all `\(n_0\le n\)`, where we use "`\(\le\)`" as the [order relation of natural numbers][bookofproofs$697]. Then it follows again from the definition of multiplication that
`\[n^+ \cdot 0=0.\quad\quad ( * )\]`
Here, `\(n^+\)` denotes the unique successor of `\(n\)`.  On the other side, we have by [definition of multiplication][bookofproofs$876] and by assumption 
`\[0\cdot n^+=(0\cdot n)+0=(n\cdot 0)+0=0+0=0.\quad\quad ( * * )\]`
In the last step (`\(0 + 0=0\)`) we have used the [definition of addition of natural numbers][bookofproofs$842]. The comparison of `\(( * )\)` and  `\(( * * )\)` proves the commutativity law `\(n\cdot 0=0\cdot n\)` for all `\(n\in\mathbb N\)`.

### Step `\((2)\)` Showing [by induction][bookofproofs$657] of `\(m\)` that `\(n\cdot m=m\cdot n\)` for all `\(m\in\mathbb N\)`.

It follows from the step `\((1)\)` that 
`\[n\cdot 0=0\cdot n\text{       (Base case)}.\]`
Now, let assume that `\(n\cdot m_0=m_0\cdot n\)` has been proven for all `\(m_0\le m\)`. Then it follows from the [definition of multiplication][bookofproofs$876] and by assumption that
`\[n\cdot m^+=(n\cdot m) + n=(m\cdot n) + n.\quad\quad ( \ast ) \]`
From the [definition of multiplication][bookofproofs$876] and the [definition of addition][bookofproofs$842], we have `\(n\cdot 1=(n\cdot 0)+n=0+n=n\)`. Using that result, applying `\(\ast\)` and also the [right-distributivity law for natural numbers][bookofproofs$1030] we get
`\[(m\cdot n)+n=(m\cdot n)+(n\cdot 1)=(m+1)\cdot n=m^+\cdot n\quad\quad ( \ast \ast ) \]`
The comparison of `\(( \ast )\)` and  `\(( \ast\ast )\)` proves the commutativity law `\(n\cdot m=m\cdot n\)` for all `\(n,m\in\mathbb N\)`.
