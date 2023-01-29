layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1525
orderid: 50
parentid: bookofproofs$1524
title: 
description:  Proof of CONVERGENT RATIONAL SEQUENCES WITH LIMIT \0\ ARE AN IDEAL OF THE RING OF RATIONAL CAUCHY SEQUENCES &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$696
keywords: are,cauchy,convergent,ideal,limit,rational,ring,sequences,proof
contributors: bookofproofs

---


---

We want to show that the set `\(I:=\{(a_n)_{n\in\mathbb N}~|~a_n\in\mathbb Q,\lim a_n=0\}\)` of all [rational sequences convergent][bookofproofs$1572] to `\(0\)` is an [ideal][bookofproofs$1062] of the  [commutative unit ring of all rational Cauchy sequences][bookofproofs$1101] `\((M , + , \cdot)\)`, formally `\(I\lhd R\)`.

We will do so by proving all properties of an ideal:

### `\((1)\)` It has been proven already that `\((I, +)\)` is a [subgroup][bookofproofs$1522] of `\((M , +)\)`.

### `\((2)\)` We want to show that `\((c_n)_{n\in\mathbb N}\in M,~(a_n)_{n\in\mathbb N}\in I\Longrightarrow (c_n\cdot a_n)_{n\in\mathbb N}\in I.\)`

It [has been shown][bookofproofs$1489] that given a rational Cauchy sequence `\((c_n)_{n\in\mathbb N}\)`, the members `\(c_n\)` are bounded, i.e. there exists a positive constant `\(c > 0, c\in\mathbb Q\)`, such that `\(|c_n|\le c\)` for all `\(n\in\mathbb N\)`. By hypothesis, `\((a_n)\in I\)` is a rational sequence convergent to `\(0\)`. Thus, we can choose any arbitrarily small `\(\epsilon\in\mathbb Q,\epsilon  > 0\)`, and conclude that there exists an `\(N(\epsilon/c)\in\mathbb N\)` such that for all `\(n > N(\epsilon/c)\)` we have the estimation
`\[|c_n\cdot a_n|=|c_n|\cdot|a_n|\le c\cdot \frac\epsilon c=\epsilon.\]`
This shows that a right-product of a rational Cauchy sequence `\((c_n)_{n\in\mathbb N}\)` and a rational sequence `\((a_n)_{n\in\mathbb N}\)` convergent to `\(0\)` is a sequence `\((c_n\cdot a_n)_{n\in\mathbb N}\)`, which also converges to `\(0\)`, or equivalently an element of `\(I\)`.
 
### `\((3)\)` We want to show that `\((c_n)_{n\in\mathbb N}\in M,~(a_n)_{n\in\mathbb N}\in I\Longrightarrow (a_n\cdot c_n)_{n\in\mathbb N}\in I.\)`

This can be concluded immediately from `\((2)\)`, since `\((M, + ,\cdot)\)` is a commutative ring by hypothesis. 

This demonstrates altogether that `\(I\)` is an ideal of `\((M, + ,\cdot)\)`.
