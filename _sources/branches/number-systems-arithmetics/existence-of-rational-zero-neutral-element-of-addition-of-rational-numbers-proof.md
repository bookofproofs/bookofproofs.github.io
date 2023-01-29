layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1474
orderid: 50
parentid: bookofproofs$1473
title: 
description:  Proof of EXISTENCE OF RATIONAL ZERO NEUTRAL ELEMENT OF ADDITION OF RATIONAL NUMBERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,element,existence,neutral,numbers,rational,zero,proof
contributors: bookofproofs

---


---

By [definition of rational numbers][bookofproofs$1033] `\(x\in\mathbb Q\)`, the rational number `\(x\in\mathbb Q\)` can be represented by a pair of integers  `\(a,b\in\mathbb Z\)`:
`\[x:=\frac ab,\quad b\in\mathbb Z\setminus\{0\}.\]`
Since `\(0\in\mathbb Z\)`, i.e. the [integer zero exists][bookofproofs$1452], the (rational) zero `\(0\in\mathbb Q\)` also exists, because it can be represented e.g. by the a pair of two integers: the (integer) zero and an arbitrary integer `\(d\neq 0\)`: 
`\[0=0_{\in\mathbb Q}:=\frac {0_{\in\mathbb Z}}{d},\quad d\in\mathbb Z\setminus\{0\}.\]`

We will show that the (rational) zero is neutral with respect to the addition of rational numbers by virtue of the following mathematical definitions and concepts:
* [definition of addition of rational numbers][bookofproofs$1446] "`\( + \)`",
* `\(\mathbb Z\)` is an [integral domain][bookofproofs$892], in particular `\(0_{\in\mathbb Z}\)` is its only zero divisor, and
* [integer `\(0_{\in\mathbb Z}\)` is neutral with respect to addition of integers][bookofproofs$1452]:


`\[\begin{array}{rcll}
x + 0&=&\frac ab+\frac 0d&\text{by definition of rational numbers}\\
&=&\frac{ad+0b}{bd}&\text{by definition of addition of rational numbers}\\
&=&\frac{ad+0}{bd}&\text{because 0 is the only zero divisor of integers}\\
&=&\frac{ad}{bd}&\text{because 0 is neutral with respect to the addition of integers}\\
&=&\frac{a}{b}&\text{because }\mathbb Z\text{ is an integral domain}\\
&=&x&\text{by definition of rational numbers}
\end{array}
\]`

It remains to be shown that also the equation `\(0+x=x\)` holds for all `\(x\in\mathbb Q\)`. It follows immediately from the [commutativity of adding rational numbers][bookofproofs$1469].