layout: motivation
categories: branches,set-theory
nodeid: bookofproofs$8049
orderid: 700
parentid: bookofproofs$185
title: Cantor's Astonishing Discoveries Regarding the Cardinals of Infinite Sets
description: CANTOR'S ASTONISHING DISCOVERIES REGARDING THE CARDINALS OF INFINITE SETS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1038
keywords: astonishing,cantor,cardinals,discoveries,infinite,regarding,sets
contributors: bookofproofs


---


---

It is intuitively clear that it is possible to compare the cardinals of [finite sets][bookofproofs$985]. For instance, a [subset of a finite set is again finite][bookofproofs$986]. In particular a proper subset `$S$` of a set `$X$` with `$|X|=|n|$` for some [natural number][bookofproofs$718] `$n\in\mathbb N$` will have a smaller cardinality `$|S|<|n|.$` This relation holds for instance for the sets
`$$X=\{1,2,3,4,5,6,7,8,9,10\},\quad S=\{2,4,6,8,10\}.$$`

In the course of his research, [Georg Cantor][bookofproofs$Cantor] (1845 - 1918) realized that it is also possible to [compare the cardinal numbers][bookofproofs$984] of [infinite sets][bookofproofs$985]. He was very surprised when he discovered that a proper subset `$S$` of an infinite set can have _the same_ cardinality, in contrary to the finite case. All that is needed is to find a [bijective function][bookofproofs$771] between the two.

For instance, take the set `$S\subset\mathbb N$` of all [even][bookofproofs$2317] [natural numbers][bookofproofs$718]. It has the same cardinality as `$\mathbb N,$` i.e. `$|\mathbb N|=|S|,$` although `$S\subset \mathbb N.$` A bijective function is indicated by the following table:

`$$\begin{array} {rcl}
1&\leftrightarrow&2\\
2&\leftrightarrow&4\\
&\vdots\\
n&\leftrightarrow&2n\\
&\vdots\\
\end{array}$$`

Cantor then found a bijective function between the (infinite) set of natural numbers `$\mathbb N$` and the [Cartesian product][bookofproofs$748] `$\mathbb N\times \mathbb N.$` The function shown below does the trick: 


![cantordiagonal](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/cantordiagonal.png?raw=true)


This function `$f:\mathbb N\times \mathbb N\to\mathbb N$` maps every [ordered pair][bookofproofs$747] of natural numbers `$(x,y)$` uniquely to the single natural number `$f((x,y))$` and this shows that `$\mathbb N^2$` and `$\mathbb N$` have the same [cardinalities][bookofproofs$980]. But in addition to this, it is even possible to [compose][bookofproofs$6866] the function `$f$` with itself requiring `$f(f(x,y),z).$` This leads to the fascinating result `$$|\mathbb N|=|\mathbb N^n|,\quad n\in \mathbb N$$` i.e. that the natural numbers `$\mathbb N$` and the multidimensional number space `$\mathbb N^n$` have still the same cardinalities, no matter how big we choose the dimension `$n.$`
