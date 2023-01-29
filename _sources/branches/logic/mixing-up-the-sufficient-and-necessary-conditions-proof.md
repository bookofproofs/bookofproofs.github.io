layout: proof
categories: branches,logic
nodeid: bookofproofs$7932
orderid: 50
parentid: bookofproofs$7928
title: 
description:  Proof of MIXING-UP THE SUFFICIENT AND NECESSARY CONDITIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: conditions,mixing,necessary,sufficient,proof
contributors: bookofproofs


---


---

We want to prove that the [mixing-up the sufficient and necessary conditions][bookofproofs$7928] is a [fallacy][bookofproofs$7913].
* The fallacy can be formulated in [propositional logic][bookofproofs$1307] as `$(p\Rightarrow q)\Rightarrow (q\Rightarrow p).$`
* The [definition of implication][bookofproofs$1304] [$\Rightarrow$" gives us the following "truth table][bookofproofs$7868] of the function:


`$[[p]]_I$` | `$[[q]]_I$` | `$[[p\Rightarrow q]]_I$` | `$[[(q\Rightarrow p)]]_I$`
:------------- |:------------- |:------------- |:-------------
 `$0$`| `$0$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$1$`| `$0$`
 `$1$`| `$0$`| `$0$`| `$1$`
 `$1$`| `$1$`| `$1$`| `$1$`

* In the second row, the premise `$p\Rightarrow q$` is true, while the conclusion `$q\Rightarrow p$` is false.
* This is, by definition, the criterion for a fallacy.
