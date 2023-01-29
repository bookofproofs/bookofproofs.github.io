layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1653
orderid: 100
parentid: bookofproofs$1647
title: 
description:  Proof of ALGEBRAIC STRUCTURE OF RATIONAL NUMBERS TOGETHER WITH ADDITION AND MULTIPLICATION &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: field of rational numbers,proof
contributors: bookofproofs

---


---

This proof is a direct application of the theorem [construction of fields from integral domains][bookofproofs$888] `\(( * )\)`, in which we will construct the field `\((\mathbb Q, +,\cdot)\)` from the [integral domain][bookofproofs$892] `\((\mathbb Z, +,\cdot)\)`.

In the proof of the theorem `\(( * )\)`, a field `\((F,\ast,\circ)\)` is constructed from an integral domain `\((R, +,\cdot )\)`, as the set of all [equivalence classes][bookofproofs$7990] `\([a,b]\)`, which are represented by ordered pairs `\((a,b),(c,d)\in R\times (R\setminus\{0\})\)` together with the following equivalence relation:

`$$(a,b)\sim (c,d)\Leftrightarrow ad=bc.$$`

In this proof, the operations `\(\ast\)` and `\(\circ\)` are defined as follows:
`$$\begin{array}{ccl}
\lbrack a,b\rbrack \ast\lbrack c,d\rbrack &:=&\lbrack ad + cb,~bd\rbrack ,\\
\lbrack a,b\rbrack \circ\lbrack c,d\rbrack &:=&\lbrack ac,~bd\rbrack .\\
\end{array} $$`

For the special case of the integral domain `\((R, + ,\cdot) =(\mathbb Z, + ,\cdot )\)`, the equivalence relation is defined for two ratios

`$$\frac ab\sim \frac cd\Leftrightarrow ad=bc,~~~~~~~~~~a,c\in\mathbb Z,~~b,d\in\mathbb Z\setminus\{0\}$$`

and the field operations in `\((\mathbb Q,\ast,\circ)\)`, "addition `\(\ast\)`" and the "multiplication `\(\circ\)`" can be now written as 
`$$\begin{array}{ccccc}
\frac ab \ast \frac cd &:=&\frac ab + \frac cd &=&\frac {a\cdot d + c\cdot b}{b\cdot d},\\
\frac ab \circ\frac cd &:=&\frac ab \cdot \frac cd &=&\frac {a\cdot c}{b\cdot d}.\\
\end{array} $$`
Thereby, we have replaced the notation `\((\mathbb Q,\ast,\circ)\)` by the more common notation `\((\mathbb Q, + ,\cdot)\)`.

Furthermore, according to the proof of `\(( * )\)`, the integral domain `\((\mathbb Z, +,\cdot )\)` is isomorphic to a proper subset `\(S\subset\mathbb Q\)` with (using our new notation)
`$$\mathbb Z\simeq  S:=\left\{\frac {a\cdot x}x~|~a\in\mathbb Z,~x\in\mathbb Z\setminus\{0\}\right\}.$$`
Please note, that since `\((\mathbb Z, +,\cdot )\)` is an integral domain, we can even write `\(\frac {a\cdot x}x=\frac {a\cdot \cancel x}{\cancel x}=\frac a1\)`. Thus, `\((\mathbb Z, +, \cdot)\)` can be regarded as a proper subset of `\((\mathbb Q, +,\cdot)\)` (i.e. each integer is a special case of a fraction), preserving the effect of the operations  `\( + \)` and `\(\cdot\)`, defined for fractions.

We also learn from the proof of theorem `\(( * )\)`:

* the additive identity (zero) is given by the fraction `\(0:=\frac 01\)`, 
* the multiplicative identity is given by the fraction `\(1:=\frac 11\)`.
* the additive inverse element to a given fraction `\(\frac ab\)` is `\(-\frac ab:=\frac {-a}b\)`, `\(b\neq 0\)`.
* the multiplicative inverse element to a given fraction `\(\frac ab\)` is `\(\frac ba\)`, `\(a,b\neq 0\)`.

This completes the proof.
