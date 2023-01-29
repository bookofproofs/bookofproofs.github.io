layout: definition
categories: branches,set-theory
nodeid: bookofproofs$748
orderid: 200
parentid: bookofproofs$63
title: Cartesian Product
description: CARTESIAN PRODUCT &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: cartesian,cartesian product,product
contributors: bookofproofs


---
The [set-theoretical meaning of ordered tuples][bookofproofs$8042] shows that being an `$n$`-tuple is a [predicate of a logical calculus][bookofproofs$6226]. Therefore, we can use the [axiom of separation][bookofproofs$675] to define what today's mathematicians call the _Cartesian product._ "René Descartes (1596 - 1650)":https://www.bookofproofs.org/history/rene-descartes/ invented this concept in the 17th century, long before the set theory was born in its strict form but with our new set-theoretical tools we can provide a foundation for this concept:

---

Let `\(A_1\ldots A_n\)` be [sets][bookofproofs$550]. Using the [set-theoretical meaning of ordered tuples][bookofproofs$8042] and the [axiom of separation][bookofproofs$675] we define the set 
`\[A_1\times A_2\times\cdots\times A_n :=\{(x_1,\ldots,x_n)\mid x_i\in A_i, 1\le i\le n\}.\]` 
as the **Cartesian product** of the sets `\(A_1\ldots A_n\)`. In other words, the Cartesian product is the set of [ordered `\(n\)`-tuples][bookofproofs$747] `\((a_1,a_2,\ldots,a_n)\)`, such that `\(a_i\in A_i\)` for `$i=1,\ldots,n.$`[^1].

If all of the `\(A_i\)` denote the same set `\(A\)`, then we use the short form

`\[A^n:=\underbrace{A\times A\times\cdots\times A}_{n\text{ times}}.\]`  

[^1]: Please note that, in general, the Cartesian product is not commutative, i.e. `\(A\times B\neq B\times A\)`, because of the order or the elements would change, in contradiction to the definition of ordered tuples.
