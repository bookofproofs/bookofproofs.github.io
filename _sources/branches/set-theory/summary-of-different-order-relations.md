layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$7994
orderid: 500
parentid: bookofproofs$189
title: Summary of Different Order Relations
description: SUMMARY OF DIFFERENT ORDER RELATIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979
keywords: different,equal,greater,greater or equal,incomparable,less,less or equal,order,relations,summary
contributors: bookofproofs


---


---

We have learned three different possibilities of order relations "`$\prec$`" on a set `$V$`, all using the same notation `$(V,\prec)$`. We now want to recap all definitions again and compare them with each other. The following table summarizes the key differences:



Partial order | Total (Linear) Order  | Strict Total Order
:------------- |:------------- |:-------------
 [Poset][bookofproofs$576]| [Chain][bookofproofs$6191]| [Strictly ordered set][bookofproofs$7993].
=^. `$(V,\preceq )$`| `$(V,\preceq )$`| `$(V,\prec)$`
|For `$u,v,w\in V$`:
* [reflexive][bookofproofs$572]: `$u\preceq u$`
* [antisymmetric][bookofproofs$575]: `$u\preceq v$` and `$v\preceq u$` implies `$u=v$`
* [transitive][bookofproofs$572]: `$u\preceq v$` and `$v\preceq w$` implies `$u\preceq w$`|For `$u,v,w\in V$`:
* [reflexive][bookofproofs$572]: `$u\preceq u$`
* [antisymmetric][bookofproofs$575]: `$u\preceq v$` and `$v\preceq u$` implies `$u=v$`
* [transitive][bookofproofs$572]: `$u\preceq v$` and `$v\preceq w$` implies `$u\preceq w$` 
* [connex][bookofproofs$1308]: `$u\preceq v$` for all `$u,v\in V.$`|For `$u,v,w\in V$`:
* [irreflexive][bookofproofs$575]: `$u\not \prec u$`
* [asymmetric][bookofproofs$575]: `$u\prec v$` implies `$v\not\prec u$` 
* [transitive][bookofproofs$572]: `$u\prec v$` and `$v\prec w$` implies `$u\prec w$` |
|Possibilities:
* **equal**: `$u=v$`
* **less or equal**: `$u\preceq v$`
* **less**: `$u\preceq v$` and `$u\neq v$`
* **greater or equal**: `$u\succeq v$`
* **greater**: `$u\succeq v$` and `$u\neq v$` 
* else **incomparable**|Possibilities:
* **equal**: `$u=v$`
* **less or equal**: `$u\preceq v$`
* **less**: `$u\preceq v$` and `$u\neq v$`
* **greater or equal**: `$u\succeq v$`
* **greater**: `$u\succeq v$` and `$u\neq v$`|Possibilities:
* **less**: `$u\prec v$`
* **greater**: `$u\succ v$`
* else **equal**: `$u=v$`| 
| Eg. `$(\mathbb N,\le)$`| Eg. `$(\mathbb N,<)$`

Please note that since a [total order][bookofproofs$6191] of a set `$V$` is reflexive while a [strict total order][bookofproofs$7993] on it is not, a total order never can be strict total and vice versa. A comparison of both types of order relations leads to the so-called **diagonal**[^1] `$D$` of `$V$` defined by `$D:=\{(x,x)\in \preceq\}$`: 
* We can transform a given [chain][bookofproofs$6191]  `$(V,\preceq )$` to a [strictly ordered set][bookofproofs$7993]  `$(V,\prec)$` by the [set difference][bookofproofs$6830] of the total order "`$\preceq$`" and `$D$`, i.e. the strict order is defined by `$\prec := \preceq\setminus D.$`
* On the other hand, if we change a given strictly ordered set `$(V,\prec)$` into a chain `$(V,\preceq )$` by the [union][bookofproofs$6827] of its strict order "`$\prec$`" and `$D$`, i.e. the total order is defined by `$\preceq:=\prec\cup D.$`

[^1]: The word [diagonal" is chosen reflecting that the pairs elements `$(x,x)\in \preceq$` are exactly the diagonal elements of the "matrix representation][bookofproofs$579] of the reflexive relation "`$\preceq$`".
