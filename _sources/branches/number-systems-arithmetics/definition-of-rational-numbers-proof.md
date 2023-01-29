layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1034
orderid: 50
parentid: bookofproofs$1033
title: 
description:  Proof of DEFINITION OF RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: numbers,rational,rational numbers,rational number,definition of rational number,definition of rational numbers,is -1 a rational number,is zero a rational number,define rational number,rational numbers def,rational numbers definition,rational number definition,rational numbers meaning,proof
contributors: bookofproofs

---


---

Let `\((a,b),(c,d)\)` be [ordered pairs][bookofproofs$747] of [integers][bookofproofs$844], such that `\(b\)` and `\(d\)` do not equal the [integer number zero][bookofproofs$1452] `\(0\)`. We will prove that the relation defined using [integer products][bookofproofs$891].
`\[\frac ab \sim \frac cd\quad:=\quad(a,b)\sim(c,d)\quad\Longleftrightarrow\quad ad = bc\]`
is an [equivalence relation][bookofproofs$574]. In other words, the rational numbers as equivalence classes `\(x:=\{(c,d),~(c,d)\sim (a,b)\}\)` are well-defined.

### `\(( i )\)` Reflexivity `\(\frac ab\sim \frac ab\)`

Clearly, `\(ab=ab\)`.

### `\(( ii )\)` Symmetry `\(\frac ab\sim \frac cd\Leftrightarrow\frac cd\sim\frac ab\)`

Since `\(ad=cb\Leftrightarrow cb=ad\)`.

###  `\(( iii )\)` Transitivity: If `\(\frac ab\sim \frac cd\)` and `\(\frac cd\sim \frac ef\)`, then `\(\frac ab\sim \frac ef\)` 

By hypothesis, `\(ad=cb\)` and `\(cf=ed\)`. Multiplying both sides of the two equations together gives us `\((ad)(cf)=(cb)(ed)\)`, which because of the [commutativity][bookofproofs$1448] and [associativity][bookofproofs$1450] of the integer multiplication is equivalent to `\((af)(cd)=(eb)(cd)\)`. If `\(cd\neq 0\)`, we can conclude immediately `\(af=eb\Rightarrow\frac ab\sim\frac ef\)` because the [cancellation property of integer multiplication][bookofproofs$1464].
Therefore, assume `\(cd=0\)`. Because [integers form an integral domain][bookofproofs$892], a product of integers can be only `\(0\)`, if at least one factor equals `\(0\)`. Because `\(d\neq 0\)` by hypothesis, we must have `\(c=0\)`. In this case we can conclude from `\(ab=cd\)` that `\(a=0\)`, because of the same argument `\(b\neq 0\)`. Similarly, we can conclude from `\(cd=ed\)` that `\(e=0\)`, because of the same argument `\(f\neq 0\)`. Therefore, `\((af)(cd)=(eb)(cd)\)` is the trivial equation `\(0\cdot 0=0\cdot 0\)` and again `\(af=eb\Rightarrow\frac ab\sim\frac ef\)`.
