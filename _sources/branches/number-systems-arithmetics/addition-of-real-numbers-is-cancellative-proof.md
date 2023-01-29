layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1576
orderid: 50
parentid: bookofproofs$1574
title: 
description:  Proof of ADDITION OF REAL NUMBERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: addition,cancellative,left cancellation property,numbers,real,right cancellation property,proof
contributors: bookofproofs

---


---

Because the [addition of real numbers is commutative][bookofproofs$33], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x+z=y+z\Leftrightarrow x=y,~~~~~~(x,y,z\in\mathbb R).\]`

By [definition of real numbers][bookofproofs$1105], the numbers `\(x,y,z\)` are some equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N}+I,\\y&:=&(y_n)_{n\in\mathbb N}+I,\\z&:=&(z_n)_{n\in\mathbb N}+I\\\end{array}\]`

for some rational Cauchy sequences `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`.

By [definition of adding real numbers][bookofproofs$1514], we have 
`\[\begin{array}{rcl}
x+z&=&(x_n+z_n)_{n\in\mathbb N}+I,\\
y+z&=&(y_n+z_n)_{n\in\mathbb N}+I.
\end{array}\]`

Because the [addition of rational Cauchy sequences is cancellative][bookofproofs$1569], it follows
`\[\begin{array}{rcll}
x+z=y+z&\Leftrightarrow&(x_n+z_n)_{n\in\mathbb N}+I=(y_n+z_n)_{n\in\mathbb N}+I&\text{by definition of adding real numbers}\\
&\Leftrightarrow& (x_n)_{n\in\mathbb N}+I=(y_n)_{n\in\mathbb N}+I&\text{because addition of rational Cauchy sequences is cancellative}\\
&\Leftrightarrow& x=y&\text{by definition of real numbers}
\end{array}
\]`

Altogether, we have shown that the addition of real numbers is [cancellative][bookofproofs$837] `\[ x+z=y+z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb R),\]`
and its conversion
`\[x=y\Rightarrow x+z=y+z,~~~~~~(x,y,z\in\mathbb R).\]`
