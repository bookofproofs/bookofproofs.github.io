layout: definition
categories: branches,logic
nodeid: bookofproofs$714
orderid: 300
parentid: bookofproofs$7871
title: Negation
description: NEGATION &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7838
keywords: negation
contributors: bookofproofs


---
After we have explained what [Boolean functions][bookofproofs$1316] and what [truth tables][bookofproofs$7868] are, it is time to use these concepts to introduce important examples of connectives.

---

Let `\(L\)` be a [set of propositions][bookofproofs$1307] with the [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$`. 
A **negation** "`\(\neg\)`" is a [Boolean function][bookofproofs$1316].
`\[\neg :=\begin{cases}L & \mapsto  L \\
x &\mapsto \neg x \\
\end{cases}\]`

defined by the following [truth table][bookofproofs$7868]:


Truth Table of the Negation

 `$[[x]]_I$`| `$[[\neg x]]_I$`
:-------------|:---
 `\(1\)`| `\(0\)`
 `\(0\)`| `\(1\)`

### Notes

* The negation of any proposition changes from one truth value to the other. 
* By the [axiom of bivalence of truth][bookofproofs$705], the negation of any negated proposition `$\neg x$` must be the proposition itself: `$\neg(\neg x)=x.$` 
* Later in the text, it will turn out that negation is one of the most important connectives: We can construct successfully logical systems even if we dispense some connectives, but we cannot do without the negation.
