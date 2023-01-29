layout: definition
categories: branches,theoretical-computer-science, complexity-theory
nodeid: bookofproofs$1087
orderid: 50
parentid: bookofproofs$203
title: Big O Notation
description: BIG O NOTATION PAUL BACHMANN 1894 &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: big,notation,paul bachmann big o
contributors: bookofproofs

---


---

Let `\(g,f:\mathbb N\mapsto\mathbb R\)` be two [functions][bookofproofs$592] of [natural numbers][bookofproofs$718] to [real numbers][bookofproofs$1105]. We say that `\(f\)` **has order of** `\(g\)` and write `\[f=\mathcal O(g),\quad\quad( * )\]` if and only if there is a positive constant `\(c\in\mathbb R_+\)` such that for all sufficiently large `\(n\in\mathbb N\)`, i.e. all `\(n \ge N( c )\)`[^1] the [absolute values][bookofproofs$583] of both functions fulfill the following relation:

`\[|f(n)|\le c|g(n)|\]`

Note: The use of "`\(=\)`" in `\(( * )\)` is somewhat different from a usual equation. This notation does not mean that `\(f\)` "equals" `\(\mathcal O(g)\)`. It rather means that, while `\(f\)` is a function, `\(\mathcal O(g)\)` is a whole class of functions `\(g\)` such that for each such `\(g\)` there exists constants `\(c\)` and `\(N(c)\)` such that `\(|f(n)|\le c|g(n)|\)` for all `\(n\ge N( c )\)`. 

[^1]: The number `\(N( c )\)` depends on the constant `\(c\)`.
