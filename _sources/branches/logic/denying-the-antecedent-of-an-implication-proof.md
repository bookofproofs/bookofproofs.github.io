layout: proof
categories: branches,logic
nodeid: bookofproofs$7934
orderid: 50
parentid: bookofproofs$7930
title: 
description:  Proof of DENYING THE ANTECEDENT OF AN IMPLICATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: antecedent,denying,denying the antecedent,implication,proof
contributors: bookofproofs


---


---

We want to prove that the [mixing-up the sufficient and necessary conditions][bookofproofs$7928] is a [fallacy][bookofproofs$7913].
* The fallacy can be formulated in [propositional logic][bookofproofs$1307] as `$(p\Rightarrow q)\wedge \neg p\Rightarrow \neg q.$`
* The definitions of the [implication][bookofproofs$1304] [$\Rightarrow$" and the "negation][bookofproofs$714] [$\neg$" give us the following "truth table][bookofproofs$7868] of the function:


`$[[p]]_I$` | `$[[q]]_I$` | `$[[p\Rightarrow q]]_I$` | `$[[\neg p]]_I$` | `$[[\neg q]]_I$`
:------------- |:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$1$`| `$1$`| `$0$`
 `$1$`| `$0$`| `$0$`| `$0$`| `$1$`
 `$1$`| `$1$`| `$1$`| `$0$`| `$0$`

* In the second row, the premises `$p\Rightarrow q$` and `$\neg p$` are both true, while the conclusion `$\neg q$` is false.
* This is, by definition, the criterion for a fallacy.
