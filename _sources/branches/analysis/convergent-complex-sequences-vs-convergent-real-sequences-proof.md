layout: proof
categories: branches,analysis
nodeid: bookofproofs$1703
orderid: 50
parentid: bookofproofs$1702
title: 
description: Proof of CONVERGENT COMPLEX SEQUENCES VS. CONVERGENT REAL SEQUENCES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: convergent complex and real sequences,proof
contributors: bookofproofs

---


---

* By hypothesis, `\((c_n)_{n\in\mathbb N}\)` is a [complex sequence][bookofproofs$1249]. We set `\(c_n=a_n+i\cdot b_n\)` for some [real numbers][bookofproofs$1105] `\(a_n,b_n\)`. 

### `\("\Rightarrow"\)`

* Assume, `\((c_n)_{n\in\mathbb N}\)` is a [convergent complex sequence][bookofproofs$1700] with `\(\lim_{n\to\infty}c_n=c\)`. 
* Then, for each `\(\epsilon > 0\)`, there exists an `\(N\in\mathbb N\)` with `\[ | c_n-c | < \epsilon\quad\quad \text{ for all }n\ge N.\]`
* Because for every [complex number][bookofproofs$216] `\(x\in\mathbb C\)`, we have `\(|\Re(x)|\le |x|\)` and `\(|\Im(x)|\le |x|\)` by the definition [complex absolute value][bookofproofs$1247], it follows for all `\(n\ge N\)`:
`\[\begin{array}{c}
 | a_n-a |=|\Re(c_n -c)|\le  | c_n-c | < \epsilon\\
 | b_n-b |=|\Im(c_n -c)|\le  | c_n-c | < \epsilon\\
\end{array}\]`
* Thus, both [real sequences][bookofproofs$875] `\((a_n)_{n\in\mathbb N}\)` and  `\((b_n)_{n\in\mathbb N}\)`  are [convergent real sequences][bookofproofs$141] with `\(\lim_{n\to\infty}a_n = \Re( c)=a\)` and `\(\lim_{n\to\infty}b_n = \Im ( c)=b\)`.

### `\("\Leftarrow"\)`

* Assume, the [real sequences][bookofproofs$875] `\((a_n)_{n\in\mathbb N}\)` and  `\((b_n)_{n\in\mathbb N}\)`  are [convergent real sequences][bookofproofs$141] with `\(\lim_{n\to\infty}a_n =a\)` and `\(\lim_{n\to\infty}b_n=b\)`. 
* Then, for each `\(\epsilon > 0\)` there exist indices `\(N_a,N_b\in\mathbb N\)` with 
`\[ | a_n-a | < \frac\epsilon2\quad\quad \text{ for all }n\ge N_a\]`
and
`\[ | b_n-b | < \frac\epsilon2\quad\quad \text{ for all }n\ge N_b.\]`
* Set `\(c:=a+ib\)` and set `\(N:=\max(N_a,N_b)\)`. 
* Then, for all `\(n\ge N\)`, it follows from the [triangle inequality for the distance in the metric space of complex numbers][bookofproofs$1253] that
`$$\begin{align} | c_n-c | &= |a_n+ib_n-a-ib| \nonumber\\
&= |(a_n-a)+i(b_n-b)| \nonumber\\
&\le |a_n-a|+|b_n-b|\nonumber\\
& < \frac\epsilon2+\frac\epsilon2\nonumber\\
&=\epsilon.\nonumber\end{align}$$`
* Therefore, `\((c_n)_{n\in\mathbb N}\)` is a [convergent complex sequence][bookofproofs$1700] with `\(\lim_{n\to\infty}c_n=c\)`.
