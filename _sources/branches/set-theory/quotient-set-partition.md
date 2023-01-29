layout: definition
categories: branches,set-theory
nodeid: bookofproofs$7991
orderid: 400
parentid: bookofproofs$574
title: Quotient Set, Partition
description: QUOTIENT SET, PARTITION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$573,bookofproofs$577
keywords: partition,quotient set,quotient sets,partitions,partition of a set,what is a quotient set,quotient set definition,quotient set equivalence relation
contributors: bookofproofs

---
The unique properties of any [equivalence relation][bookofproofs$574] `$R\subseteq V\times V$` have important conseqences for the structure of its [equivalence classes][bookofproofs$7990]:
* Every equivalence `$[a]$` is non-empty for all `$a\in V.$` This follows from `$R$` being  [reflexive][bookofproofs$572].
* If `$c\in [a]$` and `$c\in [b]$` then `$a\sim c\sim b$`. Therefore `$[a]=[b]$`. This follows from `$R$` being  [transitive][bookofproofs$572].
* Of course, from `$R$` being [symmetric][bookofproofs$572], we also have `$b\sim c\sim a$`. In fact, the two equivalence classes are equal `$[a]=[b]$` if and only if `$a\sim b.$` In other words, `$[a]$` and `$b$` are equal if `$a\sim b$`, otherwise they are disjoint `$[a]\cap [b]=\emptyset$`. 

Thus, all equivalence classes are a [partition][bookofproofs$8305] of `$V,$` because they are [mutually disjoint][bookofproofs$6227], non-empty subsets: its equivalence classes. Therefore, every equivalence relation `$R\subseteq V\times V$` generates another [set][bookofproofs$550], which we now want to define formally:

---

Let `$R\subseteq V\times V$` be an [equivalence relation][bookofproofs$57]. The [set][bookofproofs$550] of the corresponding [equivalence classes][bookofproofs$7990] `$V/_{R}:=\{[a]|:a\in V\}$` is called the **quotient set** of `$V$` by `$R$`. 

The symbol  `$V/_{R}$` is sometimes also read:

* `$V$` **modulo** `$R$`, or 
* [partition][bookofproofs$8305] of the set `$V$` under `$R$`.

The existence of the quotient set is ensured by the [axiom of choice][bookofproofs$8041].