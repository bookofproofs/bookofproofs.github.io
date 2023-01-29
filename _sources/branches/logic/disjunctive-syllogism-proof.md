layout: proof
categories: branches,logic
nodeid: bookofproofs$7925
orderid: 50
parentid: bookofproofs$7920
title: 
description:  Proof of DISJUNCTIVE SYLLOGISM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: disjunctive,disjunctive syllogism,major premise,minor premise,syllogism,proof
contributors: bookofproofs

---


---

We want to prove that the [disjunctive syllogism][bookofproofs$7920] is a [valid logical argument][bookofproofs$7913].
* The disjunctive  syllogism can be formulated in [propositional logic][bookofproofs$1307] as `$((p\vee q)\wedge (\neg p))\Rightarrow q.$`
* On the left side of the disjunctive syllogism we have only the operations [$\wedge$" and "$\vee$", we can use the fact that "propositional logic is a Boolean algebra][bookofproofs$187] `$(B,\wedge,\vee,1,0)$`. Applying the properties of this [Boolean algebra][bookofproofs$7872] `$B$` we can conclude that:
`$$\begin{array}{rl}
(p\vee q)\wedge (\neg p)&\\
(p \wedge(\neg p))\vee (q\wedge (\neg p))&(\text{distributivity of }"\wedge"\text{ and }"\vee")\\
0\vee (q\wedge (\neg p))&(\neg p\text{ is the complement element of }p)\\
q\wedge (\neg p)&(0\text{ is the smallest element of the `$B$`})\\
\end{array}$$`
* Therefore, by definition of a [valid logical argument][bookofproofs$7913], the disjunctive syllogism is valid if and only if `$q$` is true, whenever both `$q$` and `$\neg p$` are true. But this is trivial.

This result can also be achieved by calculating the truth table of the whole expression of the disjunctive syllogism, which confirmes that it is a [tautology][bookofproofs$7880]. Please click evaluate to verify this:

§§§1

---

§§§1
<div class='sage'>
import sage.logic.propcalc as propcalc
f = propcalc.formula("((p|q)&(~p))->q")
f.truthtable()

</div>
