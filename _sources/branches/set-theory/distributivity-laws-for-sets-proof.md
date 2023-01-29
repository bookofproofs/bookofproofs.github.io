layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8608
orderid: 50
parentid: bookofproofs$8607
title: 
description: PROOF OF DISTRIBUTIVITY LAWS FOR SETS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$7838
keywords: distributivity laws for sets,proof
contributors: bookofproofs

---


---

* By hypothesis, `$A,B,C$` are [sets][bookofproofs$550].
* We will prove that the [distributivity][bookofproofs$682] laws hold for the [set union][bookofproofs$6827] "`$\cup$`" and the [set intersection][bookofproofs$6828] "`$\cap$`".

### Ad "`$(1)$`"

* The first law follows from the [distributivity laws for conjunction and disjunction][bookofproofs$7910] and the respective definitions of the [set union][bookofproofs$6827] and the [set intersection][bookofproofs$6828]:

`$$\begin{array}{rcl}
x\in A\cap (B\cup C) &\Leftrightarrow&x\in A\wedge x\in (B\cup C)\\
&\Leftrightarrow&x\in A\wedge (x\in B\vee  x\in C)\\
&\Leftrightarrow&(x\in A\wedge x\in B)\vee  (x\in A\wedge x\in C)\\
&\Leftrightarrow&x\in (A\cap B)\vee  x\in (A\cap C)\\
&\Leftrightarrow&x\in (A\cap B)\cup (A\cap C)
\end{array}$$`

### Ad "`$(2)$`"

* Again, we use the [distributivity laws for conjunction and disjunction][bookofproofs$7910] and the respective definitions of the [set union][bookofproofs$6827] and the [set intersection][bookofproofs$6828]:

`$$\begin{array}{rcl}
x\in A\cup (B\cap C) &\Leftrightarrow&x\in A\vee x\in (B\cap C)\\
&\Leftrightarrow&x\in A\vee (x\in B\wedge x\in C)\\
&\Leftrightarrow&(x\in A\vee x\in B)\wedge (x\in A\vee x\in C)\\
&\Leftrightarrow&x\in (A\cup B)\wedge x\in (A\cup C)\\
&\Leftrightarrow&x\in (A\cup B)\cap (A\cup  C)
\end{array}$$`
