layout: definition
categories: branches,logic
nodeid: bookofproofs$94
orderid: 300
parentid: bookofproofs$26
title: Formal Languages Generated From a Grammar
description: FORMAL LANGUAGE GENERATED FROM A GRAMMAR ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: formal language,transitive hull,language generated from a grammar,generated from a grammar,syntactically derived,language generated from the grammar,generated from the grammar,formal languages,reflexive-transitive hull,generated language
contributors: bookofproofs

---
We want to recap the concepts of a [grammar][bookofproofs$709] and a [formal language][bookofproofs$7842] in the following definition.

---

Let `$\Sigma$` be an [alphabet][bookofproofs$708] and `$G=(V,T,R,S)$` be a [grammar][bookofproofs$709] over this alphabet. We say a [string][bookofproofs$708] `$y\in\Sigma^*$` can be **syntactically derived** from another string `$x$` using the grammar `$G$` (denoted by `$x\Rightarrow y$`), if `$$\exists u,w\in (V\cup T)^*, \exists P\to C\in R: (x=uPv\wedge y=uCv).$$`

In other words, `$x\Rightarrow y$` if and only the two strings have the form `$x=uPw$` and `$y=uCw$` (for some other strings `$u,w$`) and there is a rule `$P\to C.$` 

Note that `$y$` can be derived from `$x$` by applying several rules, e.g. `$x\Rightarrow z_1\Rightarrow\cdots\Rightarrow z_n\Rightarrow y$`. It is, therefore, reasonable to require that the set `$R$` of grammar rules is a [transitive relation][bookofproofs$572].
Denoting by `$\Rightarrow^*$` the **transitive hull** of the grammar rule relation `$R,$` we can now state that a [language][bookofproofs$7842] `$L\subset\Sigma^*$` is said to be **generated by the grammar** `$G$` if and only if 

`$$L=L(G)=\{y\in\Sigma^*\mid S\Rightarrow^* y\}.$$`

In this case, we call `$L$` a **formal language**.

### Notes

* In other words, `$L(G)$` consists exactly of those strings `$y\in\Sigma^*$` which can be grammatically derived from the starting symbol `$S$` in only finitely many steps applying the grammar rules. 
* `$L(G)$` consists therefore solely of strings built out of [terminal symbol][bookofproofs$709]s (elements of `$T$`). 
* Any non-terminal symbol (element of `$V$`, variable) plays only a placeholder-role in `$L(G)$` until it gets replaced by a rule in `$R$` by something else.
* Only when we have replaced every non-terminal symbol, we have produced a string of the language `$L(G).$`
