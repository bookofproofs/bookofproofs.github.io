layout: proof
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$1360
orderid: 100
parentid: bookofproofs$1358
title: 
description:  OF CORRECTNESS Proof of HORNER SCHEME &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1356
keywords: horner,scheme,x^2 + 3,horner scheme,proof
contributors: bookofproofs

---


---

We want to show that the Horner scheme algorithm `\(\mathtt{horner}(n,x,a)\)` correctly calculates the value `\(p(x)\)` of the polynomial over the [field][bookofproofs$557] `\(F\)` (e.g. a [polynomial over the field of complex numbers][bookofproofs$252])

`\[p(z):=a_nz^n + \ldots + a_1z + a_0\quad\quad( * )\]`
at a specific value `\(x\in F\)`,  where `\(a_0,a_1,\ldots,a_n\in F\)` and where the degree of the polynomial is `\(n\)` (i.e. `\(a_n\neq 0\)`). By applying the [axiom of distributivity][bookofproofs$682], we can transform `\(( * )\)` into 
`\[\begin{array}{rcl}
p(z)&=&a_nz^n + \ldots + a_1z + a_0\\
&=&(a_nz+a_{n-1})z^{n-1} + \ldots + a_1z + a_0\\
&=&((a_nz+a_{n-1})z+a_{n-2})z^{n-2} + \ldots + a_1z + a_0\\
&\vdots&\\
&=&((\ldots((a_nz+a_{n-1})z+a_{n-2})z^{n-2} + \ldots)z + a_1)z + a_0\quad\quad( ** )
\end{array}\]`

The formula `\(( * * )\)` shows that by setting

`\[h_n:=a_n,\quad h_k:=h_{k+1}\cdot x + a_k,\quad k=n-1,\ldots,1,0,\]`

we get `\(h_0=p(x)\)`, which proves the correctness of the algorithm.
