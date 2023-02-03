layout: part
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$118
orderid: 100
parentid: bookofproofs$195
title: Integers
description: INTEGERS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: integers
contributors: bookofproofs


---


---

### A motivation for the set of integers `\(\mathbb Z\)`

It is broadly known and usually taught already in the elementary school that the set of [natural numbers][bookofproofs$103] `\(\mathbb N=\{0,1,2,3,\ldots\}\)` can be extended to the set of all **integers** `\(\mathbb Z=\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}\)` by introducing the negative whole numbers:`\(-1,-2,-3,\ldots\)`. The major motivation for this extension is the solvability of the equation
`\[a+x=b,~~~~~~~(a,b\in\mathbb N)~~~~~~~~~~~~~~~~~~( * )\]`
which cannot be solved by a natural number for any two given initial values `\(a,b\in\mathbb N\)`. For instance, while `\(2+x=5\)` has the solution `\(3\in\mathbb N\)`, there is no such solution (in the set `\(\mathbb N\)`) of the equation `\(9+x=5\)`. The main reason for the (in general) missing solutions to the equation `\(( * )\)` is the [algebraic structure of natural numbers together with addition][bookofproofs$841], which turns out to be a [cancellative][bookofproofs$837] and [commutative][bookofproofs$672] [semigroup][bookofproofs$660] (more precisely a special case of a semigroup called [monoid][bookofproofs$659]).

The following questions arise:

1. Which is "the smallest extended" algebraic structure, in which the equation `\(( * )\)` becomes solvable, regardless which initial natural numbers `\(a,b\in\mathbb N\)` we choose? 
1. Exactly which features of this extended algebraic structure make the equation `\(( * )\)` solvable?
1. Which technical steps are necessary to find this extended algebraic structure? 
1. How can these steps be logically derived from axioms?

This part of <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> is dedicated to the set of integers. In particular, it provides answers to questions raised above. It turns out that the answer to the 1st question is the algebraic structure `\((\mathbb Z, + )\)`, which is the (additive) commutative group of integers. Anticipating the answer to the 2nd question, the solvability of `\(( * )\)` is then ensured by the existence of uniquely defined inverse elements `\(a^{-1}\in \mathbb Z\)` (which are usually written in the additive notation `\( - a\in \mathbb Z\)`), for which `\(( * )\)` can be solved by 

`\[a+x=b~~~\Longleftrightarrow~~~x=(-a + b).\]`
The technical steps necessary to establish `\((\mathbb Z, + )\)` as a new (and [well-defined][bookofproofs$558]) algebraic structure (3rd question), turn out to be a simple application of the theorem dealing with the [construction of groups from commutative cancellative semigroups][bookofproofs$839]. By "applying this theorem to the special case":https://www.bookofproofs.org/branches/definition-of-integers/proof/ of the respective semigroup `\((\mathbb N, + )\)`, we will be led to the structure of `\((\mathbb Z, + )\)`. Finally, the answer to the 4th question is established in <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong> for each theorem separately, providing overviews of the proceeding mathematical results derived from basic axioms (learn more about the "axiomatic method":https://www.bookofproofs.org/about/?details=motivation#axiomaticmethod1).
