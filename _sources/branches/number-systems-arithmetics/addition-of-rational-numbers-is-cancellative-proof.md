layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1472
orderid: 50
parentid: bookofproofs$1471
title: 
description:  Proof of ADDITION OF RATIONAL NUMBERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,cancellative,left cancellation property,numbers,rational,right cancellation property,proof
contributors: bookofproofs

---


---

Because the [addition of rational numbers is commutative][bookofproofs$1469], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x+z=y+z\Longleftrightarrow x=y,~~~~~~(x,y,z\in\mathbb Q).\]`

[By definition of rational numbers][bookofproofs$1033], each rational number is an equivalence class of ordered pairs of integers represented by some integers `\(a,b,c,d,e,f\in\mathbb Z\)`, with `\(b\neq 0,d\neq 0,f\neq 0\)`[^1]:

`\[\begin{array}{ccc}x:=\frac ab,&y:=\frac cd,&z:=\frac ef.\end{array}\]`

Assume the equation `\(x+z=y+z\)` holds. We have to show that `\(x=y\)`, and we will do it by virtue of the following mathematical definitions and concepts:
* [definition of adding rational numbers][bookofproofs$1446],
* [cancellation law for multiplying integers][bookofproofs$1464],
* [distributivity law for integers][bookofproofs$1466],
* [associativity law for multiplying integers][bookofproofs$1450], 
* [commutativity law for multiplying integers][bookofproofs$1448], and
* [cancellation law for adding integers][bookofproofs$1462].
`\[\begin{array}{rcll}
x+z=y+z&\Leftrightarrow&\frac ab+\frac ef=\frac cd+\frac ef&\text{by definition of rational numbers}\\
&\Leftrightarrow&\frac {af+eb}{bf}+\frac {cf+ed}{df}& \text{by definition of adding rational numbers}\\
&\Leftrightarrow&(af+eb)df=(cf+ed)bf&\text{by definition of rational numbers}\\
&\Leftrightarrow&(af+eb)d=(cf+ed)b&\text{by cancellation law for multiplying integers}\\
&\Leftrightarrow&(af)d+(eb)d=(cf)b+(ed)b&\text{by distributivity law for integers}\\
&\Leftrightarrow&afd+ebd=cfb+edb&\text{by associativity law for multiplying integers}\\
&\Leftrightarrow&adf+ebd=cbf+ebd&\text{by commutativity law for multiplying integers}\\
&\Leftrightarrow&adf=cbf&\text{by cancellation law for adding integers}\\
&\Leftrightarrow&ad=cb&\text{by cancellation law for multiplying integers}\\
&\Leftrightarrow&\frac ab=\frac cd&\text{by definition of rational numbers}\\
&\Leftrightarrow&x=y&\text{by definition of rational numbers}\\
\end{array}\]`

Altogether, we have shown that the addition of integers is [cancellative][bookofproofs$837] `\[ x+z=y+z\Rightarrow x=y,~~~~~~(x,y,z\in\mathbb Q),\]`
and its conversion
`\[x=y\Rightarrow x+z=y+z,~~~~~~(x,y,z\in\mathbb Q).\]`

[^1]: Note that the symbol "`\(0\)`" denotes the zero defined for integers, and not the zero defined for rational numbers.
