layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1823
orderid: 50
parentid: bookofproofs$1822
title: By Induction
description: PROOF BY INDUCTION Proof of MULTINOMIAL THEOREM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1209
keywords: multinomial coefficient,multinomial coefficients,multinomial coefficient proof,multinomial theorem example,proof,proof
contributors: bookofproofs

---


---

We want to prove that the [sum][bookofproofs$261] of `\(r\)` [complex][bookofproofs$216] or [real numbers][bookofproofs$1105] `\(x_1,x_2,\ldots,x_n\)` raised to the [`\(n\)`-th power][bookofproofs$1618] of will expand as follows:

`\[(x_1 + x_2 + \ldots + x_r)^n=\sum_{\substack{k_1+\ldots+k_r=n \\ k_1,\ldots,k_r}}\binom{n}{k_1,k_2\ldots,k_r}x_1^{k_1} x_2^{k_2}\ldots x_r^{k_r}.\]`

We will prove the theorem [by induction][bookofproofs$657] on `\(r\)`.

### `\(1)\)` Base case `\(r=1\)`

The multinomial theorem takes the form

`\[x_1^n=\binom{n}{n}x_1^{n}=x_1^n.\]`

### `\(2)\)` Induction step `\(r\to r+1\)`

Let the multinomial theorem be proved for an `\(r\)`. From the associativity law for complex numbers and by hypothesis, it follows


`\[\begin{array}{l}(x_1 + x_2 + \ldots + x_r+ x_{r+1})^n=\\(x_1 + x_2 + \ldots + x_{r-1}+(x_r+ x_{r+1}))^n\\
=\sum_{\substack{k_1+\ldots+k_{r-1}+K=n \\ k_1,\ldots,k_{r-1},K}}\binom{n}{k_1,k_2\ldots,k_{r-1},K}x_1^{k_1} x_2^{k_2}\ldots x_{r-1}^{k_{r-1}}\cdot(x_r+x_{r+1})^K.\end{array}\]`

Applying the [binomial theorem][bookofproofs$1397] to the last term in each sum, we get

`\[\begin{array}{l}\sum_{\substack{k_1+\ldots+k_{r-1}+K=n \\ k_1,\ldots,k_{r-1},K}}\binom{n}{k_1,k_2\ldots,k_{r-1},K}x_1^{k_1} x_2^{k_2}\ldots x_{r-1}^{k_{r-1}}\cdot(x_r+x_{r+1})^K=\\\sum_{\substack{k_1+\ldots+k_{r-1}+K=n \\ k_1,\ldots,k_{r-1},K}}\binom{n}{k_1,k_2\ldots,k_{r-1},K}x_1^{k_1} x_2^{k_2}\ldots x_{r-1}^{k_{r-1}}\cdot\sum_{k_r}^K\binom K{k_r}x_r^{k_r}x_{r+1}^{K-k_{r}}.\end{array}\]`

Note that the following [multinomial][bookofproofs$1819] and the [binomial coefficients][bookofproofs$1400] are equal:
`\[\binom K{k_r,k_{r+1}}=\binom K{k_r}\quad\quad\text{for }k_r=0,1,\ldots,K\text{ and for }k_{r+1}=K-k_r.\]` 

Therefore, we can write the last equation also this way:

`\[\begin{array}{l}\sum_{\substack{k_1+\ldots+k_{r-1}+K=n \\ k_1,\ldots,k_{r-1},K}}\binom{n}{k_1,k_2\ldots,k_{r-1},K}x_1^{k_1} x_2^{k_2}\ldots x_{r-1}^{k_{r-1}}\cdot(x_r+x_{r+1})^K=\\\sum_{\substack{k_1+\ldots+k_{r-1}+K=n \\ k_1,\ldots,k_{r-1},K}}\binom{n}{k_1,k_2\ldots,k_{r-1},K}x_1^{k_1} x_2^{k_2}\ldots x_{r-1}^{k_{r-1}}\cdot\sum_{k_r+k_{r+1}=K}\binom K{k_r,k_{r+1}}x_r^{k_r}x_{r+1}^{k_{r+1}}.\end{array}\quad\quad ( * )\]`


Since, by definition,

`\[\binom{n}{k_1,k_2\ldots,k_{r-1},K}\cdot\binom K{k_r,k_{r+1}}=\frac{n ! }{k_1 ! k_2 ! \ldots k_{r-1} ! K ! }\cdot\frac{K ! }{k_r ! k_{r+1} ! }=\frac{n ! }{k_1 ! k_2 ! \ldots k_{r+1} ! }=\binom{n}{k_1,k_2\ldots,k_{r+1}}\]`

we get
`\[( * ) = \sum_{\substack{k_1+\ldots+k_{r+1}=n \\ k_1,\ldots,k_r}}\binom{n}{k_1,k_2\ldots,k_{r+1}}x_1^{k_1} x_2^{k_2}\ldots x_{r+1}^{k_{r+1}}\]`
