layout: proof
categories: branches,set-theory
nodeid: bookofproofs$991
orderid: 50
parentid: bookofproofs$982
title: 
description:  Proof of COUNTING THE SET'S ELEMENTS USING ITS PARTITION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696,bookofproofs$977,bookofproofs$983
keywords: count elements of a set partition,proof
contributors: bookofproofs

---


---

From the rules of [finite cardinals and the union set operation][bookofproofs$988] it follows for any finite sets `\(X\)` and `\(U\)` with `\(X\cap U=\emptyset\)` 

`\[|X\cup U|=|X|+|U|,~~~~~~~~~~~~~~~~~~~~( * )\]`

By hypothesis `\(S\)` is a finite set, `\(S_1,\ldots S_n\subset S\)` are its subsets forming a [partition][bookofproofs$574] of `\(S\)`, i.e. 

`\[S=\bigcup_{i=1}^n S_i,~~~~~~S_i\cap S_j=\emptyset,\forall i\neq j.\]`

and the cardinalities `\(|S_i|\)` are all known `\(i=1,\ldots n\)`. 

We observe that for `\(1\le j\le n\)` we have `\[\left(\bigcup_{i=1}^{n-j}S_i\right)\cap \left(\bigcup_{i=n-j+1}^{n}S_i\right)=\emptyset.\]` It follows from the rule `\(( * )\)` that 
`\[\begin{array}{ccl}
|S|=\left|\bigcup_{i=1}^n S_i\right|&=&\left|\bigcup_{i=1}^{n-1}S_i\right|+|S_n|\\
&=&\left|\bigcup_{i=1}^{n-2}S_i\right|+|S_{n-1}|+|S_n|\\
&\vdots&\\
&=&|S_1|+|S_2|+\ldots+|S_{n-1}|+|S_n|\\
&=&\sum_{i=1}^n |S_i|
\end{array}\]`

Hereby we have used the associativity and commutativity of set union and the [associativity and commutativity of the addition of natural numbers][bookofproofs$841].
.