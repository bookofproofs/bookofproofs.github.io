layout: proof
categories: branches,logic
nodeid: bookofproofs$7933
orderid: 50
parentid: bookofproofs$7929
title: 
description:  Proof of AFFIRMING THE CONSEQUENT OF AN IMPLICATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: affirming,affirming the consequent,consequent,implication,proof
contributors: bookofproofs


---


---

We want to prove that the [affirming the consequent of an implication][bookofproofs$7928] is a [fallacy][bookofproofs$7913].
* The fallacy can be formulated in [propositional logic][bookofproofs$1307] as `$(p\Rightarrow q)\wedge q\Rightarrow q.$`
* The [definition of implication][bookofproofs$1304] "`$\Rightarrow$`" gives us the following [truth table][bookofproofs$7868] of the function:


`$[[p]]_I$` | `$[[q]]_I$` | `$[[p\Rightarrow q]]_I$` | `$[[p]]_I$`
:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$1$`| `$0$`
 `$0$`| `$1$`| `$1$`| `$0$`
 `$1$`| `$0$`| `$0$`| `$1$`
 `$1$`| `$1$`| `$1$`| `$1$`

* In the second row, the premises `$p\Rightarrow q$` and `$q$` are both true, while the conclusion `$p$` is false.
* This is, by definition, the criterion for a fallacy.
