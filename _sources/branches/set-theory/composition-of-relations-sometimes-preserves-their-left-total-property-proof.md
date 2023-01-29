layout: proof
categories: branches,set-theory
nodeid: bookofproofs$1313
orderid: 50
parentid: bookofproofs$1312
title: 
description:  Proof of COMPOSITION OF RELATIONS SOMETIMES PRESERVES THEIR LEFT-TOTAL PROPERTY &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$577
keywords: composition,left,preserves,property,relations,sometimes,their,total,proof
contributors: bookofproofs

---


---

Let `\(A,B,C\)` be [sets][bookofproofs$550] and let let `\(R_1\subseteq A\times B\)` and `\(R_2\subseteq B\times C\)` be two [left-total relations][bookofproofs$1308].
### Case `\((1)\)`
 
* Suppose, there exist at least one tripple `$(a,b,c)$` with `$a\in A,$` `$b\in B,$` and `$c\in C$` such that `$aR_1b$` and `$bR_2c$`.
* Since, by hypothesis `\(R_1\)` is left-total, we have for every `\(a\in A\)` that there is an element `\(b\in B\)` with `\(aR_1b\)`. 
* By the same argument, it follows that for every `$b\in B$` there is an element `\(c\in C\)` with `\(bR_2c\)`. 
* Alltogether, for every `$a\in A$` there is an element `$c\in C$` with `$a R_1 b$` and `$b R_2 c$`.
* From the [definition of composition of relations][bookofproofs$1309], it follows that `$(R_2\circ R_1)\subseteq A\times C$` is left-total.

### Case `\((2)\)`: 

* Now suppose that such a tripple `$(a,b,c)$` does not exist.
* Then the lemma is [vacuously true][bookofproofs$781].