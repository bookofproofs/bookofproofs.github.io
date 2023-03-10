layout: definition
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8494
orderid: 50
parentid: bookofproofs$107
title: Type-3 (Linear) Grammars and Regular Languages
description: TYPE-3 (LINEAR) GRAMMARS AND REGULAR LANGUAGES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: type-3 grammar,linear grammar,left-linear,right-linear,type-3 grammars,linear grammars,left-linear grammar,right-linear grammar,left-linear grammars,right-linear grammars,type-3,type-0 grammars,regular language,regular languages,regular
contributors: bookofproofs

---


---

A *type-3* (or **linear**) grammar is a [grammar][bookofproofs$709] `$G=(V,T,R,S)$` in which every rule `$P\to Q\in R$` allows the replacement of _only one_ [variable][bookofproofs$709] and the variable is at one end (left-side or right-side) of a production rule. There are two types of linear grammars:

* *left-linear* if and only if all grammar rules `$P\to Q\in R$` consist of `$P\in V$` (the [premise][bookofproofs$709] `$P$` is a [variable][bookofproofs$709]) and `$Q\in V T^+\cup \{\epsilon\}$` (the [conclusion][bookofproofs$709] `$Q$` is either the [empty string][bookofproofs$708] `$\epsilon$` or it is a [concatenation][bookofproofs$8492] _starting_ with a variable, followed by some non-empty [string][bookofproofs$708] of [terminals][bookofproofs$709]).
* *right-linear* if and only if all grammar rules `$P\to Q\in R$` consist of `$P\in V$` (the premise `$P$` is a variable) and `$Q\in T^+V\cup \{\epsilon\}$` (the conclusion `$Q$` is either the empty string or it is a concatenation of some non-empty string of terminals _ending_ with a variable).

[Formal languages][bookofproofs$94] generated by type-3 grammars are called **regular**.

### Notes

* The characteristics of type-3 grammars is that they always replace a single variable by the empty word or a concatenation of terminals ending or starting with a single variable.
* The notation `$T^+$` denotes the [Kleene plus][bookofproofs$8493] of all terminal symbols.
