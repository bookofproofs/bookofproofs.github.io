layout: explanation
categories: branches,combinatorics
nodeid: bookofproofs$8302
orderid: 300
parentid: bookofproofs$264
title: Connection Between the Cartesian Product and Functions Mapping Finite Sets into a Non-empty Set
description: CONNECTION BETWEEN THE CARTESIAN PRODUCT AND FUNCTIONS MAPPING FINITE SETS INTO A NON-EMPTY SET &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: 
keywords: cartesian product, functions mapping sets into a given set
contributors: bookofproofs

---


---

Now, we want to reverse the question and ask for the number of different [maps][bookofproofs$592] of a [finite set][bookofproofs$985], say with two elements `$\{a,b\},$` into an arbitrary, [non-empty set][bookofproofs$550] `$X$`, i.e. `$f:\{a,b\}\to X$`? How many possible maps of this kind are there? In order to answer this question, observe that a given `$f$` assigns uniquely `$a\to f(a)$` and `$b\to f(b),$` where `$x:=f(a)$` and `$y:=f(b)$` are some unique two elements of `$x,y\in X.$` In the [set theory][bookofproofs$27], this is called an [ordered pair][bookofproofs$747] `$(x,y).$` Such an ordered pair is an element of the [Cartesian product][bookofproofs$748] `$X\times X.$` Vice versa, any given ordered pair `$(x,y)\in X\times X$` uniquely determines a map `$f$` by defining `$f(a):=x$` and `$f(b):=y.$` 

Therefore, there is a one-to-one correspondence between maps of [finite sets][bookofproofs$985] with `$n$` elements into a given non-empty set `$X.$` This connection is summarized in the following proposition:
