layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1493
orderid: 50
parentid: bookofproofs$1488
title: 
description:  Proof of MULTIPLICATION OF RATIONAL CAUCHY SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: multiplication,rational cauchy sequences,cauchy sequence,definition of cauchy sequence,define cauchy sequence,what is a cauchy sequence,what is cauchy sequence,proof
contributors: bookofproofs

---


---

It had been shown already that [all rational Cauchy sequences are bounded][bookofproofs$1489]. In particular, for any two given rational Cauchy sequences `\((x_n)_{n\in\mathbb N}\)` and `\((y_n)_{n\in\mathbb N}\)`, we can find rational constants `\(c_x > 0,c_y > 0\in\mathbb Q\)` with
`\[|x_n|\le c_x\quad\text{respectively}\quad|y_n|\le c_y\quad\quad\text{for all }n\in\mathbb N.\]`

[By definition of rational Cauchy sequences][bookofproofs$1485], for any arbitrarily small rational number `\(\epsilon > 0\)`, we can find two natural numbers `\(N_x(\epsilon/(2c_x))\)` and `\(N_y(\epsilon/(2c_y))\)` such that for all `\(n,m\in\mathbb N\)` with `\(n, m > N(\epsilon):=\max(N_x(\epsilon/(2c_x)),N_y(\epsilon/(2c_y)))\)` we have[^1]
`\[|x_n  - x_m| < \frac\epsilon{2c_x} \quad\text{and}\quad |y_n  - y_m| < \frac\epsilon{2c_y}\quad\quad( * ). \]`

With this estimation, and using the following mathematical definitions and concepts:
* rational `\(0\)` [is neutral with respect to the addition of rational numbers][bookofproofs$1473],
* [definition of adding rational numbers][bookofproofs$1446],
* [distributivity law for rational numbers][bookofproofs$1491],
* [properties of the absolute value for rational numbers][bookofproofs$1090], and
*  [definition of multiplying integers][bookofproofs$1475]:

`\[\begin{array}{ccll}
|x_n \cdot b_n - x_m \cdot b_m|&=& |x_n \cdot y_n + 0 - x_m \cdot y_m|&\text{because }0\text{ is neutral with respect to the addition of rational numbers}\\
&=& |x_n \cdot y_n - x_n\cdot y_m + x_n\cdot y_m - x_m \cdot y_m|&\text{adding (inverse) rational numbers results in }0\\
&=&|x_n\cdot(y_n-y_m)+y_m\cdot(x_n-x_m)|&\text{by distributivity law for rational numbers}\\
&\le&|x_n\cdot(y_n-y_m)|+|y_m\cdot(x_n-x_m)|&\text{by triangle inequality}\\
&=&|x_n|\cdot|y_n-y_m|+|y_m|\cdot|x_n-x_m|\\
&\le& c_x\cdot\frac\epsilon{2c_x} + c_y\cdot\frac\epsilon{2c_y}&\text{by estimation above }( * )\\
&=& \frac\epsilon{2} + \frac\epsilon{2}&\text{by multiplication of rational numbers}\\
&=&\epsilon&\text{by addition of rational numbers}\\
\end{array}
\]`

As this estimation is valid for all `\(n, m > N(\epsilon)\)`, it follows that the sequence of such products `\((x_n \cdot y_n)_{n\in\mathbb N}\)` is a rational Cauchy sequence.

[^1]: Note that both, `\(c_x > 0, c_y > 0\)` by construction, so we do not have to be afraid of dividing by zero in the above reasoning.
