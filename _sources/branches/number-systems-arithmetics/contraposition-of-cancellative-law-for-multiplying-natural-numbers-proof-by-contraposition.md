layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1560
orderid: 50
parentid: bookofproofs$1559
title: 
description: PROOF BY CONTRAPOSITION Proof of CONTRAPOSITION OF CANCELLATIVE LAW FOR MULTIPLYING NATURAL NUMBERS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1538
keywords: cancellative,contraposition,law,multiplying,natural,numbers,proof
contributors: bookofproofs

---


---

According to the [cancellation law for multiplying natural numbers][bookofproofs$1440], we have for all [natural numbers][bookofproofs$718] `\(x,y,z\in\mathbb N\)` with `\(z\neq 0\)`

`\[\begin{array}{rcl}z \cdot x=z \cdot y&\Longleftrightarrow &x=y,\\
x \cdot z=y \cdot z&\Longleftrightarrow& x=y.
\end{array}\]`
By virtue of the [proving principle by contraposition][bookofproofs$1330], it follows
`\[x \neq y\Longleftrightarrow \begin{cases} z \cdot x\neq z \cdot y,&\text{or}\\
x \cdot z\neq y \cdot z,
\end{cases}\]`

i.e. if any two natural numbers `\(x\)` and `\(y\)` are [unequal][bookofproofs$1539], then the inequality is preserved, if we multiply both sides of the inequality by an arbitrary natural number `\(z\neq 0\)`. Conversely, if we have an inequality, in which both sides are multiplied by the same natural number `\(z\neq 0\)`, then we can "cancel it out", and still preserve the inequality.
