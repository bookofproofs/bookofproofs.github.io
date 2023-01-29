layout: proof
categories: branches,topology
nodeid: bookofproofs$1074
orderid: 50
parentid: bookofproofs$1073
title: 
description: Proof of CONVERGENT SEQUENCES ARE CAUCHY SEQUENCES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$582
keywords: convergent sequences are cauchy sequences,proof
contributors: bookofproofs

---


---

* By hypothesis, `\((a_n)_{n\in\mathbb N}\)` is a [convergent sequence][bookofproofs$148] of points in the [mectric space][bookofproofs$617] `\((X,d)\)` with a limit `\(\lim_{n\rightarrow\infty} a_n=a\)`.
Thus, for each `\(\epsilon > 0\)` there exists an index `\(N\in\mathbb N\)` with `\[d(a_n,a)  < \epsilon\quad\quad\text{ for all }n\ge N.\]`
* Therefore, and because of the [property of the metric (triangle inequality) ][bookofproofs$614], it follows  for all `\(i,j\ge N\)`  `\[ d(a_i,a_j) \le d(a_i,a) + d(a,a_j) < \epsilon + \epsilon =2\epsilon.\]`
* Since `\(\epsilon > 0\)` can be chosen arbitrarily close to `\(0\)`, it follows that the sequence `\((a_n)\)` is also a [Cauchy sequence][bookofproofs$1072].