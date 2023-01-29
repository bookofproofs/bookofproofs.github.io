layout: definition
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8484
orderid: 100
parentid: bookofproofs$78
title: Abstract Syntax Tree
description: ABSTRACT SYNTAX TREE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: abstract syntax tree,abstract syntax trees,ast,asts
contributors: bookofproofs

---


---

Let `$G=(V,T,R,S)$` be a [grammar][bookofproofs$709], let `$L(G)$` be a [language generated from the grammar][bookofproofs$94], and let `$\omega\in L$` be a [string][bookofproofs$708] of the language. An **abstract syntax tree** of the string `$\omega$` with respect to the grammar `$G$` (denoted by `$\operatorname {AST}_G(\omega)$`) is a [tree][bookofproofs$96] with
* the [starting symbol][bookofproofs$709] `$S$` as the [tree root][bookofproofs$8482],
* all [non-leave][bookofproofs$6366] vertices consisting of [non-terminal symbols][bookofproofs$709] (elements of `$V$` in `$G$`), and
* all [leave][bookofproofs$6366] vertices consisting of the characters of the string `$\omega.$`

### Construction of `$\operatorname {AST}_G(\omega)$`

1. Start with the starting symbol `$S$` as a tree root.
1. Apply a rule `$r\in R$` and expand the tree root[^1]. 
1. In case of the rule `$S\to\epsilon$` ($\epsilon$ being the [empty string][bookofproofs$708]), remove the expanded leaf.
1. Check if all leaves of `$\operatorname {AST}_G(\omega)$` are already non-terminal symbols.
1. If yes, each leaf corresponds to the terminal symbols (characters of the string `$\omega$`).
1. If not, repeat the procedure from the step `$2$` for each non-terminal symbol as a new root of another [subtree][bookofproofs$8482] of `$\operatorname {AST}_G(\omega).$`

[^1]: Note that we still do not know, which rule has to be applied - this will be clarified later when we will be talking about _parsers_.
