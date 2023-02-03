layout: chapter
categories: branches,set-theory
nodeid: bookofproofs$341
orderid: 400
parentid: bookofproofs$185
title: Can Cardinals be Ordered?
description: CAN CARDINALS BE ORDERED? ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577
keywords: can cardinals be ordered,ordered cardinals,order of cardinals
contributors: bookofproofs


---


---

We have defined a [comparison between cardinals][bookofproofs$984] using the sign "`$\le$`" for "lower or equal", like it is used in case of a usual [order relation][bookofproofs$189] between sets. But is it really one? Well, not really, because [cardinalities][bookofproofs$980] are not [sets][bookofproofs$550], they are classes of sets, by definition. However, it is possible to establish the main properties common to all [order relations][bookofproofs$189]:

* [Reflexivity][bookofproofs$572]: Obviously, for every set `$A$` the identity function `$f(a)=a$` for all `$a\in A$` is [injective][bookofproofs$769]. Therefore `$|A|\le|A|.$`
* [Transitivity][bookofproofs$572]: If there are injective functions `$f:A\to B$` and `$g:B\to C,$` then we know that the 
[composition `$g\circ f$` is also is injective][bookofproofs$6864]. Therefore, `$|A|\le|C|$`.
* [Antisymmetry][bookofproofs$575]: By definition of this property and transferred to the case of cardinals, this would mean that if there are injective functions `$f:A\to B$` and `$g:B\to A,$` then `$|A|=|B|$`, i.e. then there is a [bijective function][bookofproofs$771] `$h:A\to B.$`

The last property is known as the [Schröder-Bernstein theorem][bookofproofs$8051], which we will prove soon. Historically, there were many more or less complicated proofs of this theorem, some of them turned out to be wrong. 
The first correct proof was provided by [Richard Dedekind](https://mathshistory.st-andrews.ac.uk/Biographies/Dedekind/) (1831 - 1916).
