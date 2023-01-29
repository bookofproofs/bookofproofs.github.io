layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1651
orderid: 50
parentid: bookofproofs$42
title: 
description:  Proof of EXISTENCE OF INVERSE REAL NUMBERS WITH RESPECT TO MULTIPLICATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: existence,inverse,multiplication,numbers,real,respect,proof
contributors: bookofproofs

---


---

We have to show that each [real number][bookofproofs$1105], which does not equal [zero][bookofproofs$34], formally `\(x\neq 0\)`, has an inverse element `\(x^{-1}:=y\)` such that the [multiplication of both numbers][bookofproofs$1532] equals [one][bookofproofs$40], formally `\(x\cdot y=1\)`. 

Let `\(x\)` be represented by the [rational Cauchy sequence][bookofproofs$1485] `\((x_n)_{n\in\mathbb N}\)` and let `\(I\)` be the set of all rational Cauchy sequences [convergent][bookofproofs$1572] to `\(0\in\mathbb Q\)`, in other words, `\(x=(x_n)_{n\in\mathbb N} + I\)`. 

Then, by hypothesis, `\((x_n)_{n\in\mathbb N}\not\in I\)`. Following the [definition of convergence of rational sequences][bookofproofs$1572], this means that there are numbers `\(\epsilon_0 > 0, \epsilon_0\in\mathbb Q\)` and `\(N(\epsilon_0)\in\mathbb N\)` such that `\(|x_n|>\epsilon_0\)` for all `\(n > N(\epsilon_0)\)`. Therefore, `\(|x_n|\neq 0\)` for sufficiently large indices `\(n > N(\epsilon_0)\)`. With this result, we define a rational sequence `\((y_n)_{n\in\mathbb N}\)` with

`\[y_n:=\begin{cases}
0,&\quad 0\le n\le N(\epsilon_0)\\
\frac 1{x_n},&\quad n > N(\epsilon_0).
\end{cases}\quad\quad\quad( * )\]`
We will now show:

### `\((i)\)` `\(y=(y_n)_{n\in\mathbb N} + I\)` is a real number. 

Equivalently, we have to show that `\((y_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence. For `\(n,m > N(\epsilon_0)\)` we have 
`\[|y_n - y_m|=\left|\frac 1{x_n}-\frac 1{x_m}\right|=\frac {|x_n - x_m|}{|x_n\cdot x_m|} < \frac {|x_n - x_m|}{\epsilon_0^2}.\]`
Because `\((x_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence by hypothesis, for any arbitrarily small `\(\epsilon > 0, \epsilon \in\mathbb Q\)` there exists an `\(N(\epsilon_0^2\cdot \epsilon)\)` such that for all `\(n,m > N(\epsilon_0^2\cdot \epsilon)\)` we have 
`\[|x_n - x_m| < \epsilon_0^2\cdot \epsilon.\]`
Thus, for all `\(n,m > \max(N(\epsilon_0),N(\epsilon_0^2\cdot \epsilon))\)` we have 
`\[|y_n - y_m| <  \frac {|x_n - x_m|}{\epsilon_0^2} < \frac {\epsilon_0^2\cdot \epsilon}{\epsilon_0^2}=\epsilon,\]`
which proves that `\((y_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence, and `\(y\)` is a real number.

### `\((ii)\)` `\(y\)` is the multiplicative inverse of `\(x\)`.

By the definition `\( ( * ) \)` above, we have
`\[x_n\cdot y_n=\begin{cases}
0,&\quad 0\le n\le N(\epsilon_0)\\
1,&\quad n > N(\epsilon_0).
\end{cases}\]`
Therefore,
`\[((x_n)_{n\in\mathbb N} + I)\cdot((y_n)_{n\in\mathbb N} + I)=(x_n\cdot y_n)_{n\in\mathbb N} + I=(1)_{n\in\mathbb N} + I\quad\quad\text{for all }n > N(\epsilon_0).\]`
This means that all except the first finitely many `\(N(\epsilon_0)\)`) rational Cauchy sequence members `\(x_n\cdot y_n\)` equal `\(1\in\mathbb Q\)`, and therefore `\(x\cdot y=1\in\mathbb R\)`.
