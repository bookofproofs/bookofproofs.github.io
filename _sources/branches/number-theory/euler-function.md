layout: definition
categories: branches,number-theory
nodeid: bookofproofs$8117
orderid: 300
parentid: bookofproofs$8113
title: Euler function
description: EULER FUNCTION ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: euler,function,euler function
contributors: bookofproofs


---


---

The **Euler** function `$\phi:\mathbb N\to\mathbb N$` is an [arithmetic function][bookofproofs$8112] `$\phi(n)$` counts how many numbers in the [subset][bookofproofs$552] of [natural numbers][bookofproofs$718] `$\{1,2,\ldots,n\}$` are [co-prime][bookofproofs$8093] to `$n.$`  

### Example.

The `$\phi$` function was first described by "Leonhard Euler":https://www.bookofproofs.org/history/leonhard-euler/ (1707 - 1783). It can be visualized using SageMath. If you click on the evaluate button, you will see the values of `$\tau(n)$` for `$n=1,\ldots,100.$` 

§§§1

---

§§§1
<div class='sage'>
phipoints= [(i, euler_phi(i)) for i in range(1,100)]
list_plot(phipoints)
</div>
