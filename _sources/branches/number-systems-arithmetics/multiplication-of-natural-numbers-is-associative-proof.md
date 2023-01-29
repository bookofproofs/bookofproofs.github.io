layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1439
orderid: 50
parentid: bookofproofs$1434
title: By Induction
description:  Proof of MULTIPLICATION OF NATURAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: associative,multiplication,natural,numbers,proof
contributors: bookofproofs

---


---

We shall show the associativity of "`\( \cdot \)`" [by induction][bookofproofs$657]. For arbitrary `\(n,m\in\mathbb N\)`, it follows from the [definition of multiplication][bookofproofs$876] that

### Base case

`\[n\cdot (m\cdot 0)=n\cdot 0=0=(n\cdot m)\cdot 0.\]`

### Induction step

Now, let assume that `\(n\cdot (m\cdot p_0)=(n\cdot m)\cdot p_0\)` has been proven for all `\(p_0\le p\)`. Then it follows 
`\[\begin{array}{rcl}
n\cdot (m\cdot p^+)&=&n((m\cdot p)+m)\quad\quad(i)\\
&=&n\cdot (m\cdot p)+ n\cdot m\quad\quad(ii)\\
&=&(n\cdot m)\cdot p + n\cdot m\quad\quad(iii)\\
&=&(n\cdot m)\cdot (p + 1)\quad\quad(iv)\\
&=&(n\cdot m)\cdot p^+.
\end{array}\]`
Here, we have used in step `\((i)\)` the [definition of multiplication][bookofproofs$876], in steps `\((ii)\)` and `\(iii)\)` the [left-distributivity property of multiplication of natural numbs][bookofproofs$1030] `\(p^+\)` denotes the unique successor of `\(p\)`.

This proves the associativity of "`\( \cdot \)`" for all `\(n,m,p\in\mathbb N\)`.
