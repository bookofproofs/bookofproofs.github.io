layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1433
orderid: 50
parentid: bookofproofs$1432
title: By Induction
description:  Proof of ADDITION OF NATURAL NUMBERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,cancellative,left cancellation property,natural,numbers,right cancellation property,proof
contributors: bookofproofs

---


---

Because the [addition of natural numbers][bookofproofs$842] "`\( + \)`" is [commutative][bookofproofs$1430], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x+z=y+z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb N).\]`
The proposition can be proven [by induction][bookofproofs$657].
### Base case Base case `\(z=0\)`.

For arbitrary `\(x,y\in\mathbb N\)`, it follows from the [definition of addition][bookofproofs$842] that
`\[x+0=y+0\Rightarrow x=y.\]`

Note that `\(x+0=x\)` and `\(y+0=y\)` are both [equalities being equivalence relations][bookofproofs$1539]. Thus, we can replace the implication sign "`\(\Rightarrow\)`" by the equivalence sign "`\(\Leftrightarrow\)`", and the reasoning is still logically correct:

`\[x+0=y+0\Leftrightarrow x=y.\]`



### Induction step `\(z\to z^+:= z+1\)`.

Now, let assume that the inclusion `\(x+a_0=y+a_0\Leftrightarrow  x=y\)` has been proven for all `\(z_0\le z\)`, where we use "`\(\le\)`" as the [order relation of natural numbers][bookofproofs$719]. Then it follows again from the definition of addition that
`\[x+z^+=y+z^+\Leftrightarrow (x+z)^+=(y+z)^+.\]`
Because both successors are unique and because `\(x+z=y+z\)` is equivalent to `\(x=y\)` by assumption, it follows that 
`\[(x+z)^+=(y+z)^+\Leftrightarrow x=y.\]`
Altogether, it follows from `\(x + z=y + z\)` that `\(x=y\)` for all natural numbers `\(x,y,z\)`. Thus, the addition of natural numbers is [cancellative][bookofproofs$837].
`\[ x+z=y+z \Rightarrow x=y,\]`

and we have proven the conversion of the cancellative law:

`\[ x=y\Rightarrow x+z=y+z\]`

for all natural numbers `\(x,y,z\)`.
