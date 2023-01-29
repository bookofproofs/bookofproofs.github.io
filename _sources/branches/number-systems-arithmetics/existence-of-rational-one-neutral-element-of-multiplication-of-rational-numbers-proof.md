layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1483
orderid: 50
parentid: bookofproofs$1482
title: 
description:  Proof of EXISTENCE OF RATIONAL ONE NEUTRAL ELEMENT OF MULTIPLICATION OF RATIONAL NUMBERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: 
keywords: element,existence,multiplication,neutral,numbers,one,rational,proof
contributors: bookofproofs

---


---

By [definition of rational numbers][bookofproofs$1033], the rational number `\(x\in\mathbb Q\)` can be represented by a pair of integers `\(a,b\in\mathbb Z\)` with `\(b\neq 0\)`. 
`\[x:=\frac ab.\]`


Since `\(1\in \mathbb Z\)`, i.e. the [integer one exists][bookofproofs$1454], the (rational) one `\(1\in\mathbb Q\)` also exists, because it can be represented by any pair of the integers  `\(h\in\mathbb Z\)`, `\(h\neq 0\)`, in particular by `\(h=1\in\mathbb Z\)`: 
`\[1_{\in\mathbb Q}:=\frac hh=\frac {1_{\in\mathbb Z}}{1_{\in\mathbb Z}}\]`

We will prove that `\(1\)` is neutral with respect to the multiplication of rational numbers by virtue of the following mathematical definitions and concepts:
* [definition of multiplication of rational numbers][bookofproofs$1475] "`\( \cdot \)`", and
* `\(1\in\mathbb Z\)` [is neutral with respect to the multiplication of integers][bookofproofs$1454]:

`\[\begin{array}{rcll}
x \cdot 1&=&\frac ab\cdot\frac 11&\text{by definition of rational numbers}\\
&=&\frac {a1}{b1}&\text{by definition of multiplication of rational numbers}\\
&=&\frac ab&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&x&\text{by definition of rational numbers}
\end{array}
\]`

In other words, the rational number `\(1\)` is neutral with respect to the multiplication of rational numbers.

It remains to be shown that also the equation `\(1\cdot x=x\)` holds for all `\(x\in\mathbb Q\)`. It follows immediately from the [commutativity of multiplying rational numbers][bookofproofs$1478].