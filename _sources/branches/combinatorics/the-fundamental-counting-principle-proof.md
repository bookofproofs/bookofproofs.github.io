layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$992
orderid: 50
parentid: bookofproofs$111
title: 
description: Proof of THE FUNDAMENTAL COUNTING PRINCIPLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696,bookofproofs$977,bookofproofs$983
keywords: fundamental counting principle,counting principle,proof
contributors: bookofproofs

---


---

* From the rules of [finite cardinals and the Cartesian product][bookofproofs$988] it follows for any finite sets `\(X\)` and `\(U\)` `\[|X\times U|=|X|\cdot |U|,~~~~~~~~~~~~~~~~~~~~( * )\]`
* By hypothesis `\(S_1,\ldots S_n\)` are [finite sets][bookofproofs$985] with the [cardinalities][bookofproofs$980] `\(|S_i|\)`. It follows from the rule `\(( * )\)` that 
`\[\begin{array}{ccl}
|S|&=&|S_1\times\ldots\times S_{n-1}|\cdot|S_n|\\
&=&||S_1\times\ldots\times S_{n-2}|\cdot|S_{n-1}|\cdot|S_n|\\
&\vdots&\\
&=&|S_1|\cdot|S_2|\cdot\ldots\cdot|S_{n-1}|\cdot|S_n|\\
&=&\prod_{i=1}^n |S_i|
\end{array}\]`
* Hereby, the associativity of Cartesian product and the [associativity of the multiplication of natural numbers][bookofproofs$1434] were used.
