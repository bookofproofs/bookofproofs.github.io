layout: definition
categories: branches,number-theory
nodeid: bookofproofs$8115
orderid: 100
parentid: bookofproofs$8113
title: Number of Divisors
description: NUMBER OF DIVISORS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: divisors,number,number of divisors
contributors: bookofproofs

---


---

The **number of divisors** function `$\tau:\mathbb N\to\mathbb N$` is an [arithmetic function][bookofproofs$8112] counting how many [divisors][bookofproofs$700] a given number `$n\in\mathbb N$` has. In the [sum notation][bookofproofs$261] notation, the `$\tau$` function can be written as `$$\tau(n):=\sum_{d \mid n}1\quad\quad\forall n > 0.$$`

### Example.

The `$\tau$` function can be visualized using SageMath. If you click on the evaluate button, you will see the values of `$\tau(n)$` for `$n=1,\ldots,100.$` 

§§§1

---

§§§1
<div class='sage'>
sigmapoints= [(i, sigma(i,0)) for i in range(1,100)]
list_plot(sigmapoints)
</div>
