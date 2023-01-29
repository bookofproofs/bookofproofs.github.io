layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3245
orderid: 50
parentid: bookofproofs$6196
title: 1620 BC
description:  Proof of SUM OF EULER FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: euler,function,sum,proof
contributors: bookofproofs

---


---

* Let `$n\ge 1$` be a [natural number][bookofproofs$718].
* If we calculated for all numbers `$k=1,2,\ldots, n,$` the [greatest common divisor][bookofproofs$1280] `$d_k=\gcd(k,n)$`, then the relation `$k\sim l:=d_k=d_l$` is an [equivalence relation][bookofproofs$574] and we can group all these numbers by those having the same greatest common divisor `$d_k.$`  
* For each [equivalence class][bookofproofs$7990] `$d_k$`, we have by the [proposition][bookofproofs$1289] and the [proposition][bookofproofs$1291] that `$k\perp\frac{n}{d_k}$` ([co-prime][bookofproofs$8093]) and `$0 < k\cdot d_k\le n.$`
* From this, it follows that the count of numbers `$k$` being co-prime to `$\frac{n}{d_k}$` with `$0 < k\le\frac{n}{d_k}$` is exactly equal the [Euler function][bookofproofs$8117] `$\phi\left(\frac{n}{d_k}\right),$` by definition.
* Because all classes `$d_k$` are disjoint, we can sum up all counts and get `$$\sum_{d_k\mid n}\phi\left(\frac{n}{d_k}\right)=n.$$`
* Note that with `$\frac{n}{d_k}$` also the [complementary divisor][bookofproofs$700] `$d_k$` takes all possible values. 
* Therefore, we get the required result
`$$\sum_{d_k\mid n}\phi(d_k)=\sum_{d\mid n}\phi(d)=n.$$`
