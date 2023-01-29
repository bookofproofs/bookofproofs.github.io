layout: explanation
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1825
orderid: 50
parentid: bookofproofs$1809
title: Mutually Exclusive vs. Pairwise Independent Events
description: MUTUALLY EXCLUSIVE VS. PAIRWISE INDEPENDENT EVENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$856
keywords: events,exclusive,independent,mutually,pairwise
contributors: bookofproofs

---


---

[Mutually exclusive events][bookofproofs$859] cannot be [pairwise independent][bookofproofs$1809], i.e. from 

`\[A_i\cap A_j=\emptyset\]`

it does not (!) follow

`\[0=p(A_i\cap A_j)=p(A_i)\cdot p(A_j),\quad\quad( * )\]`

for all

`\[A_i,A_j\subseteq\Omega, i\neq j.\]`

In particular, at least one of the probabilities in would have to be `\(0\)` to fulfill `\( ( * ) \)`, i.e. it would be the [impossible event][bookofproofs$862]. In other words, e.g. if we assume `\(p(A_i) > 0\)`, then the event `\(A_i\)` can occur. But then `\(p(A_j)\)` drops to `\(0\)`. Thus, `\(A_j\)` cannot occur, if `\(A_i\)` can, and vice versa. Therefore, both events are not independent (i.e. their occurrence influences each other).
