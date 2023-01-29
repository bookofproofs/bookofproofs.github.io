layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1820
orderid: 50
parentid: bookofproofs$1819
title: 
description:  Proof of MULTINOMIAL COEFFICIENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1209
keywords: multinomial coefficient,multinomial coefficients,multinomial coefficient proof,multinomial theorem example,proof
contributors: bookofproofs

---


---

The number of possible arrangements of `\(n\)` objects is given by the [factorial][bookofproofs$1005] `\(n !\)`. By hypothesis, each of the `\(k_i\)` objects in each of the `\(m\)` different types (with `\(k_1+k_2+\ldots+k_m=n\)`) are indistinguishable. Therefore, in any of the `\(n !\)` different arrangements of `\(n\)` objects, there are `\(k_i !\)` indistinguishable arrangements of objects of the type `\(i\)` for `\(i=1,\ldots,m\)`. By the [fundamental counting principle][bookofproofs$111], there are 
`\(k_1 !k_2 !\cdot\ldots\cdot k_m !\)` indistinguishable arrangements in total. It follows that the number of distinguishable arrangements of `\(n\)` objects of `\(m\)` given types with `\(k_i\)` objects in each type can be calculated by the formula
`\[\frac{n !}{k_1 !k_2 !\cdot\ldots \cdot k_m !}.\]`
