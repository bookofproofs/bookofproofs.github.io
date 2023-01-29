layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$579
orderid: 100
parentid: bookofproofs$7988
title: Representations of Binary Relations
description: REPRESENTATIONS OF BINARY RELATIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$573
keywords: binary,relations,representations
contributors: bookofproofs


---
Before we discuss the properties of binary relations in general, we first introduce some ways to represent a given binary relation.

---

There are different possibilities to represent a binary relation `$R\subseteq S\times T$`. Sometimes, we can just enumerate the elements of `\(R\)`. For instance, if `\(S,T\)` are bothe the set of [natural numbers][bookofproofs$664] `\(\mathbb N\)` and `\(R\)` is the [successor][bookofproofs$504] relation, then we can write `\[R:=\{(1,2),(2,3),(3,4),\ldots \}\]`

The figure below shows another representation of an infinite relation of all pairs of [real numbers][bookofproofs$167] `\(x,y\in\mathbb R\)` satisfying the relation `\(x\le y\)`.


![relation1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/relation1.png?raw=true)


If `\(S, T\)` have a finite number of elements, there are at least four possibilities to represent a relation. We demonstrate these possibilities for the [divisibility][bookofproofs$77] relation `\(R\)` of all natural numbers between 1 and 10.

#### 1) Table Representation of `\(R\)`:

 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
  1| x| x| x| x| x| x| x| x| x| x
  2| | x| | x| | x| | x| | x
  3| | | x| | | x| | | x|
  4| | | | x| | | | x| | 
  5| | | | | x| | | | | x
  6| | | | | | x| | | | 
  7| | | | | | | x| | | 
  8| | | | | | | | x| | 
  9| | | | | | | | | x| 
  10| | | | | | | | | | x

#### 2) [Matrix][bookofproofs$1048]. Representation of `\(R\)`:

`\[M_R:=\left(\begin{array}{cccccccccc}
1&1&1&1&1&1&1&1&1&1\\ 
0&1&0&1&0&1&0&1&0&1\\ 
0&0&1&0&0&1&0&0&1&0\\
0&0&0&1&0&0&0&1&0&0\\
0&0&0&0&1&0&0&0&0&1\\
0&0&0&0&0&1&0&0&0&0\\
0&0&0&0&0&0&1&0&0&0\\
0&0&0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&0&1&0\\
0&0&0&0&0&0&0&0&0&1\\
\end{array}
\right)\]`

Please note that the matrix of the inverse relation `$R^{-1}$` corresponds to the [transposed matrix][bookofproofs$1054] of `$M_R$`. i.e.

`\[M_{R^{-1}}=(M_R)^{T}=\left(\begin{array}{cccccccccc}
1&0&0&0&0&0&0&0&0&0\\ 
1&1&0&0&0&0&0&0&0&0\\ 
1&0&1&0&0&0&0&0&0&0\\
1&1&0&1&0&0&0&0&0&0\\
1&0&0&0&1&0&0&0&0&1\\
1&1&1&0&0&1&0&0&0&0\\
1&0&0&0&0&0&1&0&0&0\\
1&1&0&1&0&0&0&1&0&0\\
1&0&1&0&0&0&0&0&1&0\\
1&1&0&0&0&0&0&0&0&1\\
\end{array}
\right)\]`
In our case, this matrix represents the relation of numbers `$(n,m)$` where `$n$` is the multiple of `$m.$`

#### 3) [Digraph][bookofproofs$524]. Representation of `\(R\)`:


![relation2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/relation2.png?raw=true)


The digraph of the inverse relation is the same digraph with all arrows reversed.


#### 4) List Representation of `\(R\)`:

 is devisor of ...
 1| `\(\{1,2,3,4,5,6,7,8,9,10\}\)`
 2| `\(\{2,4,6,8,10\}\)`
 3| `\(\{3,6,9\}\)`
 4| `\(\{4,8\}\)`
 5| `\(\{5,10\}\)`
 6| `\(\{6\}\)`
 7| `\(\{7\}\)`
 8| `\(\{8\}\)`
 9| `\(\{9\}\)`
 10| `\(\{10\}\)`
