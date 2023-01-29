layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1674
orderid: 50
parentid: bookofproofs$1673
title: 
description:  Proof of EXISTENCE OF COMPLEX ONE NEUTRAL ELEMENT OF MULTIPLICATION OF COMPLEX NUMBERS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex,element,existence,multiplication,neutral,numbers,one,complex number multiplication,proof
contributors: bookofproofs

---


---

By the [definition of complex numbers][bookofproofs$216], a complex number `\(x\in\mathbb C\)` can be represented by a pair of real numbers `\(a,b\in\mathbb R\)`:
`\[x:=(a,b).\]`

Since `\(1_{\in\mathbb R}\)`, i.e. the [real number one exists][bookofproofs$40], and since `\(0_{\in\mathbb R}\)`, i.e. the [real number zero exists][bookofproofs$34], it is also true that the (complex number) one `\(1_{\in\mathbb C}\)` exists, because it can be represented by a pair of the real numbers
`\[1=1_{\in\mathbb C}:=(1_{\in\mathbb R},0_{\in\mathbb R}).\]`

We will prove that `\(1\)` is neutral with respect to the multiplication of complex numbers by virtue of the following mathematical definitions and concepts:
* [definition of multiplication of complex numbers][bookofproofs$1668] "`\( \cdot \)`", 
* [multiplication by real number zero][bookofproofs$521], 
* [commutativity law for adding real numbers][bookofproofs$33], 
* the real number `\(0_{\in\mathbb R}\)` is [neutral with respect to the addition of natural numbers][bookofproofs$34], and 
* the real number `\(1_{\in\mathbb R}\)` is [neutral with respect to the multiplication of natural numbers][bookofproofs$40].

`\[\begin{array}{rcll}
x \cdot 1&=&(a,b)\cdot(1_{\in\mathbb R},0_{\in\mathbb R})&\text{by definition of complex numbers}\\
&=&(a\cdot 1_{\in\mathbb R} - b\cdot 0_{\in\mathbb R},~ a\cdot 0_{\in\mathbb R} + b\cdot 1_{\in\mathbb R})&\text{by definition of multiplication of complex numbers}\\
&=&(a\cdot 1_{\in\mathbb R} - 0_{\in\mathbb R},~ 0_{\in\mathbb R} + b\cdot 1_{\in\mathbb R})&\text{multiplication by real number zero}\\
&=&(a\cdot 1_{\in\mathbb R} - 0_{\in\mathbb R},~ b\cdot 1_{\in\mathbb R}+  0_{\in\mathbb R})&\text{by commutativity of adding real numbers}\\
&=&(a\cdot 1_{\in\mathbb R},~ b\cdot 1_{\in\mathbb R})&0_{\in\mathbb R}\text{ is neutral with respect to the addition (and subtraction) of real numbers}\\
&=&(a,b)&1_{\in\mathbb R}\text{ is neutral with respect to the multiplication of real numbers}\\
&=&x&\text{by definition of complex numbers}
\end{array}
\]`
In other words, the complex number `\(1:=(1_{\in\mathbb R},0_{\in\mathbb R})\)` is neutral with respect to the multiplication of complex numbers.

It remains to be shown that also the equation `\(1\cdot x=x\)` holds for all `\(x\in\mathbb C\)`. It follows immediately from the [commutativity of multiplying complex numbers][bookofproofs$1671].