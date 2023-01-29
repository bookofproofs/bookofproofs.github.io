layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1699
orderid: 50
parentid: bookofproofs$1698
title: 
description:  Proof of COMPLEX NUMBERS ARE TWO-DIMENSIONAL AND THE COMPLEX NUMBERS \1\ AND IMAGINARY UNIT \I\ FORM THEIR BASIS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1038,bookofproofs$1692
keywords: basis of complex numbers,two-dimensional complex numbers,complex numbers as vectors,proof
contributors: bookofproofs

---


---

We want to show that in the [complex vector space of complex numbers over the field or real numbers][bookofproofs$1694], the set of vectors `\(B:=\{1,i\}\)` forms a [basis][bookofproofs$299], i.e. any complex number `\(x\in\mathbb C\)` can be represented by a linear combination of the vectors:

* [complex number one][bookofproofs$1673] `\(1\)` and the 
* [imaginary unit][bookofproofs$1160] `\(i\)` 

`\[x=a \cdot 1+b \cdot i\]`

for some real numbers `\(a,b\in\mathbb R\)`.

We have already shown that the vectors `\(B:=\{1,i\}\)` are [linearly independent][bookofproofs$1696]. It remains to be shown that `\(B\)` is a [generating system][bookofproofs$279] of `\(\mathbb C\)`, i.e. that the set of all possible [linear combinations][bookofproofs$1035] of the vectors in `\(B\)`, i.e. the linear span 

`\[Span(B):=\{a \cdot 1+ b \cdot i~|~a,b\in\mathbb R,~1,i\in \mathbb C\}\]`

generates the complex numbers `\(\mathbb C\)`. By definition, the complex vector `\(1\)` equals the [ordered pair][bookofproofs$747] of real numbers `\((1,0)\)`. Analogously,  the complex vector `\(i\)` is identical with the ordered pair of real numbers  `\((0,1)\)`. From the [definition of scalar multiplication][bookofproofs$1694], and the [addition of complex numbers][bookofproofs$1657] it follows
`\[a \cdot 1+ b \cdot i=a \cdot (1,0)+ b \cdot (0,1)=(a,0)+(0,b)=(a,b)\]`
 for all real numbers `\(a,b\in\mathbb R\)`. Therefore, any complex number `\(x=(a,b)\)` is exactly the number, which is represented by the linear combination `\(a \cdot 1+ b \cdot i\)`. It follows 
`\[Span(B)=\mathbb C.\]`

As a consequence, `\(B\)` is a basis of `\(\mathbb C\)`. The maximum number of linearly independent vectors, which can be spanned in `\(\mathbb C\)` is `\(2\)` (otherwise, we would have `\(Span(B)\subset \mathbb C\)` and not `\(Span(B)=\mathbb C\)`. Thus, `\(\mathbb C \)` is [two-dimensional][bookofproofs$1041].