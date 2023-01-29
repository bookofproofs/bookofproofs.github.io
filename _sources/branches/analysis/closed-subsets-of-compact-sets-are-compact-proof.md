layout: proof
categories: branches,analysis
nodeid: bookofproofs$6595
orderid: 50
parentid: bookofproofs$6594
title: 
description:  Proof of CLOSED SUBSETS OF COMPACT SETS ARE COMPACT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: are,closed,compact,sets,subsets,proof
contributors: bookofproofs

---


---

* Let `$(X,d)$` be a [metric space][bookofproofs$617] and let `\(C\subset X\)` be a [compact][bookofproofs$6575] [subset][bookofproofs$552] of `\(X\)`. 
* It has to be shown that any [closed][bookofproofs$852] subset `\(A\subset C\)` is also compact.
   * Let `$U_i)_{i\in I}$` be an [open cover][bookofproofs$150] of `$A$`.
   * Since `\(A\)` is closed, the set `\(X\setminus A\)` is [open][bookofproofs$852].
   * Thus, `$(X\setminus A)\cup\bigcup_{i\in I}U_i=X$` is an open cover of `$C$`.
   * Since `\(C\)` is compact, it has [by definition of compact sets][bookofproofs$6575] a finite subcover `$$C\subset (X\setminus A)\cup U_{i_1}\cup U_{i_2}\cup\ldots\cup U_{i_k}$$` for some `\(i_1,i_2,\ldots,i_k\in I\)`.
   * Because `\(A\subset C\)`, also `\(A\)` has a finite subcover.
   * Thus, `\(A\)` is compact.
