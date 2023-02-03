layout: part
categories: branches,combinatorics
nodeid: bookofproofs$293
orderid: 400
parentid: bookofproofs$82
title: Stirling Numbers
description: STIRLING NUMBERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: stirling numbers
contributors: bookofproofs


---


---

Well-known to the reader is probably the following result: If we expand `$(x+1)^n$` for a [positive integer][bookofproofs$1075] by the [binomial theorem][bookofproofs$1397], the occurring coefficients of powers 
`$$(x+1)^n={n \choose 0}x^n+{n \choose 1}x^{n-1}+{n \choose 2}x^{n-2}+\cdots+{n \choose n-1}x^1+{n \choose n}x^0$$` 
are called binomial coefficients which obey a [recurrence formula][bookofproofs$994] `$$\binom nk=\binom {n-1}{k-1} + \binom {n-1}{k}.$$` This recurrence formula can be visualized by arranging the binomial coefficients in the so-called [Pascal's triangle][bookofproofs$1409].
In this part, we will define _Stirling numbers_, named after <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Stirling/">James Stirling</a> (1692 - 1770) that have in many ways properties very similar to those of the binomial coefficients. In particular, it will turn out that there are two types of _Stirling numbers_, and for both types, there are similar recurrence relationships.

Like for binomial coefficients, _Stirling numbers_ of both types have also interesting combinatorial interpretations.
