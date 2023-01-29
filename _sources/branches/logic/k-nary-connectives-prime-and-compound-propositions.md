layout: definition
categories: branches,logic
nodeid: bookofproofs$7867
orderid: 50
parentid: bookofproofs$7871
title: `$k$`-nary Connectives, Prime and Compound Propositions
description: K-NARY CONNECTIVES, PRIME AND COMPOUND PROPOSITIONS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$711
keywords: connective,connectives,compound proposition,compound propositions,prime proposition,prime propositions,k-nary connective
contributors: bookofproofs

---
The semantics of propositional logic involves so-called __connectives__, including the negation "$\neg$", the conjunction "$\wedge$", the disjunction "$\vee$", the inclusion "$\Rightarrow$", and the equivalence "$\Leftrightarrow$". These connectives are important concepts in mathematics on their own. Therefore, they deserve separate definitions. We will introduce them now step by step, starting with a formal definition of connectives.

---

Let `$L$` be a [formal language][bookofproofs$709] with a [syntax of propositional logic `$PL0$`][bookofproofs$1307]. Let `$L'\subset L$` be the subset of all strings of `$L$` which are propositions, i.e. which have a [semantics of `$PL0$`][bookofproofs$7871].
A *$k$-nary connective* is an operation "$\circ$" used to connect `$k$` ($k=1,2,\ldots$) propositions 

* compatible with their syntax, i.e. if `$p_1,\ldots,p_n$` are [propositions][bookofproofs$1307], then `$p_1\circ \ldots\circ p_n$` is also a proposition, and
* for which the [semantics of `$PL0$`][bookofproofs$7871] is properly defined, i.e. if `$[[p_1]]_I, [[p_2]]_I,\ldots, [[p_k]]_I$` are assigned truth values for some interpretation `$I$`, then also `$[[p_1\circ\ldots\circ p_k]]_I$` is an assigned truth value in the same interpretation `$I.$`

Propositions being [Boolean constants][bookofproofs$1307] or a [Boolean variables][bookofproofs$1307] are called **prime propositions**.

Any proposition involing a connective `$p:=p_1\circ\ldots\circ p_k$` is called a *compound proposition.*
