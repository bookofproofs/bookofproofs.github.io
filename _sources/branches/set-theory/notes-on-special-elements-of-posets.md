layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$7996
orderid: 800
parentid: bookofproofs$189
title: Notes on Special Elements of Posets
description: NOTES ON SPECIAL ELEMENTS OF POSETS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$979
keywords: elements,notes,posets,special
contributors: bookofproofs

---


---

### Existence and Uniqueness of Maxima and Minima

Please note that a [maximum or minimum][bookofproofs$7995] of `$S$` do not have to exist. For instance, the chain of integers `$(Z,\ge)$` neither has a maximum, nor a minimum. However, if a maximum or a minimum of `$S$` exist, then they are unique, which follows immediately from their definition. For instance, if `$g$` and `$g'$` were two maxima, then `$g\preceq g'$` and `$g\succeq g'$` would follow by definition. Therefore, `$g'=g,$` and thus `$g$` is unique.

### Greatest vs. Maximal (Smallest vs. Minimal)

Every maximum (minimum) is also a maximal (minimal) element, but not vice versa! This is because a maximal (minimal) element only requires that there is _no_ greater (smaller) element. But a maximum (minimum) requires that it is greater (smaller) or equal to all other elements.

### Greatest vs. Upper Bound (Smallest vs. Lower Bound)

The only difference between a maximum (minimum) `$m$` and an upper (lower) bound `$b$` of a set `$S$` is that `$m$` has to be an element of `$S,$` while the bound `$b$` can also be an element of `$V\setminus S.$` For instance, `$1$` is an upper bound of the set of all [negative real numbers][bookofproofs$1107], but `$1$` is not a negative real number. The same holds for the [infimum and the supremum][bookofproofs$7995]. To take the same example, `$0$` is a supremum of all negative real numbers but it is still not a negative real number. 

### Yet Another Example

Below, a [Hasse diagram][bookofproofs$267] of a simple poset `$V:\{a,b,c,d,e,f,g\}$` is given, in which the elements of the subset `$S=\{a,b,c,d,e\}$` are drawn as dark nodes: 


![maxmin](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/maxmin.png?raw=true)


In this poset, the following observations can be made:
* `$g$` is a maximum of `$V$` and, at the same time, its supremum, and its upper bound 
* `$S$` has no maximum, but `$d$` and `$e$` are maximal in `$S.$`
* `$g,f$` are upper bounds of `$S$`, therefore `$\sup(S)=f.$` 
* `$a$` is a minimum of `$V$` and of `$S.$` It is also a minimal element and an infimum of both sets.
