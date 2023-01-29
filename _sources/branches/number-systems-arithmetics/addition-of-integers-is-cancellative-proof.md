layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1463
orderid: 50
parentid: bookofproofs$1462
title: 
description:  Proof of ADDITION OF INTEGERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,cancellative,integers,left cancellation property,right cancellation property,proof
contributors: bookofproofs

---


---

Because the [addition of integers is commutative][bookofproofs$1460], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x+z=y+z\Leftrightarrow x=y,~~~~~~(x,y,z\in\mathbb Z).\]`

By [definition of integers][bookofproofs$844], the integer numbers `\(x,y,z\)` are some equivalence classes of ordered pairs of natural numbers represented by some natural numbers `\(a,b,c,d,e,f\in\mathbb N\)`

`\[\begin{array}{rcl}x&:=&[a,b],\\y&:=&[c,d],\\z&:=&[e,f]\\\end{array}\]`

By [definition of adding integers][bookofproofs$890], we have 
`\[\begin{array}{rcl}
x+z&=&[a+e,b+f],\\
y+z&=&[c+e,d+f].
\end{array}\]`

Because the [addition of natural numbers is cancellative][bookofproofs$1432], it follows
`\[\begin{array}{rcll}
x+z=y+z&\Leftrightarrow& [a+e,b+f]=[c+e,d+f]&\text{by definition of adding integers}\\
&\Leftrightarrow& [a,b]=[c,d]&\text{because addition of natural numbers is cancellative}\\
&\Leftrightarrow& x=y&\text{by definition of integers}
\end{array}
\]`

Altogether, we have shown that the addition of integers is [cancellative][bookofproofs$837] `\[ x+z=y+z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb Z),\]`
and its conversion
`\[x=y\Rightarrow x+z=y+z,~~~~~~(x,y,z\in\mathbb Z).\]`
