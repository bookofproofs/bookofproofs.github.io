layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1031
orderid: 50
parentid: bookofproofs$1030
title: By Induction
description: PROOF BY INDUCTION Proof of DISTRIBUTIVITY LAW FOR NATURAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: distributivity,law,natural,numbers,proof
contributors: bookofproofs

---


---

* For `\(n,m,p\in\mathbb N\)` we will first prove the "right-distributivity law" `\((n+m)\cdot p=(n\cdot p)+(m\cdot p)\)`. The validity of the "left-distributivity law" `\(p\cdot(n+m)=(p\cdot n)+(p\cdot m)\)` then follows from the [commutativity of the multiplication of natural numbers][bookofproofs$1435].
* Let `\(n,m,p\in\mathbb N\)` be arbitrary [natural numbers][bookofproofs$718].
* Considering the introduced binary operations on natural numbers [addition][bookofproofs$842] "`\( + \)`" and [multiplication][bookofproofs$876] "`\(\cdot\)`", we will prove the right-distributivity law `$(n+m)\cdot p=(n\cdot p)+(m\cdot p)$` [by induction][bookofproofs$657]  over `\(p\in\mathbb N\)`. 

#### Base Case `\(p=0\)`.

* For `$p=0$`, `$(n+m)\cdot 0=0=0+0=(n\cdot 0 + m\cdot 0).$`

#### Induction step `\(p\mapsto p^+:= p + 1\)`.

* Let the rule `\((n+m)\cdot p=(n\cdot p + m\cdot p)\)` be proven for all `\(p\ge 0\)`. 
* According to the [definition of multiplication of natural numbers][bookofproofs$876] we have  `$$(n+m)\cdot p^+:=(n+m)\cdot p + (n+m).\quad\quad( * )$$`
* On the other hand, it follows from the [commutativity of the addition of natural numbers][bookofproofs$1430] that
`$$\begin{array}{ccl}
(n\cdot p^+ + m\cdot p^+)&=&n\cdot p + n + m\cdot p + m\\
&=&n\cdot p + m\cdot p + n + m,\end{array}$$`
which equals `\( ( * ) \)`, by hypothesis. 
* It follows that `$(n+m)\cdot p^+=(n\cdot p^+ + m\cdot p^+).$`
