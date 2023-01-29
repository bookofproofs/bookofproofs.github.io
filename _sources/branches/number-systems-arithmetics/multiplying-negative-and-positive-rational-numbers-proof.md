layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1597
orderid: 50
parentid: bookofproofs$1596
title: 
description:  Proof of MULTIPLYING NEGATIVE AND POSITIVE RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: multiplying,negative,numbers,positive,rational,proof
contributors: bookofproofs

---


---

According to the [definition of negative and positive rational numbers][bookofproofs$1076], we can represent a rational number `\(x\)` by an ordered pair of 0 and a [positive][bookofproofs$1075] integer `\(b > 0\)` or two positive integers `\(a > 0,~b > 0\)` in three ways:
`\[x=\begin{cases}\frac ab,~b\neq 0&\Longleftrightarrow \text{ if }x\text{ is a positive rational number}\\
\frac 0b,~b\neq 0&\Longleftrightarrow \text{ if }x\text{ equals 0}\\
\frac {-a}b,~b\neq 0&\Longleftrightarrow \text{ if }x\text{ is a negative rational number}\\
\end{cases}\]`

Due to the  [definition of multiplying rational numbers][bookofproofs$1475], we have for two rational numbers `\(x=\frac ab\)` and `\(y=\frac cd\)`, `\(b\neq 0\)`, `\(d\neq 0\)`:

`\[\begin{array}{ccl}
x\cdot y:=\frac {ac}{bd}.\quad\quad ( * )
\end{array}
\]`

Because the [multiplication of rational numbers is commutative][bookofproofs$1478], it is sufficient to prove the following four cases, applying the rules of [multiplying negative and positive integers][bookofproofs$1589]:

### `\((1)\)` A positive rational number times a positive rational number gives a positive rational number.

Let `\(x=\frac ab\)` and `\(y=\frac cd\)` with `\(a > 0,~b > 0,~c > 0,~d > 0\)`. It follows in `\( ( * ) \)` that `\(ac > 0\)` and `\(bd > 0\)`, thus the product is a positive rational number.

### `\((2)\)` A negative rational number times a positive rational number gives a negative rational number.

Let `\(x=\frac ab\)` and `\(y=\frac cd\)` with `\(a < 0,~b > 0,~c > 0,~d > 0\)`. It follows in `\( ( * ) \)` that `\(ac < 0\)` and `\(bd > 0\)`, thus the product is a negative rational number.

### `\((3)\)` A negative rational number times a negative rational number gives a positive rational number.

Let `\(x=\frac ab\)` and `\(y=\frac cd\)` with `\(a < 0,~b > 0,~c < 0,~d > 0\)`. It follows in `\( ( * ) \)` that `\(ac > 0\)` and `\(bd > 0\)`, thus the product is a positive rational number.

### `\((4)\)` Zero times any rational number gives zero.

Let `\(x=\frac ab\)` and `\(y=\frac cd\)` with `\(a = 0,~b > 0,~d > 0\)` and an arbitrary `\(c\in\mathbb Z\)`. It follows in `\( ( * ) \)` that `\(ac = 0\)` and `\(bd > 0\)`, thus the product is zero.
