layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1599
orderid: 50
parentid: bookofproofs$1598
title: 
description:  Proof of MULTIPLYING NEGATIVE AND POSITIVE REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: multiplying,negative,numbers,positive,real,proof
contributors: bookofproofs

---


---

According to the [definition of negative and positive real numbers][bookofproofs$1107], we can represent a real number `\(x\)` in three ways:
`\[x=(x_n)_{n\in\mathbb N} + I:\begin{cases}\text{there is } N\text{ such that } x_n > 0\text{ for all } n > N&\Longleftrightarrow \text{ if }x\text{ is a positive real number}\\
\text{for all rational } \epsilon > 0 \text{ there is }N\text{ such that }-\epsilon < x_n < \epsilon\text{ for all }n > N&\Longleftrightarrow \text{ if }x\text{ equals 0}\\
\text{there is } N\text{ such that } x_n < 0\text{ for all } n > N&\Longleftrightarrow \text{ if }x\text{ is a negative real number}
\end{cases}\]`

Due to the  [definition of multiplying real numbers][bookofproofs$1532], we have for two real numbers `\(x=(x_n)_{n\in\mathbb N} + I\)` and `\(y=(y_n)_{n\in\mathbb N} + I\)`:

`\[\begin{array}{ccl}
x\cdot y:=(x_n\cdot y_n)_{n\in\mathbb N} + I.\quad\quad ( * )
\end{array}
\]`

Because the [multiplication of real numbers is commutative][bookofproofs$38], it is sufficient to prove the following four cases, applying the rules of [multiplying negative and positive rational numbers][bookofproofs$1596]:

### `\((1)\)` A positive real number times a positive real number gives a positive real number.

Assume `\(x > 0\)` and `\(y > 0\)`. Then there exist indices `\(N_x,N_y\)` such that `\(x_n > 0\)` for all `\(n > N_x\)` and `\(y_n > 0\)` for all `\(n > N_y\)`. Set `\(N=\max(N_x,N_y)\)`, then `\(x_n\cdot y_n > 0\)` for all `\(n > N\)`, and `\(xy\)` proves to be a positive real number.

### `\((2)\)` A negative real number times a positive real number gives a negative real number.

Assume `\(x < 0\)` and `\(y > 0\)`. Then there exist indices `\(N_x,N_y\)` such that `\(x_n < 0\)` for all `\(n > N_x\)` and `\(y_n > 0\)` for all `\(n > N_y\)`. Set `\(N=\max(N_x,N_y)\)`, then `\(x_n\cdot y_n < 0\)` for all `\(n > N\)`, and `\(xy\)` proves to be a negative real number.

### `\((3)\)` A negative real number times a negative real number gives a positive real number.

Assume `\(x < 0\)` and `\(y < 0\)`. Therefore, there exist indices `\(N_x,N_y\)` such that `\(x_n < 0\)` for all `\(n > N_x\)` and `\(y_n < 0\)` for all `\(n > N_y\)`. Set `\(N=\max(N_x,N_y)\)`, then `\(x_n\cdot y_n > 0\)` for all `\(n > N\)`, and `\(xy\)` is a positive real number.

### `\((4)\)` Zero times any real number gives zero.

Assume `\(x = 0\)` and `\(y\)` be any real number. Note that, like in any rational Cauchy sequence, the sequence members in `\((y_n)_{n\in\mathbb N}\)` [must be bounded][bookofproofs$1489]. This means that there exists a rational constant `\(c\in\mathbb Q\)` such that `\(|y_n| < c\)` for all `\(n\in\mathbb N\)`. Moreover, for any rational `\(\epsilon > 0\)`, there exists an index `\(N(\epsilon,c)\)` such that `\[\frac{-\epsilon}c <  x_n < \frac{\epsilon}c\]` for all `\(n > N(\epsilon,c)\)`. Then `\[-\epsilon < x_n\cdot y_n < \epsilon\]` for all `\(n > N(\epsilon,c)\)`. This means that the product `\(xy\)` equals zero.
