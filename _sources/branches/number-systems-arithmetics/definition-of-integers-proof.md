layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$845
orderid: 50
parentid: bookofproofs$844
title: 
description:  Proof of DEFINITION OF INTEGERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: definition,integers,proof
contributors: bookofproofs

---


---

Let `\((a,b),(c,d)\)` be [ordered pairs][bookofproofs$747] of [natural numbers][bookofproofs$718]. We will prove that the relation defined using [addition of natural numbers][bookofproofs$842].
`\[(a,b)\sim (c,d)\quad\Longleftrightarrow\quad\begin{cases}(a+h,b+h)=(c,d)& or\`\(a,b)=(c+h,d+h).\end{cases}\]`

is an [equivalence relation][bookofproofs$574]. In other words, the integers as equivalence classes `\([a,b]:=\{(c,d),~(c,d)\sim (a,b)\}\)` are well-defined.

### `\(( i )\)` Reflexivity `\((a,b)\sim  (a,b)\)`

Clearly, `\((a+0,b+0)=(a,b)\)`.

### `\(( ii )\)` Symmetry `\((a,b)\sim (c,d)\Leftrightarrow(c,d)\sim(a,b)\)`

If `\((a+h,b+h)=(c,d)\)`, then `\((c,d)=(a+h,b+h)\)`, otherwise if `\((a,b)=(c+h,d+h)\)`, then `\((c+h,d+h)=(a,b)\)`.

###  `\(( iii )\)` Transitivity: If `\((a,b)=(c,d)\)` and `\((c,d)\sim (e,f)\)`, then `\((a,b)\sim (e,f)\)` 

For symmetry reasons `\(( ii) \)`, it is sufficient to consider only this case: By hypothesis, `\((a+h_1,b+h_2)=(c,d)\)` and `\((c+h_2,d+h_2)=(e,f)\)` for some `\(h_1,h_2\in\mathbb N\)`. Therefore `\((a+(h_1+h_2)),b+(h_1+h_2))=(e,f)\)`.
