layout: proof
categories: branches,logic
nodeid: bookofproofs$7924
orderid: 50
parentid: bookofproofs$7921
title: 
description:  Proof of HYPOTHETICAL SYLLOGISM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: hypothetical,hypothetical syllogism,major premise,minor premise,syllogism,proof
contributors: bookofproofs


---


---

We want to prove that the [hypothetical syllogism][bookofproofs$7921] is a [valid logical argument][bookofproofs$7913].
* The hypothetical syllogism can be formulated in [propositional logic][bookofproofs$1307] as `$((p\Rightarrow q)\wedge (q\Rightarrow r))\Rightarrow (p\Rightarrow r).$`
* Using the definition of [implication][bookofproofs$1304] [$\Rightarrow `$", we can construct the  following "truth table][bookofproofs$7868]:


$`[[p]]_I$ | `$[[q]]_I$` | `$[[r]]_I$` | `$[[p\Rightarrow q]]_I$` | `$[[q\Rightarrow r]]_I$` | `$[[p\Rightarrow r]]_I$`
:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$0$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$0$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$0$`| `$1$`| `$0$`| `$1$`
 `$0$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`
 `$1$`| `$0$`| `$0$`| `$0$`| `$1$`| `$0$`
 `$1$`| `$0$`| `$1$`| `$0$`| `$1$`| `$1$`
 `$1$`| `$1$`| `$0$`| `$1$`| `$0$`| `$0$`
 `$1$`| `$1$`| `$1$`| `$1$`| `$1$`| `$1$`

* We can see that `$p\Rightarrow r$` is true (valued as `$1$`), whenever `$p\Rightarrow q$` AND `$q\Rightarrow r$` are both true. 
* By definition of a [valid logical argument][bookofproofs$7913], the hypothetical syllogism `$((p\Rightarrow q)\wedge (q\Rightarrow r))\Rightarrow (p\Rightarrow r)$` is valid.

This result can also be achieved by calculating the truth table of the whole expression of the hypothetical syllogism, which confirmes that it is a [tautology][bookofproofs$7880]. Please click evaluate to verify this:

§§§1

---

§§§1
<div class='sage'>
import sage.logic.propcalc as propcalc
f = propcalc.formula("((p->q)&(q->r))->(p->r)")
f.truthtable()

</div>
