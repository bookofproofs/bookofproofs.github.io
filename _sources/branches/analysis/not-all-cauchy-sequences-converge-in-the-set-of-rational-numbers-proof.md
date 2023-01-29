layout: proof
categories: branches,analysis
nodeid: bookofproofs$1098
orderid: 50
parentid: bookofproofs$1092
title: 
description:  Proof of NOT ALL CAUCHY SEQUENCES CONVERGE IN THE SET OF RATIONAL NUMBERS. &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$582
keywords: cauchy sequence that does not converge,is every cauchy sequence convergent,cauchy sequence not convergent,are all cauchy sequences convergent,every cauchy sequence is not convergent,non convergent cauchy sequence,do all cauchy sequences converge,cauchy sequence,cauchy but not convergent,proof
contributors: bookofproofs

---


---

Our prove will be in two steps: `\((1)\)` to prove that the sequence `\((x_n)_{n\in\mathbb N}\)` of (rational numbers) defined recursively by 
`\[\begin{array}{ll}
x_0 > 0 \in\mathbb Q\quad\text{(arbitrarily chosen)}\\
x_{n+1}:=\frac 12\left(x_n +  \frac 2{x_n}\right)
\end{array}\]`
is a (rational) [Cauchy sequence][bookofproofs$1072] and `\((2)\)` that it [is not convergent][bookofproofs$1572] in the [metric space][bookofproofs$1090] `\((\mathbb Q,|~|)\)`.

### `\((1)\)` `\((x_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence.

We have to show that for any rational number `\(\epsilon > 0\)`, (no matter how small it is), there exists an `\(N\in\mathbb N\)` with
`\[|x_n-x_m| < \epsilon\quad\quad\text{ for all }n,m\ge N.\]`

> (i) We have to make sure that the sequence is well-defined, in particular that there are no divisions by 0, when calculating the sequence members. We prove [by induction][bookofproofs$657] that `\(x_{n} >  0\)` for all `\(n \ge 0\)`. Since `\(x_0 > 0\)` by hypothesis, we can assume that `\(x_n > 0\)` is proven for all `\(n\)`, which are lower or equal some `\(n_0\ge 0\)`. Therefore (induction step) `\(x_{n+1}\)` is a sum of positive values. Thus, `\(x_{n+1} > 0\)`.

> (ii) Next, we observe that `\(x_n^2 \ge 2\)` for all `\(n\ge 1\)`. This is because
`\[x^2_n-2=\frac 14\left(x_n +\frac 2{x_n}\right)^2-2=\frac 14\left(x^2_n +4+\frac 4{x^2_n}\right)-\frac 84=\frac 14\left(x^2_n -4+\frac 4{x^2_n}\right)=\frac 14\left(x_n -\frac 2{x_n}\right)^2 \ge 0.\]`

> (iii) From (ii), it follows that `\(1/{x_n^2} \le 1/2\)` for all `\(n\ge 1\)`. After multiplying the inequality by `\(2^2\)`, we observe that `\(\left(\frac 2{x_{n}}\right)^2\le 2\)` for all `\(n \ge 1\)`.

After showing (i) - (iii), we can start to study to compare the distances between the sequence members.

> (iv)  We will show that `\(x_{n+1}\le x_n\)` for all `\(n\ge 1\)`. This is because
`\[x_n-x_{n+1}=x_n-\frac 12\left(x_n +  \frac 2{x_n}\right)=\frac{2x^2_n}{2x_n}-\frac{x^2_n}{2x_n}-\frac{2}{2x_n}=\frac{x^2_n - 2}{2x_n} \ge 0\]`

> (v) From (iii) and (iv) it follows for `\(n\ge 1\)` that 
`\[\frac 2{x_{n}}\le \frac 2{x_{n+1}}.\]`

> (vi) We have for all `\(n\ge 1\)` that 
`\[\frac 2{x_{n}}\le x_n\]`
Otherwise, we would have `\((2/x_n)^2 > x_n^2\)`, which by (ii) leads to `\((2/x_n)^2 > 2\)`, in [contradiction][bookofproofs$744] to (iii).

We observe that all consecutive sequence members are rational numbers (since they start from a rational number `\(x_0\)` and are created by the arithmetic mean of the rational numbers `\(x_n\)` and `\(2/x_n\)`, which is also a rational number). Moreover, from (vi), (v) and (vi) it follows that `\(x_n\)` and `\(2/x_n\)` are getting closer and closer to each other in each step of calculation so we get a chain of inequalities 
`\[\frac 2{x_1}\le\ldots\le\frac 2{x_{n-1}}\le\frac 2{x_n}\le\ldots \le x_n\le x_{n-1}\le\ldots\le x_1\quad\quad( * ).\]`
More precisely, given an arbitrarily small rational number `\(\epsilon > 0,\epsilon \in\mathbb Q\)`, we are always able to find an index `\(N\in\mathbb N\)`, for which the distance between the two rational numbers `\(x_n\)` and `\(2/x_n\)` will get at least as small as the rational number `\(\epsilon\)`, if the index `\(n\)` exceeds `\(N\)`:
`\[\left|x_n - \frac 2{x_n}\right| < \epsilon\quad\text{ for all }n\ge N\quad\quad( * * ).\]`
To realize this, let's see what happens when we build the consecutive sequence members. Because `\(x_{n+1}\)` is always the arithmetic mean of `\(x_n\)` and `\(2/x_n\)`, its distance to these numbers is always the `\(\frac 12\)` the distance from `\(x_n\)` and `\(2/x_n\)`. Thus, we have 
`\[\begin{array}{ccc}
\left|x_2-\frac 2{x_2}\right|&\le&\frac 12\cdot \left|x_1-\frac 2{x_1}\right|\\
\left|x_3-\frac 2{x_3}\right|&\le&\frac 1{2^2}\cdot \left|x_1-\frac 2{x_1}\right|\\
\left|x_4-\frac 2{x_4}\right|&\le&\frac 1{2^3}\cdot \left|x_1-\frac 2{x_1}\right|\\
\vdots&\le&\vdots\\
\left|x_{n}-\frac 2{x_{n}}\right|&\le&\frac 1{2^{n-1}}\cdot \left|x_1-\frac 2{x_1}\right|\\
\end{array}
\]`
Since `\(Q:=|x_1 - 2/x_1|\)` is a __constant__ positive rational number, we will finally achieve `\(( * * )\)`, if the index `\(n\)` exceeds an `\(N\)`, which we can calculate only depending from the originally chosen `\(\epsilon\)` - just chose an `\(N\)` as big, as the inequation `\[2^{N-1} > \frac Q\epsilon\]` is fulfilled. 

Recall the inequations `\( ( * ) \)` above and observe that also all sequence members `\(x_m\)` lie between  `\(x_n\)` and `\(2/x_n\)`, if `\(m \ge n\)`, which we can assume without any loss of generality. Thus, we finally get the required result
`\[|x_n-x_m|\le\left|x_{n}-\frac 2{x_{n}}\right| \le \frac 1{2^{n-1}}\cdot \left|x_1-\frac 2{x_1}\right| \le \frac 1{2^{N-1}}\cdot \left|x_1-\frac 2{x_1}\right|  < \epsilon\quad\quad\text{ for all }n,m\ge N,\]`
which means that `\((x_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence.

### `\((2)\)` The rational Cauchy sequence `\((x_n)_{n\in\mathbb N}\)` does not converge in `\((Q,|~|)\)`.

We have seen in `\((1\)`) that the rational numbers `\(x_n\)` and `\(\frac 2{x_n}\)` get arbitrarily close to some limit `\(x\)` such that `\(x^2=2\)`, or `\(x=\sqrt 2\)`. However, `\(\sqrt 2\)` proves to be [irrational][bookofproofs$1096]. In other words, the sequence `\((x_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence, but it does not converge to a rational limit.
