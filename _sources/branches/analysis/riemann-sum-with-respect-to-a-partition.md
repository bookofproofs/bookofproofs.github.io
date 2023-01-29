layout: definition
categories: branches,analysis
nodeid: bookofproofs$1781
orderid: 300
parentid: bookofproofs$474
title: Riemann Sum With Respect to a Partition
description: RIEMANN SUM WITH RESPECT TO A PARTITION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: partition,respect,riemann,riemann sum,sum
contributors: bookofproofs

---


---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153], `\(f:[a,b]\mapsto\mathbb R\)` be a  [bounded real function][bookofproofs$302], and `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)` be a partition of the interval `\([a,b]\)`. Further, let `\(\xi\in[x_{k-1},x_k]\)` (i.e. `\(\xi\)` is any point in the interval `\([x_{k-1},x_k]\)`, `\(1\le k\le n\)`). We call 

`\[\sum_{k=1}^n f(\xi_k)(x_k-x_{k-1})\]`

a **Riemann sum** of `\(f\)` with respect to the partition   `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`. 

Please note that we can have different Riemann sums of `\(f\)` with respect to the same partition, since the choice of the supporting points `\(\xi_k\)` is arbitrary in each interval  `\([x_{k-1},x_k]\)`.

The *mesh `\(\mu\)` of the partition*    `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)` is defined as the maximum length of a single partition interval

 `\[\mu:=\max_{1\le k\le n}(x_k-x_{k-1}).\]`
