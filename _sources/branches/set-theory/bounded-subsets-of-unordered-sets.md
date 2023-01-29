layout: definition
categories: branches,set-theory
nodeid: bookofproofs$6667
orderid: 1000
parentid: bookofproofs$189
title: Bounded Subsets of Unordered Sets
description: BOUNDED SUBSETS OF UNORDERED SETS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1591
keywords: bounded subsets of unordered sets,bounded subset of an unordered set
contributors: bookofproofs

---
You will find in the literature also another definition of bounded sets, which uses an [absolute value][bookofproofs$8659] `$|\cdot|$`. You should be aware that this is a technical tool mathematicians use to create the notion of "bounded sets" even for sets that cannot be ordered. Prominent examples of this kind are [bounded sets of complex numbers][bookofproofs$8554]. This tool is necessary because _bounded sets_  allow many deep new insights into the topology of such sets. Otherwise, these deep insights would be not possible, simply because the underlying set is not ordered.

The tool of an absolute value serves the purpose because an absolute value is a [function][bookofproofs$592] maps the unordered set to the ordered set of [real numbers][bookofproofs$1105] `$(\mathbb R,+,\cdot),$` while preserving some important properties of the underlying unordered set.

Unfortunately, not all unordered sets have an absolute value. In fact, it is convenient to require the set to have a special algebraic structure, called a [field][bookofproofs$557]. Although we are dealing right now with the _set theory_ and _algebra_ is another big branch of mathematics coming much "later" in <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>, we make a small digression to an algebraic topic right now. We want to show that both definitions are equivalent if the underlying set is a [field][bookofproofs$557] with [absolute value][bookofproofs$8659] defined on it.

---

Let `$(F,+,\cdot)$` be a [field][bookofproofs$557] with an [absolute value][bookofproofs$8659] `$f:F\to\mathbb R$` defined on it. Let `$S\subseteq F$` be its [non-empty][bookofproofs$550] [subset][bookofproofs$552] `$S$` is said to be **bounded** if the [image][bookofproofs$592] `$f[S]$` is [bounded][bookofproofs$584] in the set `$\mathbb R$` of [real numbers][bookofproofs$1105], i.e. if there is a [positive real number][bookofproofs$1107] `$B$` such that `$f(x)=|x|\le B$` for all `$x\in S.$`

### Notes

* The relation "`$\le$`" is the common [order relation of real numbers][bookofproofs$1107]. 
* Unordered sets can have only "bounded" subsets, i.e. it does not make sense to distinguish between "bounded below" and "bounded above" subsets, like it was the case for ordered sets.
