layout: proof
categories: branches,analysis
nodeid: bookofproofs$1629
orderid: 50
parentid: bookofproofs$1628
title: 
description:  Proof of CALCULATION RULES FOR GENERAL POWERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: general powers of positive numbers,general powers,general power,proof,proof
contributors: bookofproofs

---


---

Let `\(x,y\)` be [real numbers][bookofproofs$1105] and let `\(a,b\)` be [positive real numbers][bookofproofs$1107].
#### `\((i)\)` `\(a^{x+y}=a^x\cdot a^y\)` 

It follows from the  [definition of the general power function][bookofproofs$1626] and the [functional equation of exponential function of general base][bookofproofs$1612].
#### `\((ii)\)` `\((a^x)^y=a^{x\cdot y}\)` 

The rule can be concluded as follows from the [definition of exponential function of general base][bookofproofs$1603], and the [definition of natural logarithm][bookofproofs$1421]: Because `\[a^x=\exp_a(x)=\exp(x\ln(a))\Longleftrightarrow \ln(a^x)=x\ln a,\]`
we get 
`\[a^{xy}=\exp_a(xy)=\exp(yx\ln a)=\exp(y\ln(a^x))=(a^x)^y.\]`

####  `\((iii)\)` `\(a^x\cdot b^x=(ab)^x\)` 

This rule follows from the [definition of the general power function][bookofproofs$1626], the [definition of exponential function of general base][bookofproofs$1603], the [functional equation of exponential function][bookofproofs$1415], the [distributivity law for real numbers][bookofproofs$520] and the [functional equation of natural logarithms][bookofproofs$1601]:

`\[\begin{array}{rcll}
a^x\cdot b^x&=&\exp_a(x)\cdot\exp_b(x)&\text{definition of general power function}\\
&=&\exp(x\cdot \ln a)\cdot\exp(x\cdot \ln b)&\text{definition of exponential function of general base}\\
&=&\exp(x\cdot \ln a+ x\cdot \ln b)&\text{functional equation of exponential function}\\
&=&\exp(x\cdot (\ln a+ \ln b))&\text{distributivity law for real numbers}\\
&=&\exp(x\cdot (\ln (a\cdot b))&\text{functional equation of natural logarithm}\\
&=&\exp_{ab}(x)&\text{definition of exponential function of general base}\\
&=&(ab)^x&\text{definition of general power function}\\
\end{array}\]`

####  `\((iv)\)` `\(a^{-x}=\frac 1{a^x}\)` 

This calculation rule follows from the  [definition of the general power function][bookofproofs$1626] and the [reciprocity of exponential function of general base][bookofproofs$1614].