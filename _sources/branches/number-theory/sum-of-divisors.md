layout: definition
categories: branches,number-theory
nodeid: bookofproofs$8127
orderid: 50
parentid: bookofproofs$427
title: Sum of Divisors
description: SUM OF DIVISORS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: divisors,sum,sum of divisors
contributors: bookofproofs

---


---

The **sum of divisors** function `$F:\mathbb N\to\mathbb N$` is an [arithmetic function][bookofproofs$8112], which maps a given number `$n\in\mathbb N,$` `$n > 0$` to the sum of its [divisors][bookofproofs$700]. In the [sum notation][bookofproofs$261], the `$F$` function can be written as `$$F(n):=\sum_{d \mid n}d\quad\quad\forall n > 0.$$`

### Example.

The `$F$` function can be visualized using SageMath. If you click on the evaluate button, you will see the values of `$F(n)$` for `$n=1,\ldots,100.$`

§§§1

---

§§§1
<div class='sage'>
sigmapoints= [(i, sigma(i,1)) for i in range(1,100)]
list_plot(sigmapoints)
</div>
