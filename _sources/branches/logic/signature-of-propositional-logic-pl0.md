layout: definition
categories: branches,logic
nodeid: bookofproofs$7893
orderid: 50
parentid: bookofproofs$66
title: Signature of Propositional Logic - PL0
description: SIGNATURE OF PROPOSITIONAL LOGIC - PL0 &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7878
keywords: logic,pl0,propositional,propositional logic,signature
contributors: bookofproofs

---
Propositions can be formulated in natural languages, e.g. the English sentence "It is raining" is a proposition. However, natural languages have complex grammars and are too ambiguous to strictly define a logical calculus of a propositional logic. Therefore, we will concentrate on the main elements needed to construct a propositional logic and leave everything else as a superfluous ballast out of our definition.

---

The [signature][bookofproofs$6224] `$(V,F,P)$` of a **propositional logic** consists of 

* A set of [variables][bookofproofs$6220] `$V$`. We will denote variables by (indexed) Latin letters, e.g. `$a,b,\ldots$`, `$x_1,y_1,\ldots.$`
* A set of [n-ary functions][bookofproofs$6222]:
   *  [constants][bookofproofs$6222] `$1,0$` as nullary functions
   * and functions taking `$n\ge 1$` arguments as input and assigning the input either the constant `$1$` or `$0$` as output.
* An [empty set][bookofproofs$550] of predicates `$P=\emptyset$`.  

Because the set of predicates `$P$` is empty, the propositional logic is also called *zeroth-order predicate logic* and denoted by `$PL0$`.
