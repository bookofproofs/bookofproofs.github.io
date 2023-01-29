layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1092
orderid: 600
parentid: bookofproofs$161
title: Not all Cauchy Sequences Converge in the set of Rational Numbers
description: NOT ALL CAUCHY SEQUENCES CONVERGE IN THE SET OF RATIONAL NUMBERS. ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$582,bookofproofs$696
keywords: cauchy sequence that does not converge,is every cauchy sequence convergent,cauchy sequence not convergent,are all cauchy sequences convergent,every cauchy sequence is not convergent,non convergent cauchy sequence,do all cauchy sequences converge,cauchy sequence,cauchy but not convergent
contributors: bookofproofs

---


---

In the [metric space][bookofproofs$1090] `\((\mathbb Q,|~|)\)`, consider the [sequence][bookofproofs$874] `\((x_n)_{n\in\mathbb N}\)` of (rational numbers) defined recursively by 
`\[\begin{array}{ll}
x_0 > 0 \in\mathbb Q\quad\text{(arbitrarily chosen)}\\
x_{n+1}:=\frac 12\left(x_n +  \frac 2{x_n}\right)
\end{array}\]`

The sequence `\((x_n)_{n\in\mathbb N}\)` is a [rational Cauchy sequence][bookofproofs$1485], however it [is not convergent][bookofproofs$1572] in `\((\mathbb Q,|~|)\)`. In other words, its limit (if it exists), is not a rational number.[^1] Because this is one example of such a non-convergent Cauchy sequence in `\((\mathbb Q,|~|)\)`, we can state more generally that, in the set of rational numbers, not all Cauchy sequences do converge.

[^1]: Please note that according to the corresponding lemma, [all convergent sequences are also Cauchy sequences][bookofproofs$1073] in any metric space and so in  `\((\mathbb Q,|~|)\)`. However the converse of the lemma is not true. In this  proposition an example of a Cauchy sequence in the metric space `\((\mathbb Q,|~|)\)` is given, which has no limit in this metric space!
