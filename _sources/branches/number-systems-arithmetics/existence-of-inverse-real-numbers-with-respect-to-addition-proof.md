layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1587
orderid: 50
parentid: bookofproofs$35
title: 
description:  Proof of EXISTENCE OF INVERSE REAL NUMBERS WITH RESPECT TO ADDITION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,existence,inverse,numbers,real,respect,proof
contributors: bookofproofs

---


---

Let `\(x=(x_n)_{n\in\mathbb N}+I\)` be a real number. Because there [exists an inverse rational Cauchy sequence][bookofproofs$1508] `\((-x_n)_{n\in\mathbb N}\)`, such that 

`\[(x_n)_{n\in\mathbb N}+(-x_n)_{n\in\mathbb N}=(0)_{n\in\mathbb N},\]`

there exists the real number  `\(-x:=(-x_n)_{n\in\mathbb N}+I\)`. From the definition of [adding real numbers][bookofproofs$1514], we get

`\[\begin{array}{rcll}
x+(-x)&=&((x_n)_{n\in\mathbb N}+I) + ((-x_n)_{n\in\mathbb N}+I)&\text{by definition of real numbers}\\
&=&(x_n+(-x_n))_{n\in\mathbb N}+I&\text{by definition of adding real numbers}\\
&=&(0)_{n\in\mathbb N}+I&\text{by existence of inverse rational Cauchy sequences with respect to addition}\\
&=&0&\text{by existence of real zero}
\end{array}\]`

where `\(0\)` denotes the [real zero][bookofproofs$34], as required.
