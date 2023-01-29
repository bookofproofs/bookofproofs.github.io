layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1527
orderid: 50
parentid: bookofproofs$31
title: 
description:  Proof of ADDITION OF REAL NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,associative,numbers,real,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers, which by definition means ][bookofproofs$1105] that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\\z&:=&(z_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`.

The associativity of the [addition of real numbers][bookofproofs$1514] `\((x+y)+z=x+(y+z)\)` for all `\(x,y,z\in\mathbb R\)` follows from the [associativity of adding rational Cauchy sequences][bookofproofs$1494]. For all rational Cauchy sequences `\((x_n)_{n\in\mathbb N}, (y_n)_{n\in\mathbb N}, (z_n)_{n\in\mathbb N}\in M\)` we have
`\[\begin{array}{rcll}
(x+y)+z&=&[((x_n)_{n\in\mathbb N}+ I)+((y_n)_{n\in\mathbb N}+ I)]+((z_n)_{n\in\mathbb N}+I)&\text{by definition of real numbers}\\
&=&[((x_n)_{n\in\mathbb N}+ (y_n)_{n\in\mathbb N})+ I]+((z_n)_{n\in\mathbb N}+I)&\text{by definition of adding real numbers}\\
&=&[((x_n)_{n\in\mathbb N}+ (y_n)_{n\in\mathbb N})+ (z_n)_{n\in\mathbb N}+I]&\text{by definition of adding real numbers}\\
&=&[(x_n)_{n\in\mathbb N}+ ((y_n)_{n\in\mathbb N}+ (z_n)_{n\in\mathbb N})+I]&\text{by associativity of adding rational Cauchy sequences}\\
&=&((x_n)_{n\in\mathbb N}+ I) + [(y_n)_{n\in\mathbb N})+ (z_n)_{n\in\mathbb N}+I]&\text{by definition of adding real numbers}\\
&=&((x_n)_{n\in\mathbb N}+ I) + [((y_n)_{n\in\mathbb N})+ I) +((z_n)_{n\in\mathbb N}+I)]&\text{by definition of adding real numbers}\\
&=&x+(y+z)&\text{by definition of real numbers}\\
\end{array}\]`
