layout: definition
categories: branches,set-theory
nodeid: bookofproofs$747
orderid: 50
parentid: bookofproofs$63
title: Ordered Pair, n-Tuple
description: ORDERED PAIR, N-TUPLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: -tuple,ordered,ordered pair,pair,tuple,ordered tuple,ordered pairs set theory,ordered pair definition,ordered n tuple,n tuple,n-tuples,n-tuple,n-tuple definition,ordered n-tuples,ordered n-tuple
contributors: bookofproofs


---
In order to define what it means to have a relation between sets elements, we have to provide a strict set-theoretical idea of putting the elements in a specific order. For instance, if we want to relate two elements with each other, we want to speak about "the first" (or "the left") and "the second" (or "the right") element. This leads us to the concept of an _ordered pair_. A strict, purely set-theoretical definition was first proposed by [Kazimierz Kuratowski][kk]:

[kk]:https://mathshistory.st-andrews.ac.uk/Biographies/Kuratowski/
---

Let `\(X\)` be a [set][bookofproofs$550] and for `$n\ge 1$`, `$i=1,\ldots n$` let `\(x_i\in X\)` be some of its elements. 

We set for `$n=1$` the **tuple** `$(x_1)$` to be the [singleton][bookofproofs$8034]:

`\[\begin{array}{rcl}
(x_1)&:=&\{x_1\}
\end{array}\]`


We define the **ordered pair** as

`\[\begin{array}{rcl}
(x_1,x_2)&:=&\{\{x_1,x_2\},\{x_1\}\}
\end{array}\]`

and in general, for `$n > 2$` we set recursively the *ordered `\(n\)`-tuple* (or just *`\(n\)`-tuple*) `$(x_1,\ldots,x_n)$` recursively as the ordered pair of `$(x_1,\ldots,x_{n-1})$` and `$x_n$`, formally

`\[\begin{array}{rcl}
(x_1,\ldots,x_n)&:=&((x_1,\ldots,x_{n-1}),x_n)\end{array}.\]`

We denote `\(x_i\)` as the `\(i\)`-th element of the *$n$-tuple*.

### Notes

* Occasionally, `$n$`-tuples are also called lists.
* Sometimes, objects denoted by `$(x_1,x_2,\ldots)$` might be said to have infinite length. By definition, an `$n$`-tuple has a finite length and such objects are not `$n$`-tuples.
* `$n$`-tuples differ from sets, since order matters and repetitions have meaning, while in sets, order and repetition are not important.
