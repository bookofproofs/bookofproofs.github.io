layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1577
orderid: 50
parentid: bookofproofs$1575
title: 
description:  Proof of MULTIPLICATION OF REAL NUMBERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: cancellative,left cancellation property,multiplication,numbers,real,right cancellation property,proof
contributors: bookofproofs

---


---

Because the [multiplication of real numbers is commutative][bookofproofs$1532], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x\cdot z=y\cdot z\Leftrightarrow x=y,~~~~~~(x,y,z\in\mathbb R,~z\neq 0).\]`

By [definition of real numbers][bookofproofs$1105], the numbers `\(x,y,z\)` are some equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N}+I,\\y&:=&(y_n)_{n\in\mathbb N}+I,\\z&:=&(z_n)_{n\in\mathbb N}+I\\\end{array}\]`

for some rational Cauchy sequences `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which [converge to][bookofproofs$1572] `\(0\)`. Moreover, since `\(z\neq 0\)` by hypothesis, the rational Cauchy sequence  `\((z_n)_{n\in\mathbb N}\)` is not convergent to 0, i.e. `\((z_n)_{n\in\mathbb N}\not\in I\)`.

By [definition of multiplying real numbers][bookofproofs$1532], we have 
`\[\begin{array}{rcl}
x\cdot z&=&(x_n\cdot z_n)_{n\in\mathbb N}+I,\\
y\cdot z&=&(y_n\cdot z_n)_{n\in\mathbb N}+I.
\end{array}\]`

By hypothesis, `\((z_n)_{n\in\mathbb N}\not\in I\)`. Therefore, there exist `\(N\in\mathbb N\)` such that `\(|z_n|>0\)` for all `\(n > N\)`. For such indices it follows from the [cancellation property of multiplying rational Cauchy sequences][bookofproofs$1569] that

`\[\begin{array}{rcll}
x\cdot z=y\cdot z&\Leftrightarrow&(x_n\cdot z_n)_{n > N}+I=(y_n\cdot z_n)_{n > N}+I&\text{by definition of multiplying real numbers}\\
&\Leftrightarrow& (x_n)_{n >  N}+I=(y_n)_{n >  N}+I&\text{because multiplication of rational Cauchy sequences is cancellative}\\
&\Leftrightarrow& x=y&\text{by definition of real numbers}
\end{array}
\]`

Altogether, we have shown that the addition of real numbers is [cancellative][bookofproofs$837] `\[ x\cdot z=y\cdot z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb R,~z\neq 0),\]`
and its conversion
`\[x=y\Rightarrow x\cdot z=y\cdot z,~~~~~~(x,y,z\in\mathbb R,~z\neq 0).\]`
