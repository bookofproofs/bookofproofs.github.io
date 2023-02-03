layout: part
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$78
orderid: 50
parentid: bookofproofs$70
title: Formal Languages
description: FORMAL LANGUAGES ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: formal languages
contributors: bookofproofs


---


---

In the branch [logic][bookofproofs$25], we have already dealt with [formal languages][bookofproofs$709] `$L\subset\Sigma^*$` over a given [alphabet][bookofproofs$708] `$\Sigma.$` We learned about the "syntax":https://www.bookofproofs.org/branches/syntax-of-a-formal-language/ and [semantics][bookofproofs$7881] of formal languages. We also learned some important examples of formal languages with particular importance for mathematics - the [propositional logic][bookofproofs$7893] `$PL0$` and also the [first-order logic][bookofproofs$186] `$PL1.$`

Unlike in the logic branch, we will use the term _grammar_ instead of the term _syntax_ when dealing with formal languages.

This part belonging to the branch [theoretical computer science][bookofproofs$70] we will deal with formal languages again, but this time from a different perspective - the perspective of _programming_. Theoretical (and practical) problems occurring in conjunction with formal languages in programming include:
* Finding out if an arbitrary [string][bookofproofs$708] `$\omega\in\Sigma^*$` belongs to a given language `$L\subset \Sigma^*$` ("How to write a so-called _parser_ for a given programming language?")
* Finding out if a language `$L\subset \Sigma^*$` with a given "grammar":https://www.bookofproofs.org/branches/syntax-grammar-of-a-formal-language/ has at least one string `$\omega in L$`? ("Does the grammar allow writing computer programs at all"?)
* And if so, is `$L$` [finite or infinite][bookofproofs$985] ("How 'powerful' is a programming language - how many different programs can we write using a given programming language?")
* Do two different grammars describe the same language? ("Can we write the same programs using the two different grammars?")
