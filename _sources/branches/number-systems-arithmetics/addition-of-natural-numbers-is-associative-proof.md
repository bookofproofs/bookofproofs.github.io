layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1429
orderid: 50
parentid: bookofproofs$1428
title: By Induction
description:  Proof of ADDITION OF NATURAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,associative,natural,numbers,proof
contributors: bookofproofs

---


---

We shall show the associativity of "`\( + \)`" [by induction][bookofproofs$657].
### Base case

For arbitrary `\(n,m\in\mathbb N\)`, it follows from the [definition of addition][bookofproofs$842] that
`\[n+(m+0)=n+m=(n+m)+0.\]`

### Induction step

Now, let assume that `\(n+(m+p_0)=(n+m)+p_0\)` has been proven for all `\(p_0\le p\)`, where we use "`\(\le\)`" as the [order relation of natural numbers][bookofproofs$697]. Then it follows again from the definition of addition that
`\[n+(m+p^+)=n+(m+p)^+=(n+(m+p))^+,\]`
which according to our assumption equals
`\[(n+(m+p))^+=((n+m)+p)^+=(n+m)+p^+.\]`
This proves the associativity of "`\( + \)`" for all `\(n,m,p\in\mathbb N\)`.
