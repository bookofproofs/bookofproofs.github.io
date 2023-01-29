layout: proof
categories: branches,set-theory
nodeid: bookofproofs$731
orderid: 50
parentid: bookofproofs$729
title: 
description:  Proof of TRICHOTOMY OF ORDINALS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$8055
keywords: ordinals,trichotomy,proof
contributors: bookofproofs

---


---

* Let `\(\alpha, \beta\)` be fixed ordinals and `\(\gamma=\alpha\cap \beta\)`. 
* By the lemma about [equivalence of set inclusion and element inclusion of ordinals][bookofproofs$730], it follows from   `\(\gamma\subseteq\alpha\)` that `\(\gamma\in\alpha\)` or `\(\gamma=\alpha\)`, and from `\(\gamma\subseteq\beta\)` that `\(\gamma\in\beta\)` or `\(\gamma=\beta\)`. 
* Altogether, we have the following cases:
   * `\(\gamma\in\alpha\)` and `\(\gamma=\beta\)`. From this case it follows that `\(\beta\in\alpha\)`.
   * `\(\gamma\in\beta\)` and `\(\gamma=\alpha\)`. From this case it follows that `\(\alpha\in\beta\)`.
   * `\(\gamma=\beta\)` and `\(\gamma=\alpha\)`. From this case it follows that `\(\alpha=\beta\)`, and by the [axiom of foundation][bookofproofs$717], neither `\(\alpha\in \beta\)` nor `\(\beta\in \alpha\)` is possible. 
   * `\(\gamma\in\beta\)` and `\(\gamma\in\alpha\)`. However, this case is not possible, since otherwise we would have `\(\gamma\in\alpha\cap\beta=\gamma\)`, contradicting the [axiom of foundation][bookofproofs$717].
