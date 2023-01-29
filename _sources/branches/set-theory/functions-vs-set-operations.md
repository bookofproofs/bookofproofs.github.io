layout: lemma
categories: branches,set-theory
nodeid: bookofproofs$294
orderid: 500
parentid: bookofproofs$64
title: Behavior of Functions with Set Operations
description: BEHAVIOR OF FUNCTIONS WITH SET OPERATIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038
keywords: functions,operations,set
contributors: bookofproofs

---
In one of the previous chapters, we have learned about basic [operations on sets][bookofproofs$7986] like for instance the [set union][bookofproofs$6827], the `$A\cup B$`, or the [set intersection][bookofproofs$6828], `$A\cap B,$` or [set difference][bookofproofs$6830] `$A\setminus B$`. It turns out that [functions][bookofproofs$592] always behave in a certain way in conjunction with set operations, regardless of the kind of functions and the kind of sets involved. We now want to prove some of these behavior rules.

---

Let `$A,B$` be arbitrary [sets][bookofproofs$550]. For arbitrary [functions][bookofproofs$592] `$f:A\mapsto B$` the following rules hold:

1. `$f[X\cup Y]=f[X]\cup f[Y]$` for all [subsets][bookofproofs$552] of `$X,Y\subseteq A.$`
1. `$f[X\cap Y]\subseteq f[X]\cap f[Y]$` for all `$X,Y\subseteq A.$`
1. `$f^{-1}[X\cup Y]=f^{-1}[X]\cup f^{-1}[Y]$` for all `$X,Y\subseteq B.$`
1. `$f^{-1}[X\cap Y]=f^{-1}[X]\cap f^{-1}[Y]$` for all `$X,Y\subseteq B.$`
1. `$f[A\setminus X]\supseteq f[A]\setminus f[X]$` for all `$X \subseteq A.$`
1. `$f^{-1}[B\setminus X]=A\setminus f^{-1}[X]$` for all `$X\subseteq B.$`
1. `$f^{-1}[f[X]]\supseteq X$` for all `$X\subseteq A.$`
1. `$f^{-1}[f[X]]\supseteq X$` for all `$X\subseteq A.$`
