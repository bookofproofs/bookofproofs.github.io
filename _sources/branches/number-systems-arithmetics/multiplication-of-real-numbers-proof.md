layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1533
orderid: 50
parentid: bookofproofs$1532
title: 
description:  Proof of MULTIPLICATION OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: real number,real numbers,proof,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [real numbers, which by definition means ][bookofproofs$1105] that they are the equivalence classes `\[\begin{array}{rcl}x&:=&(x_n)_{n\in\mathbb N} + I,\\
y&:=&(y_n)_{n\in\mathbb N} + I.\end{array}\]`
In the above definition, `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)` denote elements of the set `\(M\)` of all [rational Cauchy sequences][bookofproofs$1485], which represent the real numbers `\(x\)` and `\(y\)`, while `\(I\)` denotes the set of all rational sequences, which converge to `\(0\)`. 

Note that according [definition of multiplying rational Cauchy sequences][bookofproofs$1488], the product `\((x_n\cdot y_n)_{n\in\mathbb N}\)` exists and is a rational Cauchy sequence. Therefore, the product `\((x_n\cdot y_n)_{n\in\mathbb N}+I\)` exists and is a real number. It remains to be shown that the multiplication of real numbers 
`\[\begin{array}{rcccl}
x\cdot y&:=&(x_n\cdot y_n)_{n\in\mathbb N}+ I
\end{array}\]`
is well-defined, i.e. it does not depend on the particular choice of the representatives `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)`. 


Let `\((x_n)_{n\in\mathbb N},(x_n^\prime)_{n\in\mathbb N}\)` as two different representatives of the real number `\(x\)` and let `\((y_n)_{n\in\mathbb N},(y_n^\prime)_{n\in\mathbb N}\)` be two different representatives of the real number `\(y\)`. In order to show that the multiplication of real numbers does not depend on the representatives, we have to prove that
`\[x\cdot y=(x_n^\prime\cdot y_n^\prime)_{n\in\mathbb N}+ I=(x_n\cdot y_n)_{n\in\mathbb N}+ I.\]` 

We have seen that `\((I, + )\)` [is the subgroup of the group][bookofproofs$1522] `\((M, + )\)`. Therefore `\((x_n)_{n\in\mathbb N} + I\)` and `\((y_n)_{n\in\mathbb N} + I\)` are [left cosets][bookofproofs$827] of `\(I\)`, which means that the real numbers `\(x\)` and `\(y\)` are in fact sets with different elements (albeit we usually interpret them as "numbers"). 

From `\((x_n^\prime)_{n\in\mathbb N}\in (x_n)_{n\in\mathbb N} + I\)` it follows that there exists `\((a_n)_{n\in\mathbb N}\in I\)` (i.e. a rational sequence convergent to `\(0\)`)  with `\((x_n^\prime)_{n\in\mathbb N}=(x_n + a_n)_{n\in\mathbb N}\)`.
Analogously, from `\((y_n^\prime)_{n\in\mathbb N}\in (y_n)_{n\in\mathbb N} + I\)` it follows that there exists a `\((b_n)_{n\in\mathbb N}\in I\)` (i.e. another rational sequence convergent to `\(0\)`) with `\((y_n^\prime)_{n\in\mathbb N}=(y_n + b_n)_{n\in\mathbb N}\)`.

In the following, we will use the following mathematical definitions and concepts:
* [definition of real numbers][bookofproofs$1105],
* [definition of multiplying real numbers][bookofproofs$1532] (hypothesis),
* `\(I\)` is an [ideal of the commutative unit ring][bookofproofs$1524] `\((M, \cdot, + )\)`, 
* [distributivity law for rational Cauchy sequences][bookofproofs$1506], and
* [associativity law for adding rational Cauchy sequences][bookofproofs$1494]:

We first observe that  which has been shown already. In particular, w

`\[\begin{array}{rcll}
x\cdot y&=&((x_n^\prime)_{n\in\mathbb N} + I)\cdot ((y_n^\prime)_{n\in\mathbb N} + I)&\text{by definition of real numbers}\\
&=&(x_n^\prime\cdot y_n^\prime)_{n\in\mathbb N}) + I&\text{by hypothesis}\\
&=&((x_n + a_n)_{n\in\mathbb N}\cdot(y_n + b_n)_{n\in\mathbb N})+ I&\text{according to }(*)\\
&=&((x_n\cdot y_n + x_n\cdot b_n+ a_n\cdot y_n+a_n\cdot b_n)_{n\in\mathbb N}+I&\text{by distributivity law for rational Cauchy sequences}\\
&=&((x_n\cdot y_n + (x_n\cdot b_n+ a_n\cdot y_n+a_n\cdot b_n))_{n\in\mathbb N}+I&\text{by associativity of adding rational Cauchy sequences}\\
&=&((x_n\cdot y_n)_{n\in\mathbb N}+I&\text{because }I\text{ is an ideal of }M\text{, i.e. }(x_n\cdot b_n+ a_n\cdot y_n+a_n\cdot b_n)\in I\\
&=&((x_n)_{n\in\mathbb N} + I)\cdot ((y_n)_{n\in\mathbb N} + I)&\text{by hypothesis}\\
\end{array}\]`

This demonstrates that the multiplication of real numbers "`\(\cdot\)`" does not depend on the particular choice of their representatives `\((x_n)_{n\in\mathbb N},(y_n)_{n\in\mathbb N}\in M\)` or `\((x_n^\prime)_{n\in\mathbb N},(y_n^\prime)_{n\in\mathbb N}\in M\)`.
