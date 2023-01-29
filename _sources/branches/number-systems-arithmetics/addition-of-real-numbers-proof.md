layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1526
orderid: 50
parentid: bookofproofs$1514
title: 
description:  Proof of ADDITION OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: real number,real numbers,proof,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers, which by definition means ][bookofproofs$1105] that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all [rational Cauchy sequences][bookofproofs$1485], which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`. 
Note that according [definition of adding rational Cauchy sequences][bookofproofs$1486], the sum `\((x_n+y_n)_{n\in\mathbb N}\)` exists and is a rational Cauchy sequence. Therefore, `\((x_n+y_n)_{n\in\mathbb N}+I\)` exists and is a real number. It remains to be shown that the addition of real numbers 
`\[\begin{array}{rcccl}
x+y&:=&(x_n+y_n)_{n\in\mathbb N}+ I
\end{array}\]`
is well-defined, i.e. it does not depend on the particular choice of the representatives `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)`. 

Let `\((x_n)_{n\in\mathbb N},(x_n^\prime)_{n\in\mathbb N}\)` as two different representatives of the real number `\(x\)` and let `\((y_n)_{n\in\mathbb N},(y_n^\prime)_{n\in\mathbb N}\)` be two different representatives of the real number `\(y\)`. In order to show that the addition of real numbers does not depend on the representatives, we have to prove that
`\[x+y=(x_n^\prime+y_n^\prime)_{n\in\mathbb N}+ I=(x_n+y_n)_{n\in\mathbb N}+ I.\]` 

We first observe that `\((M, + )\)` is a [commutative group, which has been shown already][bookofproofs$1518]. Moreover, we have seen that `\((I, + )\)` [is its subgroup][bookofproofs$1522]. Note that `\((x_n)_{n\in\mathbb N} + I\)` and `\((y_n)_{n\in\mathbb N} + I\)` are [left cosets][bookofproofs$827] of `\(I\)`, which means that the real numbers `\(x\)` and `\(y\)` are in fact sets with different elements (albeit we usually interpret them as "numbers"). 

From `\((x_n^\prime)_{n\in\mathbb N}\in (x_n)_{n\in\mathbb N} + I\)` it follows that there exists `\((a_n)_{n\in\mathbb N}\in I\)` (i.e. a rational sequence convergent to `\(0\)`)  with `\((x_n^\prime)_{n\in\mathbb N}=(x_n + a_n)_{n\in\mathbb N}\)`.
Analogously, from `\((y_n^\prime)_{n\in\mathbb N}\in (y_n)_{n\in\mathbb N} + I\)` it follows that there exists a `\((b_n)_{n\in\mathbb N}\in I\)` (i.e. another rational sequence convergent to `\(0\)`) with `\((y_n^\prime)_{n\in\mathbb N}=(y_n + b_n)_{n\in\mathbb N}\)`.

Using the [definition of adding rational Cauchy sequences][bookofproofs$1486], the [associativity law for adding rational Cauchy sequences][bookofproofs$1494], and the [associativity law for adding rational numbers][bookofproofs$1447] we get:
`\[\begin{array}{rcll}
x+y=(x_n^\prime+y_n^\prime)_{n\in\mathbb N}+ I&=&(x_n+a_n)_{n\in\mathbb N}+(y_n+b_n)_{n\in\mathbb N}+ I&\text{because }x\text{ and }y\text{ are left cosets of }I\\
&=&((x_n+a_n)+(y_n+b_n))_{n\in\mathbb N}+ I&\text{by definition of adding rational Cauchy sequences}\\
&=&((x_n+a_n+y_n)+b_n)_{n\in\mathbb N}+ I&\text{by associativity of adding rational numbers}\\
&=&(x_n+a_n+y_n)_{n\in\mathbb N}+(b_n)_{n\in\mathbb N}+ I&\text{by definition of adding rational Cauchy sequences}\\
&=&(x_n+a_n+y_n)_{n\in\mathbb N}+I&\text{because }(b_n)_{n\in\mathbb N}\in I\\
&=&(x_n+(a_n+y_n))_{n\in\mathbb N}+I&\text{by associativity law for adding rational numbers}\\
\end{array}\]` 
Note that, since `\((M, + )\)` is commutative, so is `\((I, + )\)`. Thus, `\(I\)` is a [normal subgroup][bookofproofs$273] of `\(M\)`. Therefore, there for the rational sequence `\((a_n)_{n\in\mathbb N}\in I\)` convergent to `\(0\)` it holds that `\((a_n+y_n)_{n\in\mathbb N}=(y_n+a_n)_{n\in\mathbb N}\)`. We can now continue our calculation by replacing 
`\[\begin{array}{rcll}
(x_n+(a_n+y_n))_{n\in\mathbb N}+I&=&(x_n+(y_n+a_n))_{n\in\mathbb N}+I&\text{because }I\text{ is a normal subgroup of }M\\
&=&((x_n+y_n)+a_n)_{n\in\mathbb N}+I&\text{by associativity law for adding rational numbers}\\
&=&(x_n+y_n)_{n\in\mathbb N}+(a_n)_{n\in\mathbb N}+I&\text{by definition of adding rational Cauchy sequences}\\
&=&(x_n+y_n)_{n\in\mathbb N}+I&\text{because }(a_n)_{n\in\mathbb N}\in I\\
\end{array}\]` 

This demonstrates that the addition of real numbers "`\(+\)`" is well-defined, since it does not depend on the particular choice of their representatives `\((x_n)_{n\in\mathbb N},(y_n)_{n\in\mathbb N}\in M\)` or `\((x_n^\prime)_{n\in\mathbb N},(y_n^\prime)_{n\in\mathbb N}\in M\)`.
