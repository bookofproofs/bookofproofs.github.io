layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$8050
orderid: 800
parentid: bookofproofs$185
title: Transitive Set and Countability - Natural Numbers Have the Smallest Infinite Cardinality
description: TRANSITIVE SET AND COUNTABILITY - NATURAL NUMBERS HAVE THE SMALLEST INFINITE CARDINALITY &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: 
keywords: cardinality,countability,have,infinite,natural,numbers,set,smallest,transitive
contributors: bookofproofs

---


---

The [above examples][bookofproofs$8049] as well as the [definition of infinite sets][bookofproofs$985] show that natural numbers `$\mathbb N$` play a prominent role in the study of the cardinality of infinite sets. This is not a coincidence. In the next branch of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>, the [number systems and arithmetics][bookofproofs$195], we will provide a [set-theoretic definition of natural numbers][bookofproofs$718], in which we will be using the [inductive set][bookofproofs$8038] `$\omega$` we have learned about when talking about the [Zermelo-Fraenkel axioms][bookofproofs$1427] of set theory. Thus, we can recap the following facts: 

* The minimal inductive set `$\omega$` is used to define the [natural numbers][bookofproofs$718] `$\mathbb N$`. By this definition, they have the same cardinalities: `$|\mathbb N|=|\omega|.$` 
* When [comparing cardinalities][bookofproofs$984], we have learned that for two given cardinalities the relation `$|A|\le |B|$` is fulfilled if there is an [injective function][bookofproofs$769] `$f:A\to B.$`
* We have shown that `$\omega$` is minimal in the sense that it is the [subset of any existing inductive set][bookofproofs$8039].
* There is always an injective function `$f:A\to B$`, if `$A\subseteq B.$` For instance, take the identity function `$f(a)=a$` for all `$a\in A.$` 

These facts show us that the natural numbers `$\mathbb N$` have the _smallest cardinality_ of all infinite sets. The big question now is: 

bq{color:blue}. Is this the _only possible_ cardinality of infinite sets or are there infinite sets with bigger cardinalities?

In order to make some progress in answering this question, we have to go back again to the definition of [comparing cardinal numbers][bookofproofs$984]. According to this definition, two given cardinalities fulfill the relation `$|A| < |B|,$` if there is an [injective function][bookofproofs$769], but no [surjective function][bookofproofs$770] `$f:A\to B.$` This motivates the following definition.
