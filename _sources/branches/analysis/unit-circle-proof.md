layout: proof
categories: branches,analysis
nodeid: bookofproofs$1750
orderid: 50
parentid: bookofproofs$1749
title: 
description:  Proof of UNIT CIRCLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: unit circle,unit circles,proof
contributors: bookofproofs

---


---

In the following proof, we will use the following results:
* [definition of absolute value of complex numbers][bookofproofs$1247],
* [taking roots is inverse to taking squares][bookofproofs$46],
* [complex conjugate of complex exponential function][bookofproofs$1747],
* [definition of the complex conjugate][bookofproofs$1245],
* [function equation of the complex exponential function][bookofproofs$1735],
* [the complex case of the result `\(\exp(0)=1\)`][bookofproofs$1739],
* [existence of inverse elements with respect to addition of complex numbers][bookofproofs$1664],
* [definition of the real part][bookofproofs$1698]:

`\[\begin{array}{rcll}
|\exp(ix)|^2&=&\left(\sqrt{\Re(\exp(ix)\cdot(\exp(ix))^*)}\right)^2&\text{definition of absolute value for complex numbers}\\
&=&\Re(\exp(ix)\cdot(\exp(ix))^*)&\text{taking roots is inverse to taking squares}\\
&=&\Re(\exp(ix)\cdot\exp((ix)^*))&\text{complex conjugate of complex exponential function}\\
&=&\Re(\exp(ix)\cdot\exp(-ix))&\text{definition of complex conjugate}\\
&=&\Re(\exp(ix+(-ix)))&\text{functional equation of}\exp\\
&=&\Re(\exp(0))&\text{existence of inverse elements with respect to addition of complex numbers}\\
&=&\Re(1)&\text{because}\exp(0))=1\\
&=&1&\text{definition of real part}\\
\end{array}\]`

Taking [square roots][bookofproofs$1161] on both sides of the equation gives the desired result
`\[|\exp(ix)|=1.\]`
