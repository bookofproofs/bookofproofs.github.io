layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1546
orderid: 50
parentid: bookofproofs$1545
title: 
description: PROOF BY CONTRAPOSITION Proof of CONTRAPOSITION OF CANCELLATIVE LAW FOR ADDING NATURAL NUMBERS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1538
keywords: adding,cancellative,contraposition,law,natural,numbers,proof
contributors: bookofproofs

---


---

According to the [cancellation law for adding  natural numbers][bookofproofs$1432], we have
 for all [natural numbers][bookofproofs$718] `\(x,y,z\in\mathbb N\)`:
`\[\begin{array}{rcl}z + x=z + y&\Longleftrightarrow &x=y,\\
x + z=y + z&\Longleftrightarrow& x=y.
\end{array}\]`
By virtue of the [proving principle by contraposition][bookofproofs$1330], it follows:
`\[x \neq y\Longleftrightarrow \begin{cases} z + x\neq z + y,&\text{or}\\
x + z\neq y + z,
\end{cases}\]`

i.e. if any two natural numbers `\(x\)` and `\(y\)` are [unequal][bookofproofs$1539], then the inequality is preserved if we add an arbitrary natural number `\(z\)` to both sides of the inequality. Conversely, given an inequality, in which the same natural number `\(z\)` is added on both sides, we can "cancel it out" and preserve the inequality.
