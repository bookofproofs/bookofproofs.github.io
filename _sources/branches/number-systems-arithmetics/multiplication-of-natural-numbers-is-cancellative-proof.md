layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1441
orderid: 50
parentid: bookofproofs$1440
title: By Induction
description:  Proof of MULTIPLICATION OF NATURAL NUMBERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: cancellative,left cancellation property,multiplication,natural,numbers,right cancellation property,proof
contributors: bookofproofs

---


---

Because of the counter-example 
`\[2\cdot 0=1\cdot 0\not\Rightarrow 2=1,\]`
the [multiplication of natural numbers][bookofproofs$876] is obviously not cancellative for the natural number `\(0\)`. However, we will prove it for all natural numbers `\(z\in\mathbb N,~z\neq 0\)`. Because the [multiplication of natural numbers][bookofproofs$876]  "`\( \cdot \)`" is [commutative][bookofproofs$1435], it is without loss of generality sufficient to show the right-cancellation property, i.e. `\[x\cdot z=y\cdot z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb N,~z\neq 0).\]`
The proposition can be proven [by induction][bookofproofs$657] of `\(z\ge 1\)`. 

### Base case `\(z=1\)`.

For arbitrary `\(x,y\in\mathbb N\)`, it follows from the [definition of multiplication][bookofproofs$876] and the [definition of addition][bookofproofs$842] that
`\[\begin{array}{rcl}
x\cdot 1 &=&y\cdot 1\\
(x\cdot 0) + x&=&(y\cdot 0)+y\\
x&=&y
\end{array}\]`

### Induction step `\(z\to z^+:=z+1\)`

Now, let assume that the inclusion `\(x\cdot z_0=y\cdot z_0\Rightarrow x=y\)` has been proven for all `\(1\le z_0\le z\)`, where we use "`\(\le\)`" as the [order relation of natural numbers][bookofproofs$697]. Then it follows again from the definition of multiplication of natural numbers that
`\[\begin{array}{rcl}
x\cdot z^+ &=&(x\cdot z)+x,\\
y\cdot z^+ &=&(y\cdot z)+y.
\end{array}\]`

By assumption, if `\(x\cdot z=y\cdot z\)`, then `\(x=y\)`. The right sides of both equations equal each other and it follows
`\[x\cdot z^+=y\cdot z^+\Rightarrow x=y,\]`
which completes the proof that the multiplication of natural numbers is [cancellative][bookofproofs$837].