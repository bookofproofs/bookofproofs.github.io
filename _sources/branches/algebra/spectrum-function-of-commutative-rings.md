layout: proposition
categories: branches,algebra
nodeid: bookofproofs$6249
orderid: 50
parentid: bookofproofs$6245
title: Spectrum Function of Commutative Rings
description: SPECTRUM FUNCTION OF COMMUTATIVE RINGS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: commutative,function,rings,spectrum
contributors: @Brenner,bookofproofs

---


---

Let `\(\varphi \colon R\longrightarrow S\,\)` be a [ring homomorphism][bookofproofs$885] between two [commutative rings][bookofproofs$880]. The following [function][bookofproofs$592], which maps the [spectra][bookofproofs$6245] of both rings is well-defined and called the **spectrum function** (given the homomorphism `\(\varphi\)`).
`\[\varphi ^{ * }\colon \cases{\operatorname {Spec} \left(S\right)\longrightarrow \operatorname {Spec} \left(R\right),\cr I \longmapsto \varphi ^{ * }(I):=\varphi ^{-1}(I)}\]`

The spectrum function fulfills the following properties: 
* `\(\varphi\)` is [continuous][bookofproofs$6195].
* For every [ideal][bookofproofs$1062] `\(I\lhd R\)`, we have `\((\varphi ^{ * })^{-1}(D(I))=D(IS)\)`, where `\(D\)` denotes [open sets of the Zariski topology][bookofproofs$6246] on `\(R\)`.
* For any another ring homomorphism `\(\psi \colon S\longrightarrow T\,\)` it follows `\((\psi \circ \varphi )^{ * }=\varphi ^{ * }\circ \psi ^{ * }.\)`
