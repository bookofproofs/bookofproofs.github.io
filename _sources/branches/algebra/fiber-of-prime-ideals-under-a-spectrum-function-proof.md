layout: proof
categories: branches,algebra
nodeid: bookofproofs$6263
orderid: 50
parentid: bookofproofs$6261
title: 
description:  Proof of FIBER OF PRIME IDEALS UNDER A SPECTRUM FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6907
keywords: fiber,function,ideals,prime,spectrum,under,proof
contributors: @Brenner,bookofproofs

---


---

By assumption, `\(\varphi \colon R\longrightarrow S\,\)` is a [ring homomorphism][bookofproofs$885] between two [commutative rings][bookofproofs$880] and `\[\varphi ^{ * }\colon \cases{\operatorname {Spek} \left(S\right)\longrightarrow \operatorname {Spek} \left(R\right),\cr J\longmapsto \varphi ^{ * }(J)}\]`
is the corresponding [spectrum function][bookofproofs$6249].
For the [fiber][bookofproofs$592] of a [prime ideal][bookofproofs$6240]  `\(I\in \operatorname {Spek} \left(R\right)\)` under the spectrum function, we want to show the following properties:

### `\(1\)` It equals `\(\operatorname {Spec} (S/IS)\)`.

This follows immediately from the [proposition][bookofproofs$6262].
### `\(2\)` It equals all prime ideals `\(J \in \operatorname {Spec} \left(S\right)\)` with `\(I S\subseteq J\)` and with `\(J \cap \varphi (R\setminus I)=\emptyset \)`.

For a prime ideal `\({J}\lhd S\)` we have `\(\varphi ^{-1}({J})={I}\)` if and only if 

* `\(\varphi ({I})\subseteq {J}\)` and 
* `\(\varphi (R\setminus {I})\subseteq S\setminus {J}\)`. 

The first condition is equivalent to  `\({I}S\lhd {J}\)` und the second to `\(\varphi (R\setminus {I})\cap {J}=\emptyset \,\)`.
