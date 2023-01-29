layout: proof
categories: branches,topology
nodeid: bookofproofs$1255
orderid: 50
parentid: bookofproofs$1254
title: 
description: PROOF OF \\EPSILON\-\\DELTA\ DEFINITION OF CONTINUITY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: continuity,definition,delta,epsilon,epsilon delta definition of continuity,epsilon delta continuity,delta epsilon definition of continuity,definition of continuity epsilon delta,continuity epsilon delta,epsilon-delta definition of continuity,epsilon delta definition,epsilon delta definition of continuous function,epsilon delta definition continuity
contributors: bookofproofs

---


---

We have to show that for two given [metric spaces][bookofproofs$617] `\((X,d_x)\)` and `\((Y,d_y)\)` and a [function][bookofproofs$592] `\(f:X\to Y\)` the definition of [continuity of `\(f\)` at a point `\(a\in X\)` ][bookofproofs$1205] is equivalent to the `\(\epsilon\)`-`\(\delta\)` definition of continuity.

### "`\(\Rightarrow\)`"

Let `\(f\)` be continuous at `\(a\)`, which, according to first definition means that `\(\lim_{x\to a} f(x)=f(a)\)`. Assume, the `\(\epsilon\)`-`\(\delta\)` condition was not fulfilled. Then there would be an `\(\epsilon > 0\)` such that for every `\(\delta > 0\)` we would find a point `\(x\in X\)` such that

`\[d_x(x,a) < \delta\]`
but  
`\[d_y(f(x),f(a)) \ge \epsilon.\]`

In particular, for a `\(\delta:=\frac 1n\)` we would have a sequence of points `\(x_n\in X\)` such that 
`\[d_x(x_n,a) < \frac 1n\quad\wedge\quad d_y(f(x_n),f(a)) \ge \epsilon\quad\quad ( * ) \]`

However, the left inequation means that `\(\lim x_n=a\)` and so `\(\lim f(x_n)=f(a)\)`, in [contradiction][bookofproofs$744] to  `\(( * )\)`. Therefore, it must be that the `\(\epsilon\)`-`\(\delta\)` condition is fulfilled. 

### "`\(\Leftarrow\)`"

Let `\((x_n)_{n\in\mathbb N}\)` be a sequence of points with `\(\lim x_n=a\)`. We have to show that  `\(\lim f(x_n)=f(a)\)`, when the `\(\epsilon\)`-`\(\delta\)` condition be fulfilled.

From `\(\lim x_n=a\)` it follows that for every (arbitrarily small,) given `\(\delta > 0\)` there exists `\(N(\delta)\in\mathbb N\)` such that `\(d_x(x_n,a) < \delta\)` for all `\(n \ge N(\delta)\)`. Now, since the `\(\epsilon\)`-`\(\delta\)` condition is fulfilled, we have that for every given `\(\epsilon > 0\)` there is a `\(\delta > 0\)` such that from `\[d_x(x_n,a) < \delta.\]`
it follows that 
`\[d_y(f(x_n),f(a)) < \epsilon.\]` 
Because this is true for all  `\(n \ge N(\epsilon):=N(\delta)\)`, it is equivalent to `\(\lim f(x_n)=f(a)\)`.
