layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$866
orderid: 50
parentid: bookofproofs$865
title: 
description:  Proof of PROBABILITY OF INCLUDED EVENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: event,included,probability,proof
contributors: bookofproofs

---


---

We first note that

`\[B=\Omega\cap B=(A\cup \overline A)\cap B=(A\cap B)\cup (\overline A\cap B).\]`

By assumption of the [inclusion][bookofproofs$552] `\(A\subset B\)`, we have that `\(A\cap B=A\)`. Therefore

`\[B=A\cup (\overline A\cap B).\]`

Because `\(A \cap (\overline A\cap B)=\emptyset\)`, the events `\(A\)` and `\((\overline A\cap B)\)` are [mutually exclusive][bookofproofs$859]. Therefore, it follows from the [definition of probability][bookofproofs$858] that 

`\[p(B)=p(A)+p(\overline A\cap B)\]`

Because `\(p(\overline A\cap B)\ge 0\)`, we have `\(p(A)\le p(B)\)`, as required.
