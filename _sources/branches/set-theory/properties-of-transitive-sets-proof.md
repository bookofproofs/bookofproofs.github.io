layout: proof
categories: branches,set-theory
nodeid: bookofproofs$722
orderid: 50
parentid: bookofproofs$721
title: 
description:  Proof of PROPERTIES OF TRANSITIVE SETS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: 1a),1b),2a),2b),properties,sets,transitive,proof
contributors: bookofproofs

---


---

p. **1a)** Let `\(Y\in X\cup\{X\}\)`. We have to show that `\(Y\subseteq X\cup\{X\}\)`, if `\(X\)` is a [transitive set][bookofproofs$720]. It follows
`\[Y\in X\cup\{X\}\Longrightarrow\cases{
Y=X\overset{\text{trivially}}{\Longrightarrow}  Y\subseteq X\\
\text{or}\\
Y\in X\overset{X\text{ is transitive}}{\Longrightarrow} Y\subseteq X
}
\]`
Altogether, it follows that `\(Y\subseteq X\cup\{X\}\)`.

p. **1b)** Let `\(Y\in \mathcal P(X)\)`. We have to show that `\(Y\subseteq \mathcal P(X)\)`, if `\(X\)` is a [transitive set][bookofproofs$720]. Since `\(Y\in \mathcal P(X)\)`, it follows from the definitions of the [power set][bookofproofs$552] that `\(Y\subseteq X\)`. This means that for all elements `\(Y^\prime\in Y\)` it is also `\(Y^\prime\in X\)` and, because of its transitivity `\(Y^\prime \subseteq X\)`. Now it follows from the definition of power set again that `\(Y^\prime \subseteq \mathcal P(X)\)`.

p. **2a)** Let `\(Y\in \bigcup X\)`. We have to show that `\(Y\subseteq \bigcup X\)`, if `\(X\)` is a set of [transitive sets][bookofproofs$720] `\(Y\in \bigcup X\)` means that `\(Y\)` is the element of the union of all elements `\(Z\in X\)`, i.e. `\(Y\in Z\)` for at least of one such `\(Z\)`. Because of the transitivity of `\(Z\)` it is `\(Y\subseteq Z\)` and so `\(Y\subseteq \bigcup X\)`.

p. **2b)** Let `\(Y\in \bigcap X\)`. We have to show that `\(Y\subseteq \bigcap X\)`, if `\(X\)` is a set of [transitive sets][bookofproofs$720] `\(Y\in \bigcap X\)` means that `\(Y\)` is the element of all elements `\(Z\in X\)`, i.e. `\(Y\in Z\)` for all `\(Z\in X\)`. Because each such `\(Z\)` it transitive, it follows `\(Y\subseteq Z\)` for all `\(Z\)` and so `\(Y\subseteq \bigcap X\)`.
