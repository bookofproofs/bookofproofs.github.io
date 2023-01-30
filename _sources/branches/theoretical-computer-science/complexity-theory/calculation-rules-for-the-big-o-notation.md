layout: proposition
categories: branches,theoretical-computer-science, complexity-theory
nodeid: bookofproofs$1167
orderid: 100
parentid: bookofproofs$203
title: Calculation Rules for the Big O Notation
description: CALCULATION RULES FOR THE BIG O NOTATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: big,calculation,notation,rules
contributors: bookofproofs

---


---

Let `\(g,f\)`, be two functions of natural numbers to real numbers and let `\(c > 0\)` be a real number, formally `\(g,f:\mathbb N\mapsto\mathbb R\)`, `\(c\in\mathbb R_+\)`. For the [big `\(\mathcal O\)`-Notation][bookofproofs$1087], the following rules of calculation hold:

> `\((1)\)` `\(f=\mathcal O(f)\)`

> `\((2)\)` `\(c\cdot \mathcal O(f)=\mathcal O(f)\)` for all `\(c > 0\)`.

> `\((3)\)` `\(\mathcal O(\mathcal O(f))=\mathcal O(f)\)`

> `\((4)\)` `\(\mathcal O(f)\cdot \mathcal O(g)=\mathcal O(f\cdot g)\)`

> `\((5)\)` `\(\mathcal O(f\cdot g)=|f|\cdot  \mathcal O(g)\)`

> `\((6)\)` If `\(|f(n)|\le |g(n)|\)` for sufficiently large `\(n\)`, then `\(\mathcal O(f)= \mathcal O(g)\)`.
