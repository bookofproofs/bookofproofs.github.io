layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8014
orderid: 50
parentid: bookofproofs$8013
title: 
description:  Proof of UNIQUENESS OF THE EMPTY SET &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: empty,set,uniqueness,proof
contributors: bookofproofs

---


---

* For any two given non-empty sets `$X,Y$` assume, their elements `$x\in X,y\in Y$` are sets themselves.
* By the [extensionality principle][bookofproofs$551] they are equal `$x=y$` if they have the same elements.
* This argument can be repeated for the elements of these elements (if any). We can repeat this argument for all elements of elements of elements, etc.
* At some point, we might arrive at elements `$x\in X$` and `$y\in Y$` which do not contain any elements. Note that the existence of such empty elements `$x=\emptyset$` and `$y=\emptyset$` is ensured by the [axiom of empty set][bookofproofs$666].
* Now, the extensionality principle says again, that `$x=y$` are equal, even though `$x=\emptyset$` and `$y=\emptyset$`.
* In other words, all empty sets are not distinguishable. Thus, `$\emptyset$` is unique.
