layout: explanation
categories: branches,combinatorics
nodeid: bookofproofs$1409
orderid: 300
parentid: bookofproofs$209
title: Pascal's Triangle (Triangle of Binomial Coefficients)
description: PASCAL'S TRIANGLE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: pascal's triangle,triangle of binomial coefficients,pascals
contributors: bookofproofs

---


---

The numbers formed by [binomial coefficients][bookofproofs$993] `\(\binom nk\)`, where `\(n\)` and `\(k\)` are natural numbers form a scheme, named the *Pascal's triangle*[^1]. The beginning of Pascal's triangle (for `\(11\le n,k\le 0\)`) is shown in the following table:

`\[\begin{array}{r|rrrrrrrrrrr}
n&\binom n0&\binom n1&\binom n2&\binom n3&\binom n4&\binom n5&\binom n6&\binom n7&\binom n8&\binom n9&\binom n{10}&\binom n{11}\\
\hline
0&1\\
1&1&1&\\
2&1&2&1&\\
3&1&3&3&1&\\
4&1&4&6&4&1\\
5&1&5&10&10&5&1\\
6&1&6&15&20&15&6&1\\
7&1&7&21&35&35&21&7&1\\
8&1&8&28&56&70&56&28&8&1\\
9&1&9&36&84&126&126&84&36&9&1\\
10&1&10&45&120&210&252&210&120&45&10&1\\
11&1&11&55&165&330&462&462&330&165&55&11&1\\
\end{array}\]`  

Note that empty entries in this table are actually `\(0\)`'s. This is because the numerator in the [closed formula for binomial coefficients][bookofproofs$1400] is zero if `\(n < k\)` 
`\[\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k(k-1)\cdots 2\cdot 1},\]`
e.g. `\(\binom 23=(1\cdot 0\cdot (-1))/(3\cdot 2\cdot 1)=0\)`. The `\(0\)` entries have been left blank to help emphasize the rest of the table. 


[^1]: named after Blaise Pascal (1623-1662)
