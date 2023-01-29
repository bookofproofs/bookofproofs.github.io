layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1006
orderid: 50
parentid: bookofproofs$1005
title: 
description:  Proof of FACTORIAL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$977
keywords: factorial,factorials,proof
contributors: bookofproofs

---


---

Let `\(V\)` be a finite set with `\(|V|=n\)`.

If `\(n \ge 1\)`, then without loss of generality let `\(V=\{a_1,a_2,\ldots,a_n\}\)`. We want to count the different [permutations][bookofproofs$188] of `\(V\)`, which according to their definition are bijective maps on the [index set][bookofproofs$6198] `\(I=\{1,2,\ldots,n\}\)`: `\(\pi:I\mapsto I\)`. More precisely, instead of counting different bijective maps, we will find the cardinal number of the set `\(\Pi=\{\pi:I\mapsto I\}\)` of all possible bijective maps.

In order to define one element of `\(\pi\in\Pi\)`, we have do define `\(\pi\)` for all `\(i\in I\)`, using the following procedure:

> To define `\(\pi(1)=i_1\)`, all values from  `\(I\)` are possible, and we choose  `\(i_1\in I_1:=I\)`.

> We have to define `\(\pi(2)=i_2\)` in such a way that `\(\pi\)` remains bijective. For that, only the values from `\(I_2:=I\setminus\{i_1\}\)` are possible, and we choose `\(i_2\in I_2\)`.

> Similarly, to define `\(\pi(3)=i_3\)`, only the values from  `\(I_3:=I\setminus\{i_1,i_2\}\)` are possible, and we choose `\(i_3\in I_3\)`.

> Similarly, to define `\(\pi(4)=i_4\)`, only the values of `\(I_4:=I\setminus\{i_1,i_2,i_3\}\)` are possible, and we choose `\(i_4\in I_4\)`.

> `\(\vdots\)`

> We repeat this procedure until we define `\(\pi(n)=i_n\)`, for which only one value from `\(I_n:=I\setminus\{i_1,i_2,i_3,\ldots,i_{n-1}\}\)` is possible, and we choose `\(i_n\in I_n\)`.

Following the [definition of set difference][bookofproofs$552] and the [fundamental counting principle][bookofproofs$111] we have that

`\[\begin{array}{ccl}
|\Pi|&=&|I_1|\cdot|I_2|\cdot|I_3|\cdot\ldots\cdot|I_{n-1}|\cdot|I_n|\\
&=&n\cdot(n-1)\cdot(n-2)\cdot\ldots\cdot 2\cdot 1\\
&=&n!
\end{array}
\]`

If `\(n = 0\)`, then `\(V\)` is empty and the existence of only one bijective map `\(\pi:\emptyset\mapsto\emptyset\)` is [vacuously true][bookofproofs$781]. Therefore, we set 

`\[0!:=1.\]`
