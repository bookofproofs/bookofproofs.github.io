layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1676
orderid: 50
parentid: bookofproofs$1675
title: 
description:  Proof of EXISTENCE OF INVERSE COMPLEX NUMBERS WITH RESPECT TO MULTIPLICATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: complex multiplication,inverse,proof
contributors: bookofproofs

---


---

By the [definition of complex numbers][bookofproofs$216], a complex number `\(x\in\mathbb C\)` can be represented by a pair of real numbers `\(a,b\in\mathbb R\)`:
`\[x:=(a,b).\]`

Let `\(x\neq 0\)`, i.e. let `\(x\)` not be the [complex zero][bookofproofs$1662]. Therefore, at least one of the real numbers `\(a,b\)` does not equal the [real number zero][bookofproofs$34] `\(0_{\in\mathbb R}\)`. According to the [rules of calculation with inequalities of real numbers][bookofproofs$594], `\(a^2+b^2\)` is a [positive real number][bookofproofs$1107], and the [general power][bookofproofs$1628].
`\[(a^2+b^2)^{-1}=\frac 1{a^2+b^2}\quad\quad ( * )\]` 
exists. Also, for `\(b\in\mathbb R\)`, the [inverse number `\(-b\in\mathbb R\)` with respect to addition exists][bookofproofs$35]. It is now obvious that we can use the real numbers `\(a\)`, `\(-b\)` and `\(( * )\)` to define a new complex number

`\[y:=\left(\frac{a}{a^2+b^2},\frac{-b}{a^2+b^2}\right).\]`

We will show that `\(x^{-1}=y\)`, i.e. that `\(y\)` is an inverse with respect to the [multiplication of complex numbers][bookofproofs$1668] of the complex number `\(x\)`. We will do so applying the following mathematical definitions and concepts:
* [rules of multiplying positive and negative real numbers][bookofproofs$1598], 
* [existence of inverse real numbers with respect to multiplication][bookofproofs$42],
* [commutativity of multiplying real numbers][bookofproofs$38] ,
* [existence of inverse real numbers with respect to addition][bookofproofs$35], and 
* [existence of the complex number one][bookofproofs$1673].
`\[\begin{array}{rcll}
x \cdot y&=&(a,b)\cdot\left(\frac{a}{a^2+b^2},\frac{-b}{a^2+b^2}\right)&\text{by definition of complex numbers}\\
&=&\left(\frac{a\cdot a-b\cdot (-b)}{a^2+b^2},\frac{a\cdot (-b)+b\cdot a}{a^2+b^2}\right)&\text{by definition of multiplication of complex numbers}\\
&=&\left(\frac{a^2+b^2}{a^2+b^2},\frac{-ab+ba}{a^2+b^2}\right)&\text{by the rules of multiplying positive and negative real numbers}\\
&=&(1_{\in\mathbb R},~ \frac{-ab+ba}{a^2+b^2})&\text{by existence of inverse real numbers with respect to multiplication}\\
&=&(1_{\in\mathbb R},~ \frac{-ba+ba}{a^2+b^2})&\text{by commutativity of multiplying real numbers}\\
&=&(1_{\in\mathbb R},~ \frac{0_{\in\mathbb R}}{a^2+b^2})&\text{by existence of inverse real numbers with respect to addition}\\
&=&(1_{\in\mathbb R},~ 0_{\in\mathbb R})&\text{multiplication of a real number by zero}\\
&=&1&\text{by the definition of complex one}
\end{array}
\]`
This completes the proof.
