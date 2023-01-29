layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1582
orderid: 50
parentid: bookofproofs$520
title: 
description:  Proof of DISTRIBUTIVITY LAW FOR REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$696
keywords: real number,real numbers,proof,proof
contributors: bookofproofs

---


---

Because the [multiplication of real numbers is commutative][bookofproofs$1532], it is without loss of generality sufficient to show the left-distributivity law
`\[x\cdot(y+z)=(x\cdot y)+(x\cdot z).\]`

By [definition of real numbers][bookofproofs$1105], the numbers `\(x,y,z\)` are some  equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N}+I,\\y&:=&(y_n)_{n\in\mathbb N}+I,\\z&:=&(z_n)_{n\in\mathbb N}+I,\\\end{array}\]`

in which `\((x_n)_{n\in\mathbb N}\)`, `\((y_n)_{n\in\mathbb N}\)`, and `\((z_n)_{n\in\mathbb N}\)` denote rational Cauchy sequences, which represent the real numbers `\(x\)` and `\(y\)` and `\(x\)`, while `\(I\)` denotes the set of all rational sequences, which [converge to][bookofproofs$1572] `\(0\)`. 


The left-distributivity law can be proven using the following mathematical definitions and concepts:
* [definition of adding real numbers][bookofproofs$1514],
* [definition of multiplying real numbers][bookofproofs$1532],
* [distributivity law for rational numbers][bookofproofs$1491].
The proof follows:

`\[\begin{array}{ccll}
x\cdot(y+z)&=&((x_n)_{n\in\mathbb N} + I)\cdot[((y_n)_{n\in\mathbb N} + I) + ((z_n)_{n\in\mathbb N} + I)]&\text{by definition of real numbers}\\
&=&((x_n)_{n\in\mathbb N} + I)\cdot((y_n + z_n)_{n\in\mathbb N} + I)&\text{by definition of adding real numbers}\\
&=&(x_n\cdot(y_n + z_n))_{n\in\mathbb N} + I&\text{by definition of multiplying real numbers}\\
&=&((x_n \cdot y_n) + (x_n \cdot z_n))_{n\in\mathbb N} + I&\text{by distributivity law for multiplying rational numbers}\\
&=&[(x_n \cdot y_n)_{n\in\mathbb N} + I] + [(x_n \cdot z_n))_{n\in\mathbb N} + I]&\text{by definition of adding real numbers}\\
&=&[((x_n)_{n\in\mathbb N} + I) \cdot ((y_n)_{n\in\mathbb N} + I)] + [((x_n)_{n\in\mathbb N} + I) \cdot ((z_n)_{n\in\mathbb N} + I)]&\text{by definition of multiplying real numbers}\\
&=&(x\cdot y)+(x\cdot z)&\text{by definition of real numbers}\\
\end{array}\]`
