layout: example
categories: branches,set-theory
nodeid: bookofproofs$8060
orderid: 50
parentid: bookofproofs$8058
title: Examples of Well-founded Relations
description: EXAMPLES OF WELL-FOUNDED RELATIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: examples,founded,relations,well,well founded relation,well-founded relation,well-foundedness,well founded order,well-founded,relations examples
contributors: bookofproofs

---
By definition, [well-founded][bookofproofs$8058] relations can never be [reflexive][bookofproofs$572]. Therefore, for instance, all [partial orders][bookofproofs$576] are not well-founded. However, the definition of well-founded relations is not intuitive, and we want to give some concrete examples in order to get a better understanding of this definition.

---

### Example 1

Every [well-order][bookofproofs$7997] in a [strictly-ordered][bookofproofs$7993] set is a [well-founded][bookofproofs$8058] relation. This follows immediately from the definitions of each of these two concepts. In particular, the strict order "`$<$`" in the well-ordered set of natural numbers `$(\mathbb N, < )$` is well-founded. For instance, the subset `$\{0\}$` has the minimal element `$0,$` since there is no other natural number `$m$` with `$m < 0.$` 

### Example 1a

Please note that if we take the [total order][bookofproofs$6191] `$(\mathbb N, \le)$` then it is a [well-order][bookofproofs$7997] (version for [posets][bookofproofs$576]), but it is not well-founded! For instance, the set `$\{0\}$` contains `$0$` as its [minimum][bookofproofs$7995], but `$0$` is not [minimal][bookofproofs$7995] in `$\{0\}$` since `$0\le 0.$` The [reflexivity][bookofproofs$572] of "`$\le$`" prevents the order to be well-founded! 

### Example 2

The relation `$R\subset\mathbb N\times\mathbb N$` defined by `$nRm:\Leftrightarrow n+1=m$` means a relation in which the natural number `$m$` is the successor of the natural number `$n.$` This relation is well-founded since every non-empty subset of natural numbers contains at least one element `$m$` such that it is _not_ the successor of all of its elements. For instance, the number `$3$` is not a successor of any of the elements of the subset `$\{3,4,5,6\}.$`

### Example 3

Let `$\mathcal P(X)$` be the [power set][bookofproofs$6831] of a given [set][bookofproofs$550] `$X,$` and let `$R\subseteq\mathcal P(X)\times \mathcal P(X)$` be the relation of being a [proper subset][bookofproofs$552] "`$\subset$`", i.e. `$xRy:\Leftrightarrow x\subset y$` is well-founded, since a given non-empty subset `$S\subseteq \mathcal P(X)$` contains at least one set `$x\in S$` such that it is not a proper subset of any other set `$y\in S.$`

### Example 4

The [divisibility][bookofproofs$77] relation `$R$` defined on sets of [natural numbers][bookofproofs$718] defined by `$X:=\{n\in\mathbb N\mid 1 \le n \}$` with `$nRm \Leftrightarrow n\mid m\wedge n\neq m.$` For instance, the non-empty subset `$S\subset X=\{4,5,6,7,8,9,10\}$` contains `$10,9,8,7,6$` as `$R$`-minimal elements, since there is no `$w\in S$` dividing them with `$w|m\wedge w\neq m.$`

### Example 5

The relation `$R$` defined on the set of finite [strings over an alphabet][bookofproofs$708] with a length `$>1$`  by `$nRm \Leftrightarrow n$` is a non-empty substring of `$m$`. For instance, take the alphabet `$\{a,b,c\}$` and build the string `$S=aabc$`. This string has a length `$>2$` and contains `$a,b,c$` as `$R$`-minimal elements since there is no substring of these strings, which is non-empty and is still in `$S.$` 

### Example 6

The relation `$R$` defined on the [Cartesian product][bookofproofs$748] `$X:=\mathbb N × \mathbb N$` of pairs of natural numbers, defined by `$(n_1,n_2)R(m_1, m_2)\Leftrightarrow n_1 < m_1\wedge n_2 < m_2.$` For instance, take the non-empty subset of pairs 
`$$\begin{array}{ccccc}
\vdots&\vdots&\vdots&\vdots&\\
(3,0)&(3,1)&(3,2)&(3,3)&\ldots\\
(2,0)&(2,1)&(2,2)&(2,3)&\ldots\\
(1,0)&(1,1)&(1,2)&(1,3)&\ldots\\
(0,0)&(0,1)&(0,2)&(0,3)&\ldots
\end{array}$$`
has the following `$R$`-minimal elements
`$$\begin{array}{ccccc}
\vdots \\
(3,0) \\
(2,0) \\
(1,0) \\
(0,0)&(0,1)&(0,2)&(0,3)&\ldots
\end{array}$$`

since only those pairs are both: contained in the subset, and there is no other pair comparable to them using the relation `$R$`

### Example 7

The [contained][bookofproofs$8066] relation `$\in_X$` defined on a set `$X$` is well-founded. This follows from the [axiom of foundation][bookofproofs$717]. As a reminder, the axiom postulates 

> "Every non-empty set `$X$` contains an element that is disjoint from X, formally `$\forall X(X\neq\emptyset \Rightarrow\exists (z\in X)X\cap z=\emptyset).$`"

The postulate is equivalent to 

> "There is an element `$z\in X$` and for no other element `$x\in X$` we have `$z\in x.$`"

This is exactly the definition of being a [well-founded relation][bookofproofs$8058], i.e. the axiom of foundation can be interpreted as the following requirement:

> "Every non-empty set `$X$` contains a `$\in$`-minimal element."
