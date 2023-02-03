layout: part
categories: branches,analysis
nodeid: bookofproofs$28
orderid: 100
parentid: bookofproofs$47
title: Real Analysis of One Variable and Elements of Complex Analysis
description: REAL ANALYSIS OF ONE VARIABLE AND ELEMENTS OF COMPLEX ANALYSIS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: real analysis of one variable,elements of complex analysis
contributors: bookofproofs


---


---

This part of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong> deals with the analysis of real-valued (and whenever applicable also complex-valued) functions with one variable, i.e. the functions of the form `$f:\mathbb R\mapsto \mathbb R$` or `$f:\mathbb C\mapsto \mathbb C,$` `$x\mapsto f(x)$`. 
Using the [axiomatic method][bookofproofs$7081], it systematically derives some basic concepts like [sequences and limits][bookofproofs$101], [infinite series][bookofproofs$142], and basic properties of functions. 

Although there is another part dedicated solely to complex analysis, in which you can find deeper results applicable for complex numbers only, there are lots of concepts that are applicable for both, [real][bookofproofs$1105] ($\mathbb R$) and [complex][bookofproofs$216] ($\mathbb C$) numbers, or even [rational numbers][bookofproofs$1033] ($\mathbb Q$), [integers][bookofproofs$844] ($\mathbb Z$) or [natural numbers][bookofproofs$718] ($\mathbb N$). In order to avoid unnecessary repetition of basic concepts, we will introduce them only once in this part. Whenever a theorem or definition can be used in the domain of the respective number system, we will use a marker 

> applicability: `$\mathbb {N, Z, Q, R , C}$`

listing all number system, it s applicable to.

### Prerequisites to start learning calculus of one variable

Before you start further reading, you should be familiar / revise your knowledge about the following areas:

* [Sets][bookofproofs$550] and their properties, including set manipulation (e.g. [union][bookofproofs$6827], [intersection][bookofproofs$6828], [difference][bookofproofs$6830]),
* [Functions][bookofproofs$592] and their [composition][bookofproofs$1314],
* [Methods of mathematical proving][bookofproofs$184], in particular, the [proving principle of induction][bookofproofs$657],
* [Sums][bookofproofs$261] and [methods of their manipulation][bookofproofs$1113],
* The sets of different [number systems][bookofproofs$195], including [natural numbers][bookofproofs$718], `$\mathbb N$`,  [integers][bookofproofs$844] `$\mathbb Z$`, [rational numbers][bookofproofs$1033] `$\mathbb Q$`, and, last but not least, [real numbers][bookofproofs$1105] `$\mathbb R$`, which are the most important mathematical objects we will be dealing with in this part of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>. 

### Theoretical minimum (in a nutshell)

Ideally, you should be already acquainted with the following facts:

* There are two basic operations defined for the real numbers `$\mathbb R$`, i.e. the [addition][bookofproofs$1514] "`$+$`" and the [multiplication][bookofproofs$1532] "`$\cdot$`". 
* Together with these two operations, the real numbers form an algebraic structure `$(\mathbb R, +,\cdot)$`, called the [field of real numbers][bookofproofs$1638]. In a nutshell, this means that all calculations involving real numbers, let's call them `$x,y,z\in\mathbb R$`, obey the following rules:
   * The addition is _associative_ `$(x+y)+z=x+(y+z)$` and _commutative_ `$x+y=y+x$`.
   * The multiplication is _associative_ `$(x\cdot y)\cdot z=x\cdot (y\cdot z)$` and _commutative_ `$x\cdot y=y\cdot x$`.
   * There is a unique real number, called _zero_ and denoted by `$0$`, which is neutral with respect to addition: `$x+0=0+x=x$` for all `$x\in\mathbb R$`. 
   * There is a unique real number, called _one_ and denoted by `$1$`, which is neutral with respect to multiplication: `$x\cdot 1=1\cdot x=x$` for all `$x\in\mathbb R$`.
   * Each real number `$x$` has a unique _additive inverse_ `$-x$`, also called its _negative_, for which we have that `$x-x:=x+(-x)=0$`. In fact, this is how the [subtraction of real numbers][bookofproofs$1588] "$-$" is defined.
   * Each real number `$x\neq 0$` has a unique _multiplicative inverse_ `$x^{-1}=\frac 1x$`, also called its _reciprocal_, for which we have that `$x\div x:=x\cdot \frac 1x=1$`. In fact, this is how the [division of real numbers][bookofproofs$6635] "$\div `$"is defined.
   * When calculations involve both, the multiplication and addition, then the _distributivity laws_ hold: `$x(y+z)=xy+xz$` and `$(x+y)z=xz+yz.$`[^1]
* You should know some basic results following from the field properties of real numbers, including:
   * `$-0=0$` ([proof][bookofproofs$502]).
   * `$-(-x)=x$` for all `$x\in\mathbb R$` ([proof][bookofproofs$526]), and other [rules for the multiplication of positive and negative numbers][bookofproofs$1598].
   * `$x\cdot 0=0\cdot x=0$` for all  `$x\in\mathbb R$` ([proof][bookofproofs$527]).
   * `$xy=0$` holds if and only if `$x=0$` or `$y=0$` (or both, [proof][bookofproofs$529]).
   * `$-(x+y)=-x-y$` ([proof][bookofproofs$537]).
   * The equality `$a+x = b$` with the variable `$x$` has exatly one solution: `$b-a$` ([proof][bookofproofs$518]).
   * The equality `$ax = b$` with the variable `$x$` and `$a\neq 0$` has exatly one solution: `$\frac ba$` ([proof][bookofproofs$519]).
   * `$\frac 1{xy}=\frac 1x\cdot \frac 1y$` for all  `$x,y\in\mathbb R$` ([proof][bookofproofs$538])
* Basically, the same rules apply for [complex numbers][bookofproofs$6788] `$\mathbb C$` with the operations [addition][bookofproofs$1657] "`$+$`" and the [multiplication][bookofproofs$1668] "`$\cdot$`". 
* Any two real numbers `$x,y\in\mathbb R$` can be ordered using the [order relation][bookofproofs$1107] "`$\le$`" . This relation is [strict and total][bookofproofs$7834], i.e. only one of the following situations can be true (this is known as the _trichotomy property_): Either `$x < y$`, or `$x=y$`, or `$x > y$`. 
* The above order relation is transitive, i.e. if `$x \le y$` and `$y \le z$`, then `$x \le z$`.
* You should know some basic results for the [calculation with inequalities][bookofproofs$594].
* You should know that complex numbers cannot be ordered. 

### Concepts you will learn in this part of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>

* Why are real numbers not _countable_ while rational numbers are?
* What are real intervals and is the difference between open and closed intervals?
* Why we need yet another axiom (the _Archimedean axiom_) to fully describe the set `$\mathbb R$` of real numbers? 
* Absolute values of real and complex numbers and their properties
* What are _sequences of numbers_ and what does it mean to _converge_ and to _absolutely converge_ against a _limit_?
* What are _Cauchy sequences_ and why the sets of real numbers `$\mathbb R$` and complex numbers `$\mathbb C$` are said to _be complete_?
* You will learn about different types of real (and sometimes also complex) functions, e.g. including _polynomials_, _rational functions_, _nth powers_, the _logarithm_, and the _exponential_ function,  _trigonometric functions_
* You will learn which properties real functions might have, including being _bounded_, _continuous_, _monotonic_,  _differentiable_, _integrable_, etc.
* What are the different types of real infinite series and their properties, including their _convergence behaviour_, the _power_, _Taylor_, and _Fourier_ series
* You will learn the _fundamental theorem of calculus_ and its various applications.

[^1]: Here, we have used a short notation for multiplication, omitting the dot "$\cdot$". Note that the distributity laws cover subtraction as a special case of addition: `$x(y-z)=xy-xz$` and `$(x-y)z=xz-yz$`. However, they only sometimes cover division as a special case of multiplication: Although we have `$(x+y)\div z=x\div z+y\div z$`, for `$z\neq 0$`, in general we have  `$x\div (y+z)\neq x\div y+x\div z$` for `$(y+z)\neq 0$`. This is because the multiplicative inverse element of `$(y+z)$` equals `$\frac 1{y+z}$`, and does not equal `$\frac 1 y+\frac 1z$` (which is `$\frac{z+y}{yz}$` rather than `$\frac 1{y+z}$`).
