layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1803
orderid: 50
parentid: bookofproofs$1802
title: 
description:  Proof of PROBABILITY OF JOINT EVENTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: events,joint,probability,proof
contributors: bookofproofs

---


---

We will first show that for any two [events][bookofproofs$857] `\(A\)` and `\(B\)`, the [probability][bookofproofs$858] of the joint event `\(A\cap B\)` is the [product][bookofproofs$1532] of the [conditional probability][bookofproofs$428] `\(p(A|B)\)` and the probability of `\(B\)`:

`\[p(A\cap B)= p(A|B) \cdot  p(B).\quad\quad ( * )\]`

### Case `\(p(B)=0\)` 

Because `\(A\cap B\subseteq B\)`, it follows from the probability of included event that 

`\[0\le p(A\cap B)\le p(B)\le 0\]`

Therefore, `\( ( * )\)` trivially holds. 

### Case `\(p(B) > 0\)`

`\( ( * )\)` follows immediately from the formula of [conditional probability][bookofproofs$428].

It remains to be shown that 

`\[p(A\cap B)= p(B|A) \cdot  p(A).\quad\quad ( * * )\]`


Because `\(A\cap B=B\cap A\)`, we have

`\[p(B\cap A)= p(A|B) \cdot  p(B).\]`

For symmetry reasons, we get from `\( ( * )\)`  and `\( ( * * )\)` the required result

`\[p(A\cap B)= p(A|B) \cdot  p(B)=p(B|A) \cdot  p(A).\]`
