layout: example
categories: branches,logic
nodeid: bookofproofs$7909
orderid: 600
parentid: bookofproofs$7898
title: Examples of Canonical Normal Forms
description: EXAMPLES OF CANONICAL NORMAL FORMS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7895
keywords: canonical,examples,forms,normal,canonical normal form
contributors: bookofproofs


---


---

After we learned in the "proof of the corresponding lemma":https://www.bookofproofs.org/branches/construction-of-conjunctive-and-disjunctive-canonical-normal-forms/proof/ how to construct [canonical normal forms][bookofproofs$7904] of any [proposition][bookofproofs$1307] `$\phi,$` we are now prepared to apply the approach in practice. In any case, we will use the [truth table][bookofproofs$7868] of the corresponding [Boolean function][bookofproofs$1316] `$f_\phi$` as a starting point.

### Example 1

Our first example is a special case. Suppose, we have a proposition containing two Boolean variables `$x,y,$` which is always valid `$\models \phi.$` Then, by [definition of validity][bookofproofs$7880], for every valuation of the two variables, the function `$f_\phi=[[\phi]]_I$` will be valued true. Because there is no row for which `$[[\phi]]_I=0$`, we can construct only [minterms][bookofproofs$7901] and therefore there is only a [disjunctive, but no conjunctive canonical normal form][bookofproofs$7904]. The corresponding truth table and minterms are shown below:


`$[[x]]_I$` | `$[[y]]_I$` | `$[[\phi]]_I$` | Minterms
:------------- |:------------- |:------------- |:-------------
 `$1$`| `$1$`| `$1$`| `$x\wedge y$`
 `$1$`| `$0$`| `$1$`| `$x\wedge \neg y$`
 `$0$`| `$1$`| `$1$`| `$\neg x\wedge y$`
 `$0$`| `$0$`| `$1$`| `$\neg x\wedge \neg y$`

Connecting all minterms with a [disjunction][bookofproofs$713] gives us the disjunctive canonical normal form: 

`$$\operatorname{dcnm}(\phi)=(x\wedge y) \vee (x\wedge \neg y) \vee (\neg x\wedge y) \vee (\neg x\wedge \neg y).$$` 

### Example 2

Let us take a more complex example. Suppose that we are given a proposition `$\psi$` with three variables `$a,b,c$` connected as follows:
`$$\psi:=a\wedge((b\vee c)\wedge \neg a\Rightarrow c)\Leftrightarrow b.$$`

Again, we calculate the truth table as well as the minterms and the maxterms, whenever it is possible:
 `$[[a]]_I$`| `$[[b]]_I$`| `$[[c]]_I$`| `$[[\psi]]_I$`| Minterms| Maxterms
 `$0$` | `$0$`| `$0$`| `$1$`| `$\neg a\wedge\neg b\wedge \neg c$`| 
| `$0$`| `$0$`| `$1$`| `$1$` | `$\neg a\wedge \neg b\wedge c$`| | 
 `$0$`| `$1$`| `$0$`| `$0$`| | `$a\vee \neg b\vee c$`
| `$0$`| `$1$`| `$1$`| `$0$`| | `$a\vee \neg b\vee \neg c$`| 
 `$1$`| `$0$`| `$0$`| `$0$`| | `$\neg a\vee b\vee c$`
 `$1$`| `$0$`| `$1$`| `$0$`| | `$\neg a\vee b\vee \neg c$`
 `$1$`| `$1$`| `$0$`| `$1$`| `$a\wedge b\wedge \neg c$`| 
 `$1$`| `$1$` | `$1$`| `$1$`| `$a\wedge b\wedge c$`| 

Now, we connect the minterms and maxterms by disjunction and conjunction, respectively, and form the [disjunctive (resp. the conjunctive) canonical normal forms][bookofproofs$7904]:

`$$\begin{array}{rcl}\operatorname{dcnm}(\psi)&=&(\neg a\wedge\neg b\wedge \neg c)\vee (\neg a\wedge \neg b\wedge c)  \vee (a\wedge b\wedge \neg c) \vee (a\wedge b\wedge c)\\
\operatorname{ccnm}(\psi)&=&(a\vee \neg b\vee c) \wedge (a\vee \neg b\vee \neg c)  \wedge(\neg a\vee b\vee c) \wedge (\neg a\vee b\vee \neg c).\end{array}$$`


This example also demonstrates that the [connectives][bookofproofs$7867] [implication][bookofproofs$1304] [$\Rightarrow$" and "equivalence][bookofproofs$1305] [$\Leftrightarrow$" which were contained in `$\psi$` could be replaced by the three "standard" connectives "conjunction][bookofproofs$712] "$\wedge$", [disjunction][bookofproofs$713] [$\vee$", and "negation][bookofproofs$714] "$\neg$" without changing the corresponding Boolean function.
