layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1670
orderid: 50
parentid: bookofproofs$1669
title: 
description:  Proof of MULTIPLICATION OF COMPLEX NUMBERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: associative,complex,multiplication,numbers,proof
contributors: bookofproofs

---


---

By the [definition of complex numbers][bookofproofs$216], the complex numbers `\(x,y,z \in \mathbb C\)` are identified by prdered pairs `\(x:=(a,b)\)`, `\(y:=(c,d)\)` and `\(z:=(e,f)\)` of some real numbers `\(a,b,c,d,e,f\in\mathbb R\)`. 

We have to show that `\((x\cdot y)\cdot z=x\cdot (y\cdot z)\)` is valid for all `\(x,y,z\in\mathbb C\)`. 

Multiplying the complex numbers `\(x\cdot y\)`, respectively `\(y\cdot z\)`, means [by definition][bookofproofs$1668].
`\[\begin{array}{cl}
x\cdot y:=&(a,b) \cdot (c,d)=(ac-bd,ad+bc),\\
y\cdot z:=&(c,d) \cdot (e,f)=(ce-df,cf+de),
\end{array}
\]`
with some new complex numbers `\((ac-bd,ad+bc)\)` and `\((ce-df,cf+de)\)`. Because [adding real numbers is commutative][bookofproofs$33] and [associative][bookofproofs$31], and due to the [distributivity law of real numbers][bookofproofs$520] we have that:
`\[\begin{array}{ccll}
(x\cdot y)\cdot z&=&[(a,b)\cdot (c,d)]\cdot (e,f)&\text{by definition of complex numbers}\\
&=&(ac-bd,ad+bc)\cdot (e,f)&\text{by definition of multiplication of complex numbers}\\
&=&((ac-bd) e-(ad+bc) f,~(ac-bd) f+(ad+bc) e)&\text{by definition of multiplication of complex numbers}\\
&=&((ace-bde)-(adf+bcf),~(acf-bdf)+(ade+bce))&\text{by distributivity law of real numbers}\\
&=&(ace-bde-adf-bcf,~acf-bdf+ade+bce)&\text{by distributivity law of real numbers and associativity of addition}\\
&=&(ace-adf-bcf-bde,~acf+ade+bce-bdf)&\text{by commutativity of addition of real numbers}\\
&=&((ace-adf)-(bcf+bde),~(acf+ade)+(bce-bdf))&\text{by distributivity law of real numbers}\\
&=&(a(ce-df)-b(cf+de),~a(cf+de)+b(ce-df))&\text{by distributivity law of real numbers}\\
&=&(a,b)\cdot(ce-df,~cf+de)&\text{by definition of multiplication of complex numbers}\\
&=&(a,b)\cdot[(c,d)\cdot(e,f)]&\text{by definition of multiplication of complex numbers}\\
&=&x\cdot (y\cdot z)&\text{by definition of  complex numbers}
\end{array}
\]`
