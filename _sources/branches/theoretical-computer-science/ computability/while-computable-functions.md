layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1184
orderid: 600
parentid: bookofproofs$1179
title: WHILE-Computable Functions
description: WHILE-COMPUTABLE FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: computable,functions,while
contributors: bookofproofs

---


---

A [function][bookofproofs$592] `\(f : \mathbb N^k \to \mathbb N\)` is *WHILE-computable*, if there exists a [unit-cost Random Access Machine][bookofproofs$1179] `\(M\)` with a [finite][bookofproofs$985] [`\(W H I L E\)` program][bookofproofs$1181] `\(P\)`, such that the machine `\(M\)` computes the **output** `\(m\in \mathbb N\)` **for every input** of `\(k\)` natural numbers `\((n_1,\ldots,n_k)\in\mathbb N^k\)`, i.e.

`\[f(n_1,\ldots,n_k)=m\]`

in the following way: Given the initial state of registers of `\(M\)` `\(r_i:=n_i\)` for `\(1\le i\le k\)` and `\(r_i:=0\)` for `\(i > k\)`, `\(M\)` starts the `\(W H I L E\)` program  `\(\mathtt {P}\)` and terminates at a new state such that 
* `\(r_i=n_i\)` for `\(1\le i\le k\)` (i.e. the initial register states remain unchanged), 
* `\(r_{k+1}=m\)` (i.e. the next register contains the output), and 
* `\(r_i=0\)` for `\(i > k + 1\)`.

The set of all WHILE-computable functions is denoted by `\(W H I L E\)`.

The function `\(f : \mathbb N^k \to \mathbb N\)` is *partially WHILE-computable*, if there is a subset `\(S^k\subseteq\mathbb N^k\)`, for which the [restriction][bookofproofs$1170] `\({f|}_{S^k} : \mathbb N^k \to \mathbb N\)` is WHILE-computable and for every input `\((n_1,\ldots,n_k)\in\mathbb N^k\setminus S^k\)` the machine `\(M\)` behaves as follows: Given the initial state of registers of `\(M\)` `\(r_i:=n_i\)` for `\(1\le i\le k\)` and `\(r_i:=0\)` for `\(i > k\)`, `\(M\)` starts the `\(W H I L E\)` program  `\(\mathtt {P}\)` and never terminates. In this case, we set
`\[f(n_1,\ldots,n_k)=\text{undefined}.\]`

The set of all partially WHILE-computable functions is denoted by `\(W H I L E^{part}\)`.
