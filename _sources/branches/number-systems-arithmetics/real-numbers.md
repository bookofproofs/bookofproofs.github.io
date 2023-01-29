layout: part
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$167
orderid: 400
parentid: bookofproofs$195
title: Real Numbers
description: REAL NUMBERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: numbers,real,square root,real numbers
contributors: bookofproofs

---


---

### Motivation for the set of real numbers `\(\mathbb R\)`

In the set of [rational numbers][bookofproofs$125] `\(\mathbb Q=\left\{q:=\frac xy, x\in \mathbb Z, y\in \mathbb Z\setminus\{0\}\right\}\)` it is possible to solve any linear equation of the form

`\[ax + b = c,\quad\quad a,b,c\in\mathbb Q,~a\neq 0.\]`

The major motivation for further extending the realm of numbers is the solvability of the equation
`\[x^2=a,~~~~~~~(a\in \mathbb Q, a > 0)~~~~~~~~~~~~~~~~~~( * )\]`
which cannot be always solved by a rational number. For instance, while `\(x^2=\frac {25}{16}\)` has the two rational solutions `\(x_1=\frac 54,~x_2=-\frac 54\)`, there is no rational solution of the equation `\(x^2=2\)`, which was [discovered in 5th century BC in Ancient Greece][bookofproofs$1096].
The main reason for the generally missing solution of the equation `\(( * )\)` is the topological structure of rational numbers `\((\mathbb Q, + ,\cdot)\)`. On the one hand, rational numbers are a **dense set**, that is for any rational number `\(q\in\mathbb Q\)` and for any rational `\(\epsilon > 0\)` (no matter how small), there exists at least another rational number `\(p\)` such that the distance between `\(p\)` and `\(q\)` is smaller then `\(\epsilon\)`, formally `\(|q - p| < \epsilon\)`. On the other hand, there are surprisingly many [gaps between" rational numbers. One such gap is the solution of  `\(( * )\)` and there are infinitely many others, called "irrational numbers][bookofproofs$140]. What is even more surprising from the topological point of view, the cardinality of the rational numbers is, (in some strict sense called [countability][bookofproofs$773]), smaller then the cardinality of the irrational numbers. The rational numbers, together with the irrational numbers, constitute the set of real numbers.

If `\(a > 0\)` is any real number, then the equation  `\(( * )\)` has always two real numbers as solutions. This is why: Consider the sequence `\((x_n)_{n\in\mathbb N}\)` of real numbers  

`\[\begin{array}{ll}
x_0 > 0 \in\mathbb Q\quad\text{(arbitrarily chosen)}\\
x_{n+1}:=\frac 12\left(x_n +  \frac a{x_n}\right)
\end{array}\]`

It can be easily shown that this sequence is [monotonically decreasing][bookofproofs$1155] and [bounded][bookofproofs$1136] and as such, it is [convergent in the set of real numbers][bookofproofs$197]. The limit is called the **square root** of the number `\(a\)` and denoted by `\(\sqrt a\)`. Because `\((-\sqrt a)^2=(\sqrt a)^2\)`, also `\(-\sqrt a\)` is a solution of `\( ( * ) \)`. Thus, the equation `\( ( * ) \)` is always solvable and has at two real solutions: `\(x_1=\sqrt a,~x_2=-\sqrt a\)`.
