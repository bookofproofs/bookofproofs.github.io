layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1544
orderid: 50
parentid: bookofproofs$842
title: 
description:  Proof of ADDITION OF NATURAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1538
keywords: addition,addition of natural numbers,natural,numbers,proof
contributors: bookofproofs

---


---

Let `\(n\)` and `\(m\)` be [natural numbers][bookofproofs$718] and let  `\(n^+\)` denote the [successor][bookofproofs$504] of `\(n\)`. We will show that the sum `\(n+m\)` defined recursively by 
`\[\begin{array}{lccl}
1.&n+0&:=&n,\\
2.&n+m^+&:=&(n+m)^+
\end{array}\quad \quad ( * )
\]`
exists and is unique. We will show that there is at most one such sum (step 1) and that there is at least one such sum (step 2), thus there is exactly one such sum.

### Step `\(1:\)` There is at most one possible definition of an addition operation of natural numbers like in `\( ( * ) \)`.

We will show that, for a given `\(n\)`, the definition in  `\( ( * ) \)` is not dependent on the sign of addition. To prove it, we will use two different signs "`\(+\)`" and "`\(\oplus\)`" and check, whether or not they define "different" addition operations:
1.  Assume `\(n+0=n\)` as well as `\(n\oplus 0=n\)`.
1. Assume `\(n+m^+=(n+m)^+\)` as well as `\(n\oplus m^+=(n\oplus m)^+\)`.

Let `\(M\)` be a [subset][bookofproofs$552] of all natural numbers `\(m\)`, for which `\(n + m=n\oplus m\)`. We can conclude that `\(M\)` is not empty, since it (at least) contains the number `\(0\)`. This is because, by first assumption, `\[n+0=n=n\oplus 0.\]` Now, if any number `\(m\)` is contained in `\(M\)`, then, according to the [Peano axiom **P2**][bookofproofs$504], and due to the second assumption, we have
`\[n + m^+=(n+m)^+=(n\oplus m)^+=n\oplus m^+.\]`
This means that with any number `\(m\)` contained in `\(M\)` also its successor `\(m^+\)` is contained in `\(M\)`. Because also `\(0\)` is contained in `\(M\)`, we get by [Peano axiom **P5**][bookofproofs$504], that `\(M\)` contains all natural numbers (principle of induction). This demonstrates, that for a given `\(n\)` and all `\(m\)`, we have
`\[n+m=n\oplus m,\]`
i.e. the sum defined `\( (* )\)` does not depend on the addition sign "`\(+\)`".

### Step `\(2:\)` There is at least one possible definition of an addition operation of natural numbers like in `\( ( * ) \)`.

Let `\(M\)` be a [subset][bookofproofs$552] of all natural numbers `\(n\)`, for which `\(n + m\)` can be defined like in `\( ( * ) \)`. We can conclude that `\(M\)` is not empty, since it (at least) contains the number `\(0\)`. This is because, by `\(1\)` of `\( ( * ) \)`, `\[0+0=0,\]`
 by `\(2\)` of `\( ( * )\)`
 `\[0+m^+=m^+=(0+m)^+.\]`
Now, if any number `\(n\)` is contained in `\(M\)`, then according to the [Peano axiom **P2**][bookofproofs$504], we have
`\[\begin{array}{lccl}
1.&n^++0&:=&n^+,\\
2.&n^++m^+&:=&(n^++m)^+
\end{array}
\]`
This means that with any number `\(n\)` contained in `\(M\)` also its successor `\(n^+\)` is contained in `\(M\)`. Because also `\(0\)` is contained in `\(M\)`, we get by [Peano axiom **P5**][bookofproofs$504], that `\(M\)` contains all natural numbers (principle of induction). This demonstrates, that there is at least one possible definition of an addition operation of natural numbers like in `\( ( * ) \)`.

Altogether, steps `\(1\)` and `\(2\)` show that there is exactly one possible definition of addition operation, or that for any two natural numbers `\(n\)` and `\(m\)`, their sum `\(n+m\)` exists and is unique.
