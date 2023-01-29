layout: definition
categories: branches,logic
nodeid: bookofproofs$8493
orderid: 100
parentid: bookofproofs$7842
title: Iteration of Languages, Kleene Star, Kleene Plus
description: ITERATION OF LANGUAGES, KLEENE STAR, KLEENE PLUS, KLEENE CLOSURE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: iteration of languages,kleene star,kleene plus,kleene closure,kleene closures
contributors: bookofproofs


---
We have used already the symbol `$\Sigma^*$` to denote all words over an [alphabet][bookofproofs$708] `$\Sigma$`. The following symbols, proposed by "Stephen Cole Kleene":https://www.bookofproofs.org/history/stephen-cole-kleene (1909 - 1994) prove very useful in theoretical computer science and are generalizations of this concept for any [languages][bookofproofs$7842].
---

Let `$L$` be a [languages][bookofproofs$7842] over an [alphabets][bookofproofs$708] with the [empty word][bookofproofs$708] `$\epsilon$`. The **iteration** `$L^n$` of `$L$` is a repeated [concatenation][bookofproofs$8492] of itself, defined recursively by `$$L^0:=\{\epsilon\}\quad L^{n+1}:=LL^n.$$`

The **Kleene star** `$L^*$` is the [union][bookofproofs$6827] `$$L^*:=\bigcup_{i\ge 0}L^i$$` of all of its iterations (i.e. including the empty word). In comparison, the **Kleene plus** `$L^+$` excludes the empty word: `$$L^+:=L^*\setminus\{\epsilon\}=\bigcup_{i\ge 1}L^i.$$`

The symbols `$L^*$` and `$L^+$` are sometimes also called **Kleene closures** of `$L$`.
