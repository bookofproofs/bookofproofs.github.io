layout: definition
categories: branches,logic
nodeid: bookofproofs$710
orderid: 200
parentid: bookofproofs$66
title: Interpretation of Propositions - the Law of the Excluded Middle
description: INTERPRETATION OF PROPOSITIONS - THE LAW OF THE EXCLUDED MIDDLE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$7878
keywords: law of the excluded middle
contributors: bookofproofs


---
As [mentioned above][bookofproofs$7873], the German mathematician <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Leibniz/">Gottfried Wilhelm von Leibniz</a> (1646 - 1716) postulated that _Every judgment is either true or false._ This became known as the **Law of Excluded Middle**. The law of excluded middle only holds in propositional logic `$PL0$` because of its special semantics. We are now able to formally restate the Law of Excluded Middle and define the semantics of `$PL0$`.

---

Let `\(L\)` be a [formal language][bookofproofs$94] with the [syntax of propositional logic][bookofproofs$1307].
### Law of Excluded Middle (modern formulation)

For every [interpretation][bookofproofs$7874] `$I(U,L)$` in any [domain of discourse][bookofproofs$6219] `$U$`, the  [valuation function][bookofproofs$7874] of any string `$s\in L$` is a [partial function][bookofproofs$592].
`\[
[[s]]_I:=\begin{cases}
\in\mathbb B,&\text{ if }s\text{ is a proposition} \\
undefined,&\text{otherwise}
\end{cases}
\]`

Remember that we denote by `$\mathbb B=\{1,0\}$` the [set of truth values][bookofproofs$707].
### An equivalent formulation 

If `$s\in L$` is a proposition, then either `$I\models s$`  or `$I\not{\models} s$` for all [models][bookofproofs$7880] `$I$`, shortly `$$\models s\text{ or }\not {\models} s,$$` where [$\models$" is the "satisfaction relation][bookofproofs$7880].
