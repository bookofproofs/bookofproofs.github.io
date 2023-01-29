layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1697
orderid: 50
parentid: bookofproofs$1696
title: 
description:  Proof of LINEAR INDEPENDENCE OF THE IMAGINARY UNIT \I\ AND THE COMPLEX NUMBER \1\ &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$1038,bookofproofs$1692
keywords: complex,imaginary,independence,linear,number,unit,linear independence complex vectors,proof
contributors: bookofproofs

---


---

Because we have already shown that the [complex numbers form a vector space over the field of real numbers][bookofproofs$1694], we will now prove that the vectors [complex number one][bookofproofs$1673] `\(1\)` and the [imaginary unit][bookofproofs$1160] `\(i\)` are [linearly independent][bookofproofs$1036]. Let `\(\alpha,\beta\in\mathbb R\)` be some real numbers and consider the equation
`\[\alpha\cdot 1 + \beta \cdot i=0.\]`
We have to prove that this equation has only the trivial solution `\(\alpha=\beta=0\)`. For the purpose of a better understanding of the prove, we will use the notation 
`\[\alpha\cdot (1) + \beta \cdot (i)=0,\]`
to indicate that `\((1)\)` and `\((i)\)` are vectors and not simply numbers.

By definition, the complex vector `\(1:=(1,0)\)`, i.e. the complex number `\(1\)` is identical with the [ordered pair][bookofproofs$747] of real numbers `\((1,0)\)`. Analogously,  the complex vector `\(i:=(0,1)\)`, i.e. the complex number `\(i\)` is identical with the ordered pair of real numbers  `\((0,1)\)`. Therefore, the above equation is equivalent to
`\[\begin{array}{rcl}
\alpha\cdot (1) + \beta \cdot (i)=0&\Longleftrightarrow&\beta\cdot (i)=-\alpha\cdot (1)\\
&\Longleftrightarrow&\beta\cdot (0,1)=-\alpha\cdot (1,0)
\end{array}\]`
From the [definition of the scalar multiplication][bookofproofs$1694], it follows
`\[ (0,\beta)=(-\alpha,0)\Longleftrightarrow -\alpha=0\text{ and }\beta=0.\]`

Because `\(-\alpha=-1\cdot \alpha\)` (i.e the [product of the real numbers][bookofproofs$1532] `\(-1\)` and `\(\alpha\)`) and because [the product of two real numbers is only zero, if at least one of them is zero][bookofproofs$528], it follows `\(\alpha=0\)`.
