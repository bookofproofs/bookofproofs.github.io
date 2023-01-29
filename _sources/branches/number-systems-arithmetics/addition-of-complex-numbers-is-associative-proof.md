layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1659
orderid: 50
parentid: bookofproofs$1658
title: 
description:  Proof of ADDITION OF COMPLEX NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: addition,associative,complex,numbers,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [complex numbers, which by definition means][bookofproofs$216] that they are ordered pairs of real numbers `\[\begin{array}{rcl}x&:=&(a,b),\\
y&:=&(c,d),\\z&:=&(e,f).\end{array}\]`

The associativity of the [addition of complex numbers][bookofproofs$1657] `\((x+y)+z=x+(y+z)\)` for all `\(x,y,z\in\mathbb C\)` follows from the [associativity of adding real numbers][bookofproofs$31]:
`\[\begin{array}{rcll}
(x+y)+z&=&[(a,b)+(c,d)]+(e,f)&\text{by definition of complex numbers}\\
&=&(a+c,b+d)+(e,f)&\text{by definition of adding complex numbers}\\
&=&((a+c)+e,(b+d)+f)&\text{by definition of adding complex numbers}\\
&=&(a+(c+e),b+(d+f))&\text{by associativity of adding real numbers}\\
&=&(a,b)+(c+e,d+f)&\text{by definition of adding complex numbers}\\
&=&(a,b)+[(c,d)+(e,f)]&\text{by definition of adding complex numbers}\\
&=&x+(y+z)&\text{by definition of complex numbers}
\end{array}\]`
