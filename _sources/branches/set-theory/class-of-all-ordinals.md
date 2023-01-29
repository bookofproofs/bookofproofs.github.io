layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8091
orderid: 1300
parentid: bookofproofs$112
title: The Class of all Ordinals `$\Omega$`
description: THE CLASS OF ALL ORDINALS OMEGA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$8055
keywords: class of all ordinals
contributors: bookofproofs

---
We have seen that [ordinal numbers are downward closed][bookofproofs$727]. But does it also hold in the opposite direction? Is there a "set of all ordinals" `$\Omega$`?

The [Burali-Forti paradox][bookofproofs$779] shows that such a set cannot exist. In other words, the notion of a [set][bookofproofs$550] is [too narrow" to be used for summing up all existing "ordinal numbers][bookofproofs$723].
---

In the terms of the [Neumann-Berneys-Gödel set theory][bookofproofs$8012] (NBG), `$\Omega$` as a collection of _all_ [ordinal numbers][bookofproofs$723] is not a [set][bookofproofs$550] but a [proper class][bookofproofs$8012].

### Notes

* For a proper class, it is forbidden to be an element of a class (especially itself), therefore `$\Omega\not\in\Omega.$`
* Nevertheless, all ordinals `$\alpha\in\Omega$` build an infinite [chain][bookofproofs$6191] of being contained in each other. 
* Remember that we have already constructed the [minimal inductive set][bookofproofs$8038] `$\omega$` independently from the discussion of [ordinal numbers][bookofproofs$723] while we were talking about the [Zermelo-Fraenkel axioms][bookofproofs$1427].
* `$\omega$` can be visualized as follows:


![inductiveset](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/inductiveset.png?raw=true)


Please note that `$\omega\neq\Omega$`, i.e. the _set_ `$\omega$` never can equal (!) the _class_ `$\Omega.$` However, it was constructed using a similar, recursive principle:

1. `$\emptyset \in \omega$`
1. `$\emptyset \in \omega$`
