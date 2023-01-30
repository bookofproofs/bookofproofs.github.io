layout: proof
categories: branches,logic
nodeid: bookofproofs$7922
orderid: 50
parentid: bookofproofs$7918
title: 
description:  Proof of MODUS PONENS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: major premise,minor premise,modus,modus ponens,ponens,proof
contributors: bookofproofs

---


---

We want to prove that [modus ponens][bookofproofs$7918] is a [valid logical argument][bookofproofs$7913].
* Modus ponens can be formulated in [propositional logic][bookofproofs$1307] as `$((p\Rightarrow q)\wedge p)\Rightarrow q.$` 
* Reformulating [the implication as disjunction][bookofproofs$6874] gives us the expression `$((\neg p\vee q)\wedge p)\Rightarrow q.$`
* On the left side we have only the operations "`$\wedge$`" and "`$\vee$`". Therefore, we can use the fact that [propositional logic is a Boolean algebra][bookofproofs$187] `$(B,\wedge,\vee,1,0)$`, and make use of the properties of this [Boolean algebra][bookofproofs$7872] `$B$` as follows:
`$$\begin{array}{rl}
((\neg p\vee q)\wedge p)\Rightarrow q&\\
(p \wedge(\neg p\vee q))\Rightarrow q&(\text{commutativity of }"\wedge")\\
((p \wedge\neg p)\vee (p\wedge q))\Rightarrow q&(\text{distributivity of }"\wedge"\text{ and }"\vee")\\
(0\vee (p\wedge q))\Rightarrow q&(\neg p\text{ is the complement element of }p)\\
(p\wedge q)\Rightarrow q&(0\text{ is the smallest element of the `$B$`})\\
\end{array}$$`
* It follows from the truth table of [conjunction][bookofproofs$712] that if `$p$` and `$q$` are true, than `$q$` is true.
* By definition of a [valid logical argument][bookofproofs$7913], modus ponens `$((p\Rightarrow q)\wedge p)\Rightarrow q$` is valid.
