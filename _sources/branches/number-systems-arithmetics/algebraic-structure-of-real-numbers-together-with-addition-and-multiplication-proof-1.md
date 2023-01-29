layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1644
orderid: 100
parentid: bookofproofs$1638
title: 
description:  Proof of ALGEBRAIC STRUCTURE OF REAL NUMBERS TOGETHER WITH ADDITION AND MULTIPLICATION &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: field of real numbers,algebraic structure of real numbers,proof
contributors: bookofproofs

---


---

According to the [definition of real numbers][bookofproofs$1105], a real number `\(x\)`  is the equivalence class of all rational Cauchy sequences, the difference of which converges to `\(0\in\mathbb Q\)`. 

We have proven that the set of all [rational Cauchy sequences][bookofproofs$1485], together with the [addition of rational Cauchy sequences][bookofproofs$1486] "`\(\oplus\)`" and the [multiplication of rational Cauchy sequences][bookofproofs$1488] "`\(\odot\)`", forms the [commutative unit ring of all rational Cauchy sequences][bookofproofs$1101] `\((M , \oplus , \odot)\)`. We have also proven that the set `\(I:=\{(a_n)_{n\in\mathbb N}~|~a_n\in\mathbb Q,\lim a_n=0\}\)` i.e. the set of all rational sequences, which converge to `\(0\)`, [is an ideal of][bookofproofs$1524] `\(M\)`, formally `\(I\lhd M\)`.

With these prerequisites, we can use a corresponding [lemma about factor rings][bookofproofs$274] to conclude the existence of a  commutative factor ring `\((M/I , + , \cdot)\)`, in which "`\(+\)`" and `\(\cdot\)` denote new addition (respectively multiplication) operations for the factor ring `\(M/I\)`. 

To identify the factor ring `\((M/I , + , \cdot)\)` with the [field][bookofproofs$557] of real numbers `\((\mathbb R , + , \cdot)\)`, it remains to be shown that each equivalence class `\((x_n)_{n\in\mathbb N} + I\)` with `\((x_n)_{n\in\mathbb N} + I\neq (0)_{n\in\mathbb N}+I\)` has a multiplicative inverse element in `\((M/I , + , \cdot)\)`. This is equivalent with the [existence of inverse elements with respect to multiplication][bookofproofs$42].