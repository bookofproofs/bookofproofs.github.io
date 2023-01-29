layout: motivation
categories: branches,set-theory
nodeid: bookofproofs$726
orderid: 200
parentid: bookofproofs$8079
title: Observation 1: The Mostowski Function Produces Transitive Sets
description: OBSERVATION 1: THE MOSTOWSKI FUNCTION PRODUCES TRANSITIVE SETS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$656
keywords: mostowski function,transitive sets,transitive set,transitive set example,transitive function
contributors: bookofproofs


---
The [initial example][bookofproofs$8080], as well as the [other examples][bookofproofs$8082] show that the [Mostowski function][bookofproofs$8079] creates very different results on an ordered set `$(X,\preceq),$` depending on the underlying [well-founded][bookofproofs$8058] relation `$"\preceq".$` We want to make some observations, which will motivate a theorem of [Mostowski][mo].

[mo][https://mathshistory.st-andrews.ac.uk/Biographies/Mostowski/]
---

Please note that in all four examples, the resulting Mostowski collapse `$\pi([X])$` is a [transitive set][bookofproofs$720], i.e. if `$x\in y$` and `$y\in\pi([X])$`, then `$x\in \pi([X]).$`


### Ad Example 1  

The Mostowski collapse was here the "von Neumann":https://www.bookofproofs.org/history/john-von-neumann/ set 

`$$\pi[\mathbb N]=\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\},\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\},\ldots \}.\quad ( * )$$`
 
To see that this set is indeed transitive, note that all elements of this set obey a special construction principle: Starting with the empty set `$\emptyset,$` the next set in the series after is `\(\emptyset \cup \{\emptyset\}.\)`, and the specific construction principle `\(X\cup \{X\}\)` is repeated at every new element. We have [already proven][bookofproofs$721] that `\(X\cup \{X\}\)` is transitive if `\(X\)` was. Since `$\emptyset$` is transitive, by induction, the whole Mostowski collapse `$( * )$` must be transitive. Moreover, even _every element_ of the set `$( * )$` is itself a transitive set.

### Ad Example 2

The Mostowski collapse was here the set 

`$$\pi[\mathbb N]=\{\emptyset,\{\emptyset\},\{\{\emptyset\}\},\{\{\{\emptyset\}\}\},\ldots \}.\quad ( * * )$$`

In contrast to the first example, in this set only the first two elements `$\emptyset$` and `$\{\emptyset\}$` are transitive, all other are not. But the Mostowski collapse `$( * * )$` as a whole is transitive. In fact, we can combine any first `\(n\)` elements into new sets according to the following rule: `\[T_0:=X_0,~T_n:=\bigcup_{0\le k\le n} X_k\]` to produce transtive sets:


![axiom8_2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom8_2.jpg?raw=true)


Now, for any `\(T_n\)` we have then: If `\(X_k\in T_n\)` for `\(1\le k\le n\)`, then by definition `\(X_k=\{X_{k-1}\}\)`. However, `\(\{X_{k-1}\}\)` is a subset of `\(T_n\)`, so `\(T_n\)` is transitive.

### Ad Example 3 and Example 4

The two Mostowski collapses in the examples were the sets  

`$$\pi[\mathcal P(\{a,b,c\})]=\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\},\{\emptyset, \{\emptyset\}\}\}\}$$`

and 

`$$\pi[X_k]=\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\}\quad\forall k.$$`

These sets are transitive since they are the first elements of the von Neumann set in Example 1.
