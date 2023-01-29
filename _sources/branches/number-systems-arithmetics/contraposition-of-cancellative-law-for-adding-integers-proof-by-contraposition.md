layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1562
orderid: 50
parentid: bookofproofs$1561
title: 
description: PROOF BY CONTRAPOSITION Proof of CONTRAPOSITION OF CANCELLATIVE LAW FOR ADDING INTEGERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1538
keywords: adding,cancellative,contraposition,integers,law,proof
contributors: bookofproofs

---


---

According to the [cancellation law for adding integers][bookofproofs$1462], we have
 for all [integers][bookofproofs$718] `\(x,y,z\in\mathbb Z\)`:
`\[\begin{array}{rcl}z + x=z + y&\Longleftrightarrow &x=y,\\
x + z=y + z&\Longleftrightarrow& x=y.
\end{array}\]`
By virtue of the [proving principle by contraposition][bookofproofs$1330], it follows
`\[x \neq y\Longleftrightarrow \begin{cases} z + x\neq z + y,&\text{or}\\
x + z\neq y + z,
\end{cases}\]`

i.e. if any two integers `\(x\)` and `\(y\)` are [unequal][bookofproofs$1539], then the inequality is preserved if we add an arbitrary integer `\(z\)` to both sides of the inequality. Conversely, given an inequality, in which the same integer `\(z\)` is added on both sides, we can "cancel it out" and preserve the inequality.
