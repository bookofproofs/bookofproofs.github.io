layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1490
orderid: 50
parentid: bookofproofs$1489
title: 
description:  Proof of RATIONAL CAUCHY SEQUENCE MEMBERS ARE BOUNDED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: are,bounded,cauchy,members,rational,sequence,proof
contributors: bookofproofs

---


---

We have to show that the rational members `\(a_n\)` of any given [rational Cauchy sequence][bookofproofs$1485] `\((a_n)_{n\in\mathbb N}\)` are bounded, i.e. there exists a positive constant `\(c\in\mathbb Q\)`, such that `\(|a_n|\le c\)` for all `\(n\in\mathbb N\)`. 

By definition of rational Cauchy sequences, for any rational number `\(\epsilon > 0\)` we have `\(|a_i-a_j| < \epsilon\)` for all `\(i,j\ge N(\epsilon)\)`. In particular, if we choose `\(\epsilon=1\)`, there is an index `\(N\in\mathbb N\)` for which the [absolute value][bookofproofs$1081] of the [difference][bookofproofs$1446] `\(|a_n-a_m|\)` becomes smaller than `\(1\)` for all `\(m,n > N\)`.

Now, we consider all `\(a_m\)` with the index `\(m=N+1\)`. Using the [triangle property of the absolute value][bookofproofs$1081],  we get 

`\[|a_n|=|a_n-a_m+a_m|\le |a_n-a_m|+|a_m| < 1+ |a_m|\quad\quad\text{for all }n > N.\]`
Set `\(c:=\max(|a_1|,\ldots,|a_{N}|,1+|a_m|)\)`. By construction, the constant `\(c\)` gives us the required result  
`\[|a_n|\le c\quad\quad\text{for all }n\in\mathbb N.\]`
