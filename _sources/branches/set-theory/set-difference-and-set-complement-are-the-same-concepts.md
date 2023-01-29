layout: corollary
categories: branches,set-theory
nodeid: bookofproofs$8026
orderid: 700
parentid: bookofproofs$675
title: Set Difference and Set Complement are the Same Concepts
description: SET DIFFERENCE AND SET COMPLEMENT ARE THE SAME CONCEPTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: are,complement,concepts,difference,same,set
contributors: bookofproofs

---
It is no coincidence that the [set difference][bookofproofs$6830] `$A\setminus B =\{x \mid x\in A \wedge x\notin B\}$` and the [set complement][bookofproofs$6829] `$B^C =\{x \mid x\in A\wedge x\notin B\}$`  have the same [set-builder notations][bookofproofs$587]. In fact, they are almost the same mathematical concepts. Certainly, they are equal sets `$B^C=A\setminus B$`, and we therefore also call the set difference `$A\setminus B$` the "relative complement of `$B$` with respect to `$A$`". 
The reason why mathematicians use a separate name "complement" and notation `$B^C$` instead of just talking about the set difference `$A\setminus B$` is that sometimes,
the set `$A$` is so clear from the context that makes a line of thought clearer to leave `$A$` out. 

This is another important consequence of the [axiom of separation][bookofproofs$675]:

---

In the Zermelo-Frankel set theory, no set `$B$` has an "absolute complement" `$B^C$`. This [set complement][bookofproofs$6829] is equal to the [set difference][bookofproofs$6830] `$A\setminus B$` being the **relative complement** of `$B$` with respect to `$A$`. This is true even if we take `$A$` as the [universal set][bookofproofs$7984].