layout: motivation
categories: branches,algebra
nodeid: bookofproofs$8248
orderid: 50
parentid: bookofproofs$234
title: Rational Numbers and the Greatest Common Divisor
description: RATIONAL NUMBERS AND THE GREATEST COMMON DIVISOR &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$8189
keywords: common,divisor,greatest,numbers,rational,gcd of rational numbers
contributors: bookofproofs


---


---

Let `$\frac{a}b\in\mathbb Q$` be a [rational number][bookofproofs$1033] with `$0 < a$` and `$0 < b.$` In the [proof of the greatest common divisor][bookofproofs$1286] for the calculation of the [greatest common divisor][bookofproofs$1280] `$\gcd(a,b)$`, the Euclidean algorithm can be written with a sequence of rational numbers defined as follows:

`$$\begin{array}{rclclcl}
\frac{a}{b} & = & q_0 & + & \frac{r_1}{b} & \text{with} & q_0\in\mathbb N,\; 0 < r_1 < b\\
\frac{b}{r_1} & = & q_1 & + & \frac{r_2}{r_1} & \text{with} & q_1\in\mathbb N,\; 0 < r_2 < r_1\\
\frac{r_1}{r_2} & = & q_2 & + & \frac{r_3}{r_2}& \text{with} & q_2\in\mathbb N,\; 0 < r_3 < r_2\\
&\vdots&\\
\frac{r_{n-3}}{r_{n-2}} & = & q_{n-2}& + & \frac{r_{n-1}}{r_{n-2}} & \text{with} & q_{n-2}\in\mathbb N,\; 0 < r_{n-1} < r_{n-2}\\
\frac{r_{n-2}}{r_{n-1}} & = & q_{n-1}& + & \frac{r_{n}}{r_{n-1}} & \text{with} & q_{n-1}\in\mathbb N,\;  0 < r_{n} < r_{n-1}\\
\frac{r_{n-1}}{r_{n}} & = & q_{n} &&& \text{with} & q_{n}\in\mathbb N
\end{array}$$`

Therefore, we can put the ratios in each other and get the following representation of the number `$\frac ab$`:

`$$\frac{a}b=q_0+\cfrac{1}{q_1+\cfrac{1}{q_2+\cfrac{1}{\ddots+\cfrac{1}{q_{n-2}+\cfrac{1}{q_{n-1}+\cfrac{1}{q_n}}}}}}$$`

Please note that because `$r_{n} < r_{n-1}$`, we have `$q_n > 1$` and thus `$q_n\neq 0.$` Thus, this representation is well-defined. It is possible to represent any positive rational number this way. But how about [irrational numbers][bookofproofs$6663]. In order to answer this question, we will introduce a new concept, the concept of _continued fractions_.
