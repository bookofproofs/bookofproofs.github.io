layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$844
orderid: 50
parentid: bookofproofs$118
title: Definition of Integers
description: DEFINITION OF INTEGERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: definition,integers
contributors: bookofproofs


---


---

Let `\((a,b),(c,d)\)` be [ordered pairs][bookofproofs$747] of [natural numbers][bookofproofs$718]. We consider them equivalent, if there exist a natural number `\(h\)` such that one ordered pair can be obtained from the other ordered pair [by adding][bookofproofs$842]  `\(h\)` to both natural numbers of that pair, formally 

`\[(a,b)\sim (c,d)\quad\Longleftrightarrow\quad\begin{cases}(a+h,b+h)=(c,d)& or\`\(a,b)=(c+h,d+h).\end{cases}\]`

The relation [\(\sim\)`" defined above is an "equivalence relation][bookofproofs$574], i.e. for a given ordered pair `\((a,b)\in\mathbb N\times\mathbb N\)`, we can consider a whole set of ordered pairs `\((c,d)\in\mathbb N\times\mathbb N\)` equivalent to `\((a,b)\)`:

`\[x:=\{(c,d)\in\mathbb N\times\mathbb N:\quad( c, d )\sim ( a, b )\}.\]`

The set `\(x\)` is called an **integer**[^1]. We say that the ordered pair `\((a,b)\in\mathbb N\times\mathbb N\)` is **representing** the integer `\(x\)`. The **set of all integers** is denoted by `\(\mathbb Z\)`.

### Notation

In order to make a difference in notation, we write `\([a,b]\)`, instead of `\((a,b)\)`, if we mean the integer represented by the ordered pair `\((a,b)\)` rather than the concrete ordered pair `\((a,b)\)`. A more common (e.g. taught in the elementary school) notation is the notation of integers retrieved from the difference `\(a-b\)`, however, the concept of building a difference is not introduced yet (in fact, we have not introduced the concept of negative integers yet[^2]). For the time being, we give a comparison of the different notations to make more clear:  


Common integer notation | Alternative integer notations | Set of ordered pairs of natural numbers, each notation stands for
:------------- |:------------- |:-------------
 `\(\vdots\)`| `\(\vdots\)`| `\(\vdots\)`
 `\(-3\)`| e.g. `\([0,3],[1,4],\ldots\)`| `\(\begin{array}{llllll}\{(0,3),&(1,4),&(2,5),&\ldots,&(h,3+h),&~h\in\mathbb N\}\end{array}\)`
 `\(-2\)`| e.g. `\([0,2],[1,3],\ldots\)`| `\(\begin{array}{llllll}\{(0,2),&(1,3),&(2,4),&\ldots,&(h,2+h),&~h\in\mathbb N\}\end{array}\)`
 `\(-1\)`| e.g. `\([0,1],[1,2],\ldots\)`| `\(\begin{array}{llllll}\{(0,1),&(1,2),&(2,3),&\ldots,&(h,1+h),&~h\in\mathbb N\}\end{array}\)`
 `\(0\)`| e.g. `\([0,0],[1,1],\ldots\)`| `\(\begin{array}{llllll}\{(0,0),&(1,1),&(2,2),&\ldots,&(h,h),&~h\in\mathbb N\}\end{array}\)`
 `\(1\)`| e.g. `\([1,0],[2,1],\ldots\)`| `\(\begin{array}{llllll}\{(1,0),&(2,1),&(3,2),&\ldots,&(1+h,h),&~h\in\mathbb N\}\end{array}\)`
 `\(2\)`| e.g. `\([1,0],[3,1],\ldots\)`| `\(\begin{array}{llllll}\{(2,0),&(3,1),&(4,2),&\ldots,&(2+h,h),&~h\in\mathbb N\}\end{array}\)`
 `\(3\)`| e.g. `\([1,0],[4,1],\ldots\)`| `\(\begin{array}{llllll}\{(3,0),&(4,1),&(5,2),&\ldots,&(3+h,h),&~h\in\mathbb N\}\end{array}\)`
 `\(\vdots\)`| `\(\vdots\)`| `\(\vdots\)`

	

[^1]: Please note that integers are in fact sets.

[^2]: The concept of negative integers will be introduced in the discussion of [order relation for integers][bookofproofs$1075].