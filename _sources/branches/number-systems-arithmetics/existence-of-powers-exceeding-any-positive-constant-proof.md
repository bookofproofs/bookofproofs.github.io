layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1349
orderid: 50
parentid: bookofproofs$1348
title: 
description:  Proof of EXISTENCE OF POWERS EXCEEDING ANY POSITIVE CONSTANT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: any,constant,exceeding,existence,positive,powers,proof
contributors: bookofproofs

---


---

Let `\(b > 1\)` be a [real number][bookofproofs$1105] and let `\(C > 0\)` be a constant. We want to show that there exists a natural number `\(n\)`, for which `\(b^n > C\)`. 

Set `\(x:= b~- 1\)`. Since `\(x > 0\)`, we can use [Bernoulli's inequality][bookofproofs$590] and conclude that

`\[b^n=(1+x)^n \ge 1 + nx\]`

for all `\(n\ge 2\)`. Together with the [Archimedean axiom][bookofproofs$1339], it follows that there exists a [natural number][bookofproofs$718] `\(n\in\mathbb N\)` with `\[nx > C - 1.\]`
Combining both inequalities, we get for this `\(n\)` that `\(b^n > C\)`.
