layout: proof
categories: branches,logic
nodeid: bookofproofs$7911
orderid: 50
parentid: bookofproofs$7910
title: 
description:  Proof of DISTRIBUTIVITY OF CONJUNCTION AND DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$711
keywords: distributivity laws for conjunction and disjunction,proof
contributors: bookofproofs


---


---

We want to show that the [conjunction][bookofproofs$712] "`$\wedge$`" and the [disjunction][bookofproofs$713] "`$\vee$`" are [distributive][bookofproofs$682] over each other.
* It is sufficient to show the following [equivalences][bookofproofs$1305].
`$$\begin{array}{rcl}
x\wedge (y\vee z)&\Longleftrightarrow&(x\wedge y)\vee (x\wedge z),\\
x\vee (y\wedge z)&\Longleftrightarrow&(x\vee y)\wedge (x\vee z),
\end{array}\quad( * )$$`
because the equivalence
`$$\begin{array}{rcl}
(y\vee z)\wedge x&\Longleftrightarrow&(y\wedge x)\vee (z\wedge x),\\
(y\wedge z)\vee x&\Longleftrightarrow&(y\vee x)\wedge (z\vee y)
\end{array}$$`
will follow immediately from the following facts:
   * [conjunction `$\wedge$` is associative][bookofproofs$6844], 
   * [disjunction `$\vee$` is associative][bookofproofs$6846], 
   * [conjunction `$\wedge$` is commutative][bookofproofs$1834], and 
   * [disjunction `$\vee$` is commutative][bookofproofs$1835].
* Using the [truth tables][bookofproofs$7868] of conjunction and disjunction, we construct the truth tables of both sides of the equivalences `$( * )$`:


`$[[x]]_I$` | `$[[y]]_I$` | `$[[z]]_I$` | `$[[x\wedge (y\vee z)]]_I$` | `$[[(x\wedge y)\vee (x\wedge z)]]_I$`
:------------- |:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$0$`| `$0$`| `$0$`
 `$0$`| `$0$`| `$1$`| `$0$`| `$0$`
 `$0$`| `$1$`| `$0$`| `$0$`| `$0$`
 `$0$`| `$1$`| `$1$`| `$0$`| `$0$`
 `$1$`| `$0$`| `$0$`| `$0$`| `$0$`
 `$1$`| `$0$`| `$1$`| `$1$`| `$1$`
 `$1$`| `$1$`| `$0$`| `$1$`| `$1$`
 `$1$`| `$1$`| `$1$`| `$1$`| `$1$`

This can be verified using Sagecell:

§§§1

§§§2

* The comparison of the last columns of the truth tables shows that `$x\wedge (y\vee z)\Longleftrightarrow(x\wedge y)\vee (x\wedge z)$` is a [tautology][bookofproofs$7880].
* The proof of the tautology `$x\vee (y\wedge z)\Longleftrightarrow(x\vee y)\wedge (x\vee z)$` can be done similarily.

---

§§§1
<div class='sage'>
s = sage.logic.propcalc.formula("x&(y|z)")
s.truthtable()
</div>

§§§2
<div class='sage'>
s = sage.logic.propcalc.formula("(x&y)|(x&z)")
s.truthtable()
</div>
