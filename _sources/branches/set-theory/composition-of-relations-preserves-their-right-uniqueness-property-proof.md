layout: proof
categories: branches,set-theory
nodeid: bookofproofs$1311
orderid: 50
parentid: bookofproofs$1310
title: 
description:  Proof of COMPOSITION OF RELATIONS PRESERVES THEIR RIGHT-UNIQUENESS PROPERTY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$577
keywords: composition,preserves,property,relations,right,their,uniqueness,proof
contributors: bookofproofs

---


---

Let `\(A,B,C\)` be [sets][bookofproofs$550] and let let `\(R_1\subseteq A\times B\)` and `\(R_2\subseteq B\times C\)` be two [right-unique relations][bookofproofs$1308].
### Case `\((1)\)`
 
* Suppose, there exist at least one tripple `$(a,b,c)$` with `$a\in A,$` `$b\in B,$` and `$c\in C$` such that `$aR_1b$` and `$bR_2c$`.
* From the right-uniqueness of `$R_1$` it follows that `$b$` is uniquely determined by `$a$`. 
* From the ritht-uniqueness of `$R_2$` it follows that `$c$` is uniquely determined by `$b$`.
* Alltogether, `$c$` is uniquely determined by `$a$`.
* From the [definition of composition of relations][bookofproofs$1309], it follows that `$(R_2\circ R_1)\subseteq A\times C$` is right-unique.

### Case `\((2)\)`: 

* Now suppose that such a tripple `$(a,b,c)$` does not exist.
* Then the lemma is [vacuously true][bookofproofs$781].