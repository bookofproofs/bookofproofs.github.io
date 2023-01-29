layout: proof
categories: branches,analysis
nodeid: bookofproofs$1162
orderid: 50
parentid: bookofproofs$1161
title: 
description:  Proof of SQUARE ROOTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: square root,square roots,roots,proof
contributors: bookofproofs

---


---

Let `\(a > 0\)` be a [real number][bookofproofs$1105]. We want to find all solutions of the equation
`\[x^2=a.\quad\quad( * )\]`

The key to find a solution is the observation that if `\(x\)` is a solution of the equation `\( ( * ) \)`, then `\(x=\frac ax\)`, otherwise `\(x\neq\frac ax\)`. Therefore, if `\(x_0\)` is any approximation of the solution of `\( ( * ) \)`, the mean value 

`\[x_1:=\frac 12\left(x_0+\frac a{x_0}\right)\]`

will be a better approximation to that solution. 

Therefore, we define a [sequence of real numbers][bookofproofs$875].
`\[\begin{array}{ll}
x_0 > 0 \in\mathbb R\quad\text{(arbitrarily chosen)}\\
x_{n+1}:=\frac 12\left(x_n +  \frac a{x_n}\right)
\end{array}\]`

The proof consists of three steps: 

### `\((1)\)` We show that `\(\lim_{n\rightarrow\infty} x_n=\sqrt a\)`.

First, we gather some extensions about the behavior of the sequence members of  `\((x_n)_{n\in\mathbb N}\)`.

> (i) We have to make sure that the sequence is well-defined, in particular that there are no divisions by 0, when calculating the sequence members. We prove [by induction][bookofproofs$657] that `\(x_{n} >  0\)` for all `\(n \ge 0\)`. Since `\(x_0 > 0\)` by hypothesis, we can assume that `\(x_n > 0\)` is proven for all `\(n\)`, which are lower or equal some `\(n_0\ge 0\)`. Therefore (induction step) `\(x_{n+1}\)` is a sum of positive values. Thus, `\(x_{n+1} > 0\)`.

> (ii) Next, we observe that `\(x_n^2 \ge a\)` for all `\(n\ge 1\)`. This is because
`\[x^2_n-a=\frac 14\left(x_n +\frac a{x_n}\right)^2-a=\frac 14\left(x^2_n + 2a +\frac {a^2}{x^2_n}\right)-\frac {4a}4=\frac 14\left(x^2_n -2a+\frac 4{x^2_n}\right)=\frac 14\left(x_n -\frac a{x_n}\right)^2 \ge 0.\]`

> (iii) From (ii), it follows that `\(1/{x_n^2} \le 1/a\)` for all `\(n\ge 1\)`. After multiplying the inequality by `\(a^2\)`, we observe that `\(\left(\frac a{x_{n}}\right)^2\le a\)` for all `\(n \ge 1\)`.

After showing (i) - (iii), we can start to study to compare the distances between the sequence members.

> (iv)  We will show that `\(x_{n+1}\le x_n\)` for all `\(n\ge 1\)`. This is because
`\[x_n-x_{n+1}=x_n-\frac 12\left(x_n +  \frac a{x_n}\right)=\frac{2x^2_n}{2x_n}-\frac{x^2_n}{2x_n}-\frac{a}{2x_n}=\frac{x^2_n - a}{2x_n} \ge 0\]`

> (v) From (iii) and (iv) it follows for `\(n\ge 1\)` that 
`\[\frac a{x_{n}}\le \frac a{x_{n+1}}.\]`

> (vi) We have for all `\(n\ge 1\)` that 
`\[\frac a{x_{n}}\le x_n\]`
Otherwise, we would have `\((a/x_n)^2 > x_n^2\)`, which by (ii) leads to `\((a/x_n)^2 > a\)`, in [contradiction][bookofproofs$744] to (iii).

From (iii), (iv) and (vi), it follows that `\((x_n)_{n\in\mathbb N}\)` is a [bounded sequence][bookofproofs$1136]  with 

`\[\frac{a}{x_1} \le x_n \le x_1.\]`

and that it is [monotonically decreasing][bookofproofs$197]. According to the [monotone convergence theorem][bookofproofs$197] it has a limit. Thus, it must be a number `\(x\)` satisfying the equation `\(x=\frac ax\)`. We denote `\(x\)` by `\(\sqrt a\)`.

### `\( (2) \)` With `\(\sqrt a\)` also `\(-\sqrt a\)` is a solution of `\( ( * ) \)`. 

This follows from the [rule][bookofproofs$531] that `\((-x)(-y)=xy\)` holds for all `\(x,y\in\mathbb R\)`. 

### `\( (3) \)` There are no other solutions of `\( ( * ) \)`. 

By construction, the sequence `\((x_n)_{n\in\mathbb N}\)` [converges][bookofproofs$141]  to the number `\(x\)` satisfying `\(x=\frac ax\)`. The proposition follows from the fact that the [limit of a convergent sequence is unique][bookofproofs$1129].