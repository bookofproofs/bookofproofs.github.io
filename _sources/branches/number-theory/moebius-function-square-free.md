layout: definition
categories: branches,number-theory
nodeid: bookofproofs$8116
orderid: 200
parentid: bookofproofs$8113
title: Möbius Function, Square-free
description: MöBIUS FUNCTION, SQUARE-FREE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: möbius function,moebius function,square-free,möbius
contributors: bookofproofs


---


---

The **Möbius**  **Moebius**) function `$\mu:\mathbb N\to\{-1,0,1\}$` is an [arithmetic function][bookofproofs$8112] indictating if a natural number `$n > 0$` is *square-free*, i.e. if in its [canonical representation][bookofproofs$803].
`$$ n=\prod_{i=1}^\infty p_i^{e_i}$$`

all exponents `$e_i$` are less or equal `$1.$` More precisely, the Möbius function is defined by

`$$\mu(n) :=
\begin{cases}
1  & \text{if } n=1\\
(-1)^{r} & \text{if } n \text{ is square-free, i.e. a product of }r\text{ distinct primes }\\
0 & \text{else}
\end{cases}\quad\quad\forall n > 0.$$`

It was introduced by "August Ferdinand Möbius":https://www.bookofproofs.org/history/august-ferdinand-moebius/ (1790 - 1868) and plays a prominent role in number theory, as we will see later.

### Example.

The `$\mu$` function can be visualized using SageMath. If you click on the evaluate button, you will see the values of `$\mu(n)$` for `$n=1,\ldots,100.$` It is oscillating between the values `$0$` `$-1,$` and `$+1.$`

§§§1

---

§§§1
<div class='sage'>
moebiuspoints= [(i, moebius(i)) for i in range(1,100)]
list_plot(moebiuspoints)
</div>
