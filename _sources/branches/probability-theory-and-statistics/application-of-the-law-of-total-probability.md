layout: solution
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1830
orderid: 50
parentid: bookofproofs$1829
title: Application of the Law of Total Probability
description: Solution of  &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: application,law,probability,total
contributors: bookofproofs

---


---

We define the events

> `\(A:="\text{The first item drawn is not broken}"\)`

> `\(B:="\text{The second item drawn is not broken}"\)`

Because we have a [Laplace experiment][bookofproofs$973], the probabilities of `\(A\)` and `\(\overline{A}\)` are

`\[p(A)=\frac {10-4}{10}=\frac 35;\quad\quad p(\overline{A})=1-p(A)=\frac 25.\]`

Because the drawing is without replacement, the probabilities of `\(B\)` given `\(A\)` and `\(\overline{A}\)` are

`\[p(B|A)=\frac {9-4}{9}=\frac 59;\quad\quad p(B|\overline{A})=\frac {9-3}{9}=\frac 69=\frac 23.\]`

Note that the events `\(A\)` and `\(\overline{A}\)` are [mutually exclusive and collectively exhaustive][bookofproofs$859]. It follows that we can apply the [law of total probability][bookofproofs$449] and calculate the probability of `\(B\)`:

`\[p(B)=p(B|A)p(A)+ p(B|\overline{A})p(\overline{A})=\frac 56\cdot \frac 35+\frac 23\cdot \frac 25=\frac{27}{45}=\frac 35.\]`

It turns out that the events `\(A\)` and `\(B\)` have the same probability.
