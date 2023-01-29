layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1244
orderid: 50
parentid: bookofproofs$1243
title: 
description:  Proof of COMPLEX NUMBERS ARE A FIELD EXTENSION OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: complex numbers are a field extension of real numbers,real numbers are embedded in complex numbers,complex numbers are an extension of the real numbers,embedded real numbers,proof
contributors: bookofproofs

---


---

Let `\((\mathbb R,\oplus,\odot)\)` be the [field of real numbers][bookofproofs$1638] and let `\((\mathbb C, + ,\cdot)\)` be the [field of complex numbers][bookofproofs$1690]. We want to show that the [function][bookofproofs$592].
`\[f:=\cases{\mathbb R\to\mathbb C,\\
x\to (x,0),}\]`
is an [bijective][bookofproofs$771] [field homomorphism][bookofproofs$559].
Obviously, if the real numbers `\(a,b\)` are unequal `\(a\neq 0\)`, then `\[f(a)=(a,0)\neq (b,0)=f(b).\]`

Thus, `\(f\)` is injective. Furthermore, and trivially, for all `\(f(a)=(a,0)\in\mathbb C\)`, there exists `\(a\in\mathbb R\)`. Thus `\(f\)` is surjective.  Because `\(f\)` is injective as well as surjective, `\(f\)` is also bijective.

Moreover, for all real numbers `\(a,b\)` it follows from the [existence of real zero][bookofproofs$34] and the [definition of complex addition][bookofproofs$1657]:

`\[\begin{array}{rcll}
f(a\oplus b)&=&f(a\oplus b,0)&\text{by definition of }f\\
&=&(a\oplus b,0\oplus 0)&\text{because real zero is neutral with respect to the addition or real numbers}\\
&=&(a,0)+(b,0)&\text{by definition of complex addition}\\
&=&f(a)+f(b)&\text{by definition of }f
\end{array}\]`

We also have for all real numbers `\(a,b\)`, by virtue of the [multiplication of real numbers by real zero][bookofproofs$521] and the [definition of complex multiplication][bookofproofs$1668].
`\[\begin{array}{rcll}
f(a\odot b)&=&f(a\odot b,0)&\text{by definition of }f\\
&=&(a\odot b\oplus 0,0\oplus 0)&\text{because real zero is neutral with respect to the addition or real numbers}\\
&=&(a\odot b\oplus 0\odot 0,a\odot 0\oplus 0\odot b)&\text{multiplication of real numbers by real zero}\\
&=&(a,0)\cdot(b,0)&\text{by definition of complex multiplication}\\
&=&f(a)\cdot f(b)&\text{by definition of }f
\end{array}\]`

Thus, `\(f\)` is field homomorphism.
