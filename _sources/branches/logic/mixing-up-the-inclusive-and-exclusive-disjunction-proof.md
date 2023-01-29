layout: proof
categories: branches,logic
nodeid: bookofproofs$7931
orderid: 50
parentid: bookofproofs$7927
title: 
description:  Proof of MIXING-UP THE INCLUSIVE AND EXCLUSIVE DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823,bookofproofs$7838
keywords: disjunction,exclusive,inclusive,mixing,proof
contributors: bookofproofs


---


---

We want to prove that the [mixing-up the inclusive and exclusive disjunction][bookofproofs$7927] is a [fallacy][bookofproofs$7913].
* The fallacy can be formulated in [propositional logic][bookofproofs$1307] as `$(p\vee q)\wedge p\Rightarrow \neg q.$`
* We get the following [truth table][bookofproofs$7868] of the function due to the definition of [negation][bookofproofs$714] and [implication][bookofproofs$1304]:


`$[[p]]_I$` | `$[[q]]_I$` | `$[[p\vee q]]_I$` | `$[[ \neg q]]_I$`
:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$0$`| `$1$`
 `$0$`| `$1$`| `$1$`| `$0$`
 `$1$`| `$0$`| `$1$`| `$1$`
 `$1$`| `$1$`| `$1$`| `$0$`

* The last row shows that while the premises `$p$` and `$p\vee q$` are both true, the conclusion `$\neg q$` is false.
* This is, by definition, the criterion for a fallacy.
