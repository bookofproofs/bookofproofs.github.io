layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1459
orderid: 50
parentid: bookofproofs$1454
title: 
description:  Proof of EXISTENCE OF INTEGER ONE NEUTRAL ELEMENT OF MULTIPLICATION OF INTEGERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: integers,multiplication,multiplication of integers,proof,neutral integer,proof
contributors: bookofproofs

---


---

By the [definition of integers][bookofproofs$844], an integer number `\(x\in\mathbb Z\)` can be represented by a pair of natural numbers `\(a,b\in\mathbb N\)`:
`\[x:=[a,b].\]`

Since `\(1_{\in\mathbb N}\)`, i.e. the [natural one exists][bookofproofs$1457], and since `\(0_{\in\mathbb N}\)`, i.e. the [natural zero exists][bookofproofs$1455], it is also true that the integer one `\(1_{\in\mathbb Z}\)` exists, because it can be represented by a pair of the natural numbers
`\[1=1_{\in\mathbb Z}:=[h+1_{n\in\mathbb N},h],\quad h\in\mathbb N,\]`
in particular (for `\(h=0\in\mathbb N\)`):
`\[1=1_{\in\mathbb Z}=[1_{\in\mathbb N},0_{\in\mathbb N}].\]`

We will prove that `\(1\)` is neutral with respect to the multiplication of integers by virtue of the following mathematical definitions and concepts:
* [definition of multiplication of integers][bookofproofs$891] "`\( \cdot \)`", 
* [definition of multiplication of natural numbers][bookofproofs$876], 
* [commutativity law for adding natural numbers][bookofproofs$1430], 
* the natural number `\(0_{\in\mathbb N}\)` is [neutral with respect to the addition of natural numbers][bookofproofs$1455], and 
* the natural number `\(1_{n\in\mathbb N}\)` is [neutral with respect to the multiplication of natural numbers][bookofproofs$1457].

`\[\begin{array}{rcll}
x \cdot 1&=&[a,b]\cdot[1_{n\in\mathbb N},0_{\in\mathbb N}]&\text{by definition of integers}\\
&=&[a\cdot 1_{n\in\mathbb N} + b\cdot 0_{\in\mathbb N},~ a\cdot 0_{\in\mathbb N} + b\cdot 1_{n\in\mathbb N}]&\text{by definition of multiplication of integers}\\
&=&[a\cdot 1_{n\in\mathbb N} + 0_{\in\mathbb N},~ 0_{\in\mathbb N} + b\cdot 1_{n\in\mathbb N}]&\text{by definition of multiplication of natural numbers (in particular the multiplication by }0_{\in\mathbb N}\text{)}\\
&=&[a\cdot 1_{n\in\mathbb N} + 0_{\in\mathbb N},~ b\cdot 1_{n\in\mathbb N}+ 0_{\in\mathbb N}]&\text{by commutativity of addition of natural numbers}\\
&=&[a\cdot 1_{n\in\mathbb N},~ b\cdot 1_{n\in\mathbb N}]&0_{\in\mathbb N}\text{ is neutral with respect to the addition of natural numbers}\\
&=&[a,b]&1_{n\in\mathbb N}\text{ is neutral with respect to the multiplication of natural numbers}\\
&=&x&\text{by definition of integers}
\end{array}
\]`
In other words, the integer `\(1:=[1,0]\)` is neutral with respect to the multiplication of integers.

It remains to be shown that also the equation `\(1\cdot x=x\)` holds for all `\(x\in\mathbb Z\)`. It follows immediately from the [commutativity of multiplying rational numbers][bookofproofs$1448].