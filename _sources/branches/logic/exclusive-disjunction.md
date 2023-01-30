layout: definition
categories: branches,logic
nodeid: bookofproofs$7869
orderid: 200
parentid: bookofproofs$713
title: Exclusive Disjunction
description: EXCLUSIVE DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: disjunction,exclusive
contributors: bookofproofs


---


---

In order to reflect the more natural meaning of `$x$` __or__ `$y$`, which is "either `$x$` or `$y$`, but not both", 
we introduce another [Boolean function][bookofproofs$1316], called the **exclusive disjunction** "`$\oplus$`", 
 (sometimes also called the "exclusive or"). 

For any given [propositions][bookofproofs$1307] `$x$` and `$y$`, the exclusive disjunction `$x\oplus y$` is defined using the [conjunction][bookofproofs$712], [disjunction][bookofproofs$713] and [negation][bookofproofs$714]:

`$$x\oplus y:=(x\vee y)\wedge \neg(x\wedge y),$$`

expressing 

"$x$ __or__ `$y$`, __but__ __not__ both."

The [truth table][bookofproofs$7868] of the exclusive disjunction is given by:


Truth Table of Exclusive Disjunction
:-------------
 `$[[x]]_I$`| `$[[y]]_I$`| `$[[x\oplus y]]_I$`
 `$1$`| `$1$`| `$0$`
 `$0$`| `$1$`| `$1$`
 `$1$`| `$0$`| `$1$`
 `$0$`| `$0$`| `$0$`

### Notes

* The exclusive disjunction of two propositions is only true if exactly one of the propositions is true. Otherwise, it is false.
