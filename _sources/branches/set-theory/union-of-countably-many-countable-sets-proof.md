layout: proof
categories: branches,set-theory
nodeid: bookofproofs$797
orderid: 50
parentid: bookofproofs$796
title: 
description: Proof of UNION OF COUNTABLE MANY COUNTABLE SETS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: union of countably many sets,union of countably many countable sets,countably many countable sets,countable,proof
contributors: bookofproofs

---


---

* Since each `\(D_n\)` is [countable][bookofproofs$772] by hypothesis, we can write `\(D_n=\{x_{nm},~m\in\mathbb N\}\)`. 
* We claim, that the union 
`\[M:=\bigcup_{n\in\mathbb N} D_n\]` is again countable. 
* In order to see it, we write the elements of the union in a table:
`\[\begin{array}{ccccccc}
\left(x_{00}\right)_0,&\left(x_{01}\right)_1,&\left(x_{02}\right)_3,&\left(x_{03}\right)_6,&\left(x_{04}\right)_{10},&\cdots\\
\left(x_{10}\right)_2,&\left(x_{11}\right)_4,&\left(x_{12}\right)_7,&\left(x_{13}\right)_{11},&\cdots\\
\left(x_{20}\right)_5,&\left(x_{21}\right)_8,&\left(x_{22}\right)_{12},&\cdots\\
\left(x_{30}\right)_{9},&\left(x_{31}\right)_{13},&\cdots\\
\left(x_{40}\right)_{14},&\cdots\\
\vdots
\end{array}\]`
* The outer index defines an [injective function][bookofproofs$769] `\(f:M\mapsto\mathbb N\)`. Therefore, `\(M\)` is countable.
