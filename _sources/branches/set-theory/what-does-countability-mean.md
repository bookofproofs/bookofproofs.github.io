layout: proof
categories: branches,set-theory
nodeid: bookofproofs$773
orderid: 50
parentid: bookofproofs$6661
title: What does countability mean?
description:  Proof of REAL NUMBERS ARE UNCOUNTABLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656
keywords: real numbers are uncountable,proof
contributors: bookofproofs


---
[Cantor][bookofproofs$Cantor]'s proof is as brilliant as it is simple.

---

We want to show that the set `$\mathbb R$` of [real numbers][bookofproofs$1105] is [uncountable][bookofproofs$772]. We will show that this is true even for the [real interval][bookofproofs$1153] `$[0,1]\subset\mathbb R.$` 
* Suppose, `$[0,1]$` is [countable][bookofproofs$772].
* Therefore, by [definition of countability][bookofproofs$772], there is an [injective function][bookofproofs$769] `$f:[0,1]\to\mathbb N$`. 
* Suppose that we can list the values of this function in some hypothetical way:
`\[
\begin{array}{rcl}
(\underline{0}.0379357232\ldots)&\rightarrow&1\\
(0.\underline{7}112223358\ldots)&\rightarrow&2\\
(0.9\underline{4}80483777\ldots)&\rightarrow&3\\
(0.00\underline{8}4973921\ldots)&\rightarrow&4\\
(0.009\underline{5}857262\ldots)&\rightarrow&5\\
(0.0399\underline{0}39551\ldots)&\rightarrow&6\\
(0.23964\underline{3}9345\ldots)&\rightarrow&7\\
\vdots
\end{array}
\]`
* Now, consider the real number `$r$` built by the underlined digits in the diagonal.[^1] 
* Now, define a new real number `$s$` by changing in `$r$` every digit after the comma in an arbitrary way.[^2] 
* Note that we cannot find any value `\(n\in\mathbb N\)` such that `$f(s)=n$`. 
* Thus, although we have found a new real number, `$f$` is not injective.  
* This is a contradiction to the hypothesis.
* Thus the number of real numbers `$0\le r\le 1$` is [uncountable][bookofproofs$772].
[^1]: In our example, `\(r=3.748503\ldots\)`. 

[^2]: For instance, change after the point `\(7\)` to `\(8\)` , `\(4\)` to `\(7\)`, `\(8\)` to `\(1\)`, `\(5\)` to `\(6\)`, `\(0\)` to `\(9\)`, `\(3\)` to `\(1\)`, etc. After this procedure, we will get a new real number, which is, in our case `\(s=0.871691\ldots\)`.
