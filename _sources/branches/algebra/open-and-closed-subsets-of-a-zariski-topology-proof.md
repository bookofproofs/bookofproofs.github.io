layout: proof
categories: branches,algebra
nodeid: bookofproofs$6327
orderid: 50
parentid: bookofproofs$6262
title: 
description: PROOF OF OPEN AND CLOSED SUBSETS OF A ZARISKI TOPOLOGY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6907
keywords: closed,open,subsets,topology,zariski,proof
contributors: bookofproofs

---


---

We only provide a sketch of a proof:

### ad `\((1)\)` 

* From the [lemma about the one-to-one correspondence of ideals in a factor ring and a commutative ring][bookofproofs$6248] it follows that the [prime ideals][bookofproofs$6240] in the [factor ring][bookofproofs$274] `\(R/{I}\)` correspond over the ideal `\({J}\mapsto q^{-1}({J})={J}+{I}\)` to the prime ideals of `\(R\)` containing the ideal `\({I}\)`. 
* Therefore, the [spectrum function][bookofproofs$6242] `\(q^{ * }\)` is [bijective][bookofproofs$771] and has the [image][bookofproofs$592] being the set `\(V(I)\)` of all ideals of `\(R\)` containing `\(I\)`.
* It is also [closed][bookofproofs$6242], since for any ideal `\({K}\subseteq R/{I}\)` and a prime ideal `\({J}\subseteq R/{I}\)` we have `\({K}\subseteq {J}\)` if and only if `\[{K}+{I}=q^{-1}({K})\subseteq {J}+{I}.\]` Therefore the image of `\(V({K})\)` equals the image of `\(V({K}+{I})\)` and thus, it is closed.

### ad `\((2)\)` 

* This follows immediately from the [lemma about prime ideals of multiplicative systems in integral domains][bookofproofs$6244]

### ad `\((3)\)` 

* Note that for any prime ideal `\({J}\)` and an element `\(f\in R\)` we have `\(f\not \in {J}\)` if and only if `\({J}\)` is disjoint to the [multiplicative system][bookofproofs$6234] `\(\left\{f^{n}{|}\,n\in \mathbb {N} \right\}\)`.
* From that note, it follows together with `\((2)\)` that the map is [injective][bookofproofs$769] and its image equals `\(D(f)\)`. 
* The same argument applied on `\(g\in R\)` respectively `\({\frac {g}{1}}\in R_{f}\)` reveals that the image of `\(D(g)\subseteq \operatorname {Spek} \left(R_{f}\right)\)` equals `\(D(fg)\)` and is therefore open.
