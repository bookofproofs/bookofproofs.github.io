layout: proof
categories: branches,analysis
nodeid: bookofproofs$1613
orderid: 50
parentid: bookofproofs$1612
title: 
description:  Proof of FUNCTIONAL EQUATION OF THE EXPONENTIAL FUNCTION OF GENERAL BASE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: base,equation,exponential,function,functional,general,proof
contributors: bookofproofs

---


---

Let `\(x,y,a\)` be real numbers and let `\(a > 0\)`. Due to the [functional equation of exponential function][bookofproofs$1415], we have
`\[\exp(x+y)=\exp(x)\cdot \exp(y).\]`
By definition, the exponential equation of general base is given by
`\[\exp_a(x):=\exp(x\ln(a)).\]`
From the [distributivity law for real numbers][bookofproofs$520], it follows

`\[\begin{array}{rcll}
\exp_a(x+y)&=&\exp((x+y)\ln(a))&\text{by definition of }\exp_a\\
&=&\exp(x\ln(a)+y\ln(a))&\text{using the distributivity law}\\
&=&\exp(x\ln(a))\cdot\exp(y\ln(a))&\text{applying the functional equation for the exponential function}\\
&=&\exp_a(x)\cdot\exp_a(y)&\text{by definition of }\exp_a\\
\end{array}\]`
