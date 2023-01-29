layout: proof
categories: branches,analysis
nodeid: bookofproofs$1706
orderid: 50
parentid: bookofproofs$1705
title: 
description: Proof of COMPLEX CAUCHY SEQUENCES VS. REAL CAUCHY SEQUENCES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: complex and real cauchy sequences,proof
contributors: bookofproofs

---


---

In the following `\((c_n)_{n\in\mathbb N}\)` is a [complex sequence][bookofproofs$1249] with `\(c_n=a_n+i\cdot b_n\)` for some [real numbers][bookofproofs$1105] `\(a_n,b_n\)`. We will prove two inclusions:

### `\("\Rightarrow"\)`

* Assume, `\((c_n)_{n\in\mathbb N}\)` is a [complex Cauchy sequence][bookofproofs$1250].
* Then, for each `\(\epsilon > 0\)`, there exists an `\(N\in\mathbb N\)` with 
`\[ | c_n-c_m | < \epsilon\quad\quad \text{ for all }n,m\ge N.\]`
* Because for every complex number `\(x\in\mathbb C\)`, we have `\(|\Re(x)|\le |x|\)` and `\(|\Im(x)|\le |x|\)`, it follows for all `\(m,n\ge N\)`:`\[\begin{array}{c}
 | a_n-a_m |=|\Re(c_n -c_m)|\le  | c_n-c_m | < \epsilon,\\
 | b_n-b_m |=|\Im(c_n -c_m)|\le  | c_n-c_m | < \epsilon.\\
\end{array}\]`
* Thus, both [real sequences][bookofproofs$875] `\((a_n)_{n\in\mathbb N}\)` and  `\((b_n)_{n\in\mathbb N}\)`  are [real Cauchy sequences][bookofproofs$1704].
### `\("\Leftarrow"\)`

* Assume, the [real sequences][bookofproofs$875] `\((a_n)_{n\in\mathbb N}\)` and  `\((b_n)_{n\in\mathbb N}\)` are [real Cauchy sequences][bookofproofs$1704].
* Then, for each `\(\epsilon > 0\)`, there exist indices `\(N_a,N_b\in\mathbb N\)` with `\[ | a_n-a_m | < \frac\epsilon2\quad\quad \text{ for all }n,m\ge N_a\]` and `\[ | b_n-b_m | < \frac\epsilon2\quad\quad \text{ for all }n,m\ge N_b.\]`
* Set `\(N:=\max(N_a,N_b)\)`. 
* Then, for all `\(n,m\ge N\)`, it follows from the [triangle inequality for the distance in the metric space of complex numbers][bookofproofs$1253] that
`$$\begin{align}| c_n-c_m |&= |a_n+ib_n -a_m-ib_m|\nonumber\\
&=|(a_n-a_m)+i(b_n-b_m)|\nonumber\\
&\le |a_n-a_m|+|b_n-b_m|\nonumber\\
& < \frac\epsilon2+\frac\epsilon2\nonumber\\
&=\epsilon.\nonumber\end{align}$$`
* Therefore, `\((c_n)_{n\in\mathbb N}\)` is a [complex Cauchy sequence][bookofproofs$1250].