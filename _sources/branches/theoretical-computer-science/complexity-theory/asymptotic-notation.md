layout: section
categories: branches,theoretical-computer-science, complexity-theory
nodeid: bookofproofs$203
orderid: 50
parentid: bookofproofs$133
title: Asymptotic Notation
description: ASYMPTOTIC NOTATION &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: asymptotic,asymptotic notation,notation
contributors: bookofproofs

---


---

Measuring the time a computer needs to perform an algorithm (a computer program or a calculation) would be one method of estimating the complexity of this calculation. However, this method would not be the best. Why? Because the time measured would to a great extend depend on how fast the computer is. Performing the same calculation on two different computers (e.g. with two different processor chips) would result in different times measured. The measurements would reflect the speed of the processor chips, but would have no meaning with respect to the complexity of the calculation we originally wanted to measure. 

There is a better method of measuring the complexity of algorithms (and not the speed of computers). The complexity (or running "time") depends solely on the input number `\(n\)` to the specific algorithm. In other words and more formally speaking, the "time" to be measured is an unknown function `\(f(n)\)` which has to be estimated. 

The **asymptotic notation** (sometimes also called the *big `\(\mathcal O\)` notation*) is used in theoretical computer science in order to estimate the __worst case__ running time of an algorithm. If we know the worst case and can express this worst case by a more simple function `\(g(n)\)`, we can write `\[f=\mathcal O(g)\]` and mean by that the unknown function `\(f(n)\)` we wanted to estimate grows at most as fast as the known function `\(g(n)\)`, depending on the input number `\(n\)`.
