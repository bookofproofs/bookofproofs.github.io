layout: proof
categories: branches,theoretical-computer-science, complexity-theory
nodeid: bookofproofs$1168
orderid: 50
parentid: bookofproofs$1167
title: 
description:  Proof of CALCULATION RULES FOR THE BIG O NOTATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: big,calculation,notation,rules,proof
contributors: bookofproofs

---


---

Let `\(g,f\)`, be two functions of natural numbers to real numbers and let c be a real number, formally `\(g,f:\mathbb N\mapsto\mathbb R\)`, `\(c\in\mathbb R\)`. 

According to the [definition of the big `\(\mathcal O\)`-Notation][bookofproofs$1087], we have `\(f=\mathcal O(g)\)` if and only if there is a positive constant `\(c\in\mathbb R_+\)` such that for all sufficiently large `\(n\in\mathbb N\)`, i.e. all `\(n \ge N( c )\)` we have `\(|f(n)|\le c|g(n)|\)`.

### `\((1)\)` Proof of `\(f=\mathcal O(f)\)`

This is trivially fulfilled, since  for `\(c=1\)` we have `\(|f(n)|\le 1|f(n)|\)` for all `\(n\ge N(1)\)`. 

### `\((2)\)` Proof of `\(c\cdot \mathcal O(f)=\mathcal O(f)\)` for any `\(c > 0\)`.

`\(\mathcal O(f)\)` denotes the class of all functions `\(g:\mathbb N\mapsto\mathbb R\)` such that there exist constants `\(b > 0\)` and `\(N(b)\in\mathbb N\)`, for which `\(|g(n)|\le b\cdot|f(n)|\)` for all `\(n\ge N(b)\)`. 

Thus, for a fixed `\(c > 0\)`, `\(c\cdot \mathcal O(f)\)` denotes a class of all functions `\(g:\mathbb N\mapsto\mathbb R\)` such that there exist constants `\(b > 0\)` and `\(N(b)\in\mathbb N\)`, for which `\(c\cdot |g(n)|\le c\cdot b\cdot|f(n)|\)` for all `\(n\ge N(b)\)`. 

In other words, `\(c\cdot \mathcal O(f)\)` is the class of all functions `\(h(n):=c\cdot g(n)\)`, such that there exist the constants `\(d:=c\cdot b > 0\)` and `\(N(d)\in \mathbb N\)`, for which `\(|h(n)|\le d\cdot|f(n)|\)` for all `\(n\ge N(d)\)`. But this means  `\(c\cdot \mathcal O(f)=\mathcal O(f)\)`.

 
### `\((3)\)` Proof of `\(\mathcal O(\mathcal O(f))=\mathcal O(f)\)`

We have to show: If `\(g=\mathcal O(f)\)`, then `\(\mathcal O(g)=\mathcal O(f)\)`. 

Let `\(g=\mathcal O(f)\)`, which means that there exist constants `\(b > 0\)` and `\(N(b)\in\mathbb N\)`, for which `\(|g(n)|\le b\cdot|f(n)|\)` for all `\(n\ge N(b)\)`.

For any function `\(h=\mathcal O(g)\)`, there exist constants `\(c > 0\)` and `\(N( c )\in\mathbb N\)`, for which `\(|h(n)|\le c\cdot|g(n)|\)` for all `\(n\ge N(  c )\)`.

Combining both results, we get for the constant `\(d:=c\cdot b\)` that `\(|h(n)|\le c\cdot|g(n)|\le c\cdot b\cdot|f(n)|=d\cdot|f(n)|\)` for all `\(n\ge N(d):=\max(N( c ), N(b))\)`. This means that `\(\mathcal O(\mathcal O(f))=\mathcal O(f)\)`.

### `\((4)\)` Proof of `\(\mathcal O(f)\cdot \mathcal O(g)=\mathcal O(f\cdot g)\)`

We have to show that if `\(h_1=\mathcal O(f)\)` and `\(h_2=\mathcal O(g)\)`, then `\(h_1\cdot h_2=\mathcal O(f\cdot g)\)`.

`\(h_1=\mathcal O(f)\)` means that there exist constants `\(c_1 > 0\)` and `\(N(c_1)\in\mathbb N\)`, for which `\(|h_1(n)|\le c_1\cdot|f(n)|\)` for all `\(n\ge N(c_1)\)`.

`\(h_2=\mathcal O(g)\)` means that there exist constants `\(c_2 > 0\)` and `\(N(c_2)\in\mathbb N\)`, for which `\(|h_2(n)|\le c_2\cdot|g(n)|\)` for all `\(n\ge N(c_2)\)`.

Combining both results, we have `\(|(h_1\cdot h_2)(n)|=|h_1(n)|\cdot|h_2(n)|\le c_1|f(n)|\cdot c_2|g(n)|=c_3|(f\cdot g)(n)|\)` for the constant `\(c_3:=c_1\cdot c_2 > 0\)` and all `\(n\ge N(c_3):=max (N(c_1),N(c_2))\)`. This means that `\(\mathcal O(f)\cdot \mathcal O(g)=\mathcal O(f\cdot g)\)`.

### `\((5)\)` Proof of `\(\mathcal O(f\cdot g)=|f|\cdot  \mathcal O(g)\)`

We have to show that if `\(h_1=\mathcal O(f\cdot g)\)`, then there exist constants `\(c > 0\)` and `\(N( c )\in\mathbb N\)` such that `\(h_1(n)\le |f(n)|\cdot c\cdot |g(n)|\)` for all `\(n\ge N( c )\)`.

`\(h_1=\mathcal O(f\cdot g)\)` means that there exist constants `\(c_1 > 0\)` and `\(N(c_1)\in\mathbb N\)`, for which `\(|h_1(n)|\le c_1\cdot|f(n)|\cdot |g(n)|\)` for all `\(n\ge N(c_1)\)`.

`\(h_2=\mathcal  |f|\cdot O(g)\)` means that there exist constants `\(c_2 > 0\)` and `\(N(c_2)\in\mathbb N\)`, for which `\(|h_2(n)|\le |f(n)|\cdot c_2\cdot|g(n)|\)` for all `\(n\ge N(c_2)\)`.

Both conditions are the same, considering the commutativity of multiplication and setting `\(c_2:=c_1\)`.

### `\((6)\)` Proof of `\(|f|\le |g|\Rightarrow\mathcal O(f)= \mathcal O(g)\)`

`\(\mathcal O(f)\)` denotes the class of all functions `\(h_1:\mathbb N\mapsto\mathbb R\)` such that there exist constants `\(c_1 > 0\)` and `\(N(c_1)\in\mathbb N\)`, for which `\(|h_1(n)|\le c_1\cdot|f(n)|\)` for all `\(n\ge N(c_1)\)`. 

Correspondingly, `\(\mathcal O(g)\)` denotes the class of all functions `\(h_2:\mathbb N\mapsto\mathbb R\)` such that there exist constants `\(c_2 > 0\)` and `\(N(c_2)\in\mathbb N\)`, for which `\(|h_2(n)|\le c_2\cdot|f(n)|\)` for all `\(n\ge N(c_2)\)`. 

If `\(f(n)\le g(n)\)` for all `\(n\in\mathbb N\)`, then `\(|h_2(n)|\le c_2\cdot|f(n)|\le c_2\cdot|g(n)|\)` for all `\(n\ge N(c_2)\)`. This means that `\(|f|\le |g|\Rightarrow\mathcal O(f)= \mathcal O(g)\)`.
