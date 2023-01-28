layout: chapter
categories: branches,algebra
nodeid: bookofproofs$120
orderid: 400
parentid: bookofproofs$85
title: Magmas, Semigroups, Monoids (Overview)
description: MAGMAS, SEMIGROUPS, MONOIDS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: magmas,monoids,semigroups,semigroups and monoids,semigroup and monoid,semigroup monoid,monoid properties
contributors: bookofproofs


---


---

With the introduced [properties of binary operations][bookofproofs$115] we are now able to define the first simple algebraic structures (or _algebras_).  The following table shows which algebras will be introduced soon and which properties they require. 


Algebra `$(X,\ast)$`  | [Closure][bookofproofs$1103] | [Associativity][bookofproofs$668] | [Neutral Element][bookofproofs$661] | [Existence of Inverse][bookofproofs$670] | [Cancellation][bookofproofs$837] | [Commutativity][bookofproofs$672]
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
 [Magma][bookofproofs$836]| ✔| (✔)| (✔)| (✔)| (✔)| (✔)
 [Semigroup][bookofproofs$660]| ✔| ✔| (✔)| (✔)| (✔)| (✔)
 [Monoid][bookofproofs$659]| ✔| ✔| ✔| (✔)| (✔)| (✔)

When in the table the entry "(✔)" is used, then it means that the defined binary operation `$"\ast"$` might not fulfill the property at all, which is required, if the sigh "✔" is used. 

If an optional operation is fulfilled anyway, then the name of the algebraic structure is modified. For instance, if in a given semigroup the all elements `$x,y\in X$` commute, i.e. `$x\ast y=y\ast x,$` then we call such a semigroup a _commutative semigroup_. For some combinations, the name might even change. For instance, if `$X$` is a monoid, and inverses exist for all elements of `$X,$` then we have a _group_ in place, but we will introduce groups in a later chapter. In this chapter, we want to concentrate on the tree simple-structure algebras: magma, semigroup, and monoid.
