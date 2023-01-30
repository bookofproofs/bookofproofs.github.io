layout: proof
categories: branches,logic
nodeid: bookofproofs$7923
orderid: 50
parentid: bookofproofs$7919
title: 
description:  Proof of MODUS TOLLENS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: major premise,minor premise,modus,modus tollens,tollens,proof
contributors: bookofproofs

---


---

We want to prove that [modus tollens][bookofproofs$7919] is a [valid logical argument][bookofproofs$7913].
* Modus tollenscan be formulated in [propositional logic][bookofproofs$1307] as `$((p\Rightarrow q)\wedge \neg q)\Rightarrow \neg p.$`
* Reformulating [the implication as disjunction][bookofproofs$6874] gives us the expression `$((\neg p\vee q)\wedge \neg  q)\Rightarrow \neg p.$`
* On the left side we have only the operations "`$\wedge$`" and "`$\vee$`". Therefore, we can use the fact that [propositional logic is a Boolean algebra][bookofproofs$187] `$(B,\wedge,\vee,1,0)$`, and make use of the properties of this [Boolean algebra][bookofproofs$7872] `$B$` as follows:
`$$\begin{array}{rl}
((\neg p\vee q)\wedge \neg  q)\Rightarrow \neg p&\\
((\neg p \wedge\neg q)\vee (q\wedge \neg q))\Rightarrow \neg p&(\text{distributivity of }"\wedge"\text{ and }"\vee")\\
((\neg p \wedge\neg q)\vee 0)\Rightarrow \neg p&(\neg q\text{ is the complement element of }q)\\
(\neg p \wedge\neg q)\Rightarrow \neg p&(0\text{ is the smallest element of the `$B$`})\\
\end{array}$$`
* It follows from the truth table of [conjunction][bookofproofs$712] that if `$\neg p$` and `$\neg q$` are true, than `$\neg p$` is true.
* By definition of a [valid logical argument][bookofproofs$7913], modus tollens `$((p\Rightarrow q)\wedge \neg q)\Rightarrow \neg p$` is valid.
