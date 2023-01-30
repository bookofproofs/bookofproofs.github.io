layout: proof
categories: branches,logic
nodeid: bookofproofs$6853
orderid: 50
parentid: bookofproofs$6852
title: 
description:  Proof of DE MORGAN'S LAWS LOGIC &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711
keywords: de morgans laws (logic),de morgans rules,de morgans laws,proof
contributors: bookofproofs


---


---

* Let `$x,y$` be [propositions][bookofproofs$710].
* In the following, we will use the [semantics of propositional logic][bookofproofs$7871], and the definitions of the [conjunction][bookofproofs$712] "`$\wedge$`", the [disjunction][bookofproofs$713] "`$\vee$`", and the [negation][bookofproofs$714] "`$\neg$`".
* We can construct a [truth table][bookofproofs$7868] for `$\neg(x\wedge y)$` and  `$(\neg x)\vee(\neg y)$` respectively:

`$[[x]]_I$` | `$[[y]]_I$` | `$[[\neg x]]_I$` | `$[[\neg y]]_I$` | `$[[x\wedge y]]_I$` | `$[[\neg(x\wedge y)]]_I$` | `$[[(\neg x)\vee (\neg y)]]_I$`
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
 `$1$`| `$1$`| `$0$`| `$0$`| `$1$`| `$0$`| `$0$`
 `$0$`| `$1$`| `$1$`| `$0$`| `$0$`| `$1$`| `$1$`
 `$1$`| `$0$`| `$0$`| `$1$`| `$0$`| `$1$`| `$1$`
 `$0$`| `$0$`| `$1$`| `$1$`| `$0$`| `$1$`| `$1$`

* Since the values in both columns to the right of the table are equal, it follows that the equivalence  `$\neg(x\wedge y)\Leftrightarrow(\neg x)\vee (\neg y)$` is a [tautology][bookofproofs$7880].
* Similarly, we construct truth tables for `$\neg(x\vee y)$` and  `$(\neg x)\wedge(\neg y)$` respectively:
 `$[[x]]_I$`| `$[[y]]_I$`| `$[[\neg x]]_I$`| `$[[\neg y]]_I$`| `$[[x\vee y]]_I$`| `$[[\neg(x\vee y)]]_I$`| `$[[(\neg x)\wedge (\neg y)]]_I$`
 `$1$`| `$1$`| `$0$`| `$0$`| `$1$`| `$0$`| `$0$`
 `$0$`| `$1$`| `$1$`| `$0$`| `$1$`| `$0$`| `$0$`
 `$1$`| `$0$`| `$0$`| `$1$`| `$1$`| `$0$`| `$0$`
 `$0$`| `$0$`| `$1$`| `$1$`| `$0$`| `$1$`| `$1$`

* Since the values in both columns to the right of the table are equal, it follows that the equivalence  `$\neg(x\vee y)\Leftrightarrow(\neg x)\wedge (\neg y)$` is a [tautology][bookofproofs$7880].
* Altogether, we have shown the laws 
`$$\begin{array}{c}\neg(x\wedge y)=(\neg x)\vee (\neg y)\\\neg(x\vee y)=(\neg x)\wedge (\neg y)\end{array}.$$`
