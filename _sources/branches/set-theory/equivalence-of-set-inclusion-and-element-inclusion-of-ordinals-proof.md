layout: proof
categories: branches,set-theory
nodeid: bookofproofs$776
orderid: 50
parentid: bookofproofs$730
title: 
description:  Proof of EQUIVALENCE OF SET INCLUSION AND ELEMENT INCLUSION OF ORDINALS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$8055
keywords: element,equivalence,inclusion,ordinals,set,proof
contributors: bookofproofs

---


---

* Let `$\alpha,\beta\in (X,\in_X),$` in which `$X$` is an [ordinal][bookofproofs$723].
* Since [ordinals are downward closed][bookofproofs$727], `$\alpha$` and `$\beta$` are ordinals.

#### "`\(\Leftarrow\)`". 

* Let `$\alpha\subseteq \beta.$`
* If `$\alpha=\beta,$` we are done.
* Assume, therefore that `$\alpha\subset \beta.$`
* We have `$\beta$` is an ordinal, `$\alpha\subset \beta$` and `$\alpha$` is [transitive][bookofproofs$720].
* It follows from the [equivalent notions of ordinals][bookofproofs$8089] that `$\alpha\in \beta.$`

#### "`\(\Rightarrow\)`". 

* Let `$\alpha\in\beta$` or `$\alpha=\beta.$`
* If `$\alpha=\beta$` then `$\alpha\subseteq\beta,$` and we are done.
* Assume, therefore, that `$\alpha\in\beta.$`
* Since `$\beta$` is an [ordinal][bookofproofs$723], `$\beta$` is [transitive][bookofproofs$720], i.e from `$x\in\alpha$` and `$\alpha\in\beta$` it follows that `$x\in \beta$`
* Altogether, it follows that `$\alpha \subset\beta.$`
