layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1695
orderid: 50
parentid: bookofproofs$1694
title: 
description:  Proof of COMPLEX NUMBERS AS A VECTOR SPACE OVER THE FIELD OF REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1038
keywords: complex,field,numbers,over,real,space,vector,complex vector space over real numbers,complex number space,complex vector space,real number space,numbers vector,vector space over field of complex numbers,complex numbers vector space,vector space over complex numbers,r is not a vector space over c,are complex numbers a vector space,c is a vector space
contributors: bookofproofs

---


---

We will prove that the complex numbers `\(\mathbb C\)` form a [vector space over the field][bookofproofs$560] `\(\mathbb R\)` with respect to the following maps: 
`\[
\cases{
\mathbb C\times \mathbb C\mapsto \mathbb C:x,y\mapsto x + y:=(a+c,b+d)  & \text{(the vector addition)}\\
\mathbb R\times \mathbb C\mapsto \mathbb C:\alpha,x\mapsto \alpha \cdot x:=(\alpha \cdot a,\alpha \cdot b) & \text{(the scalar multiplication)}
}\]`
for any real number `\(\alpha\in\mathbb R\)` and any complex numbers `\(x,y\in\mathbb C\)`, [identified by some ordered pairs of real numbers][bookofproofs$216] `\(x:=(a,b)\)`, `\(y:=(c,d)\)`, `\(a,b,c,d\in\mathbb R\)`.

In particular, we have shown that the [real numbers together with addition and multiplication form a field][bookofproofs$1638] (`\(\mathbb R,+,\cdot)\)`. We have also shown that the [complex numbers together with the addition form a commutative group][bookofproofs$1666] `\((\mathbb C, + )\)`, in particular they form a non-empty set of vectors.

It remains to be shown that for the real numbers `\(\alpha,\beta\in\mathbb R\)` and the complex numbers `\(x,y\in\mathbb C\)`, the following rules of scalar multiplication hold:
1. `\((\alpha + \beta)\cdot x=\alpha\cdot x + \beta\cdot x\)`,
1. `\(\alpha\cdot(x + y)=\alpha\cdot x + \alpha\cdot y\)`, 
1. `\((\alpha\cdot \beta)\cdot x=\alpha\cdot (\beta\cdot x)\)`,
1. If `\(1\)` is the neutral element of multiplication in `\(\mathbb R\)`, then it is also a neutral element of the scalar multiplication in `\(\mathbb C\)`, i.e. `\(1\cdot x=x\)`.

#### Ad `\(1.\)` 

Using the [definition of complex numbers][bookofproofs$216], the above definition of scalar multiplication, the [distributivity rule for real numbers][bookofproofs$520] and the [definition of adding complex numbers][bookofproofs$1657], we can confirm the first rule of scalar multiplication:

`\[\begin{array}{rcll}
(\alpha + \beta)\cdot x&=&(\alpha + \beta)\cdot (a,b)&\text{by definition of complex numbers}\\
&=&((\alpha + \beta)\cdot a,(\alpha + \beta)\cdot b)&\text{by definition of scalar multiplication }\\
&=&((\alpha\cdot a) + (\beta\cdot a),(\alpha\cdot b) + (\beta\cdot b))&\text{by distributivity rule for real numbers}\\
&=&(\alpha\cdot a,\alpha\cdot b) + (\beta\cdot a, \beta\cdot b)&\text{by definition of adding complex numbers}\\
&=&\alpha\cdot x + \beta\cdot x &\text{by definition of complex numbers}
\end{array}\]`


#### Ad `\(2.\)` 

In analogy to 1., we can prove the second rule of scalar multiplication:

`\[\begin{array}{rcll}
\alpha\cdot(x + y)&=&\alpha\cdot((a,b)+ (c,d))&\text{by definition of complex numbers}\\
&=&\alpha\cdot(a+c,b+d)&\text{by definition of adding complex numbers}\\ 
&=&(\alpha\cdot(a+c),\alpha\cdot(b+d))&\text{by definition of scalar multiplication}\\
&=&((\alpha\cdot a) + (\alpha\cdot c),(\alpha\cdot b) + (\alpha\cdot d))&\text{by distributivity rule for real numbers}\\
&=&(\alpha\cdot a,\alpha\cdot b) + (\alpha\cdot c, \alpha\cdot d)&\text{by definition of adding complex numbers}\\
&=&\alpha\cdot (a,b) + \alpha\cdot (c,d)&\text{by definition of scalar multiplication}\\
&=&\alpha\cdot x + \alpha\cdot y &\text{by definition of complex numbers}
\end{array}\]`

#### Ad `\(3.\)` 

Using the [multiplying real numbers is associative][bookofproofs$37], we can confirm the third rule of scalar multiplication:

`\[\begin{array}{rcll}
(\alpha \cdot \beta)\cdot x&=&(\alpha \cdot \beta)\cdot (a,b)&\text{by definition of complex numbers}\\
&=&((\alpha \cdot \beta)\cdot a,(\alpha \cdot \beta)\cdot b)&\text{by definition of scalar multiplication }\\
&=&(\alpha \cdot (\beta\cdot a),\alpha \cdot (\beta\cdot b))&\text{by associativity of multiplying real numbers}\\
&=&\alpha \cdot (\beta\cdot a,\beta\cdot b)&\text{by definition of scalar multiplication}\\
&=&\alpha \cdot (\beta\cdot (a,b))&\text{by definition of scalar multiplication}\\
&=&\alpha\cdot (\beta\cdot x)&\text{by definition of complex numbers}
\end{array}\]`

#### Ad 4.

We have shown the existence of `\(1\)` as a [neutral element of multiplication of real numbers][bookofproofs$40]. Obviously, 


`\[\begin{array}{rcll}
1\cdot x&=&1\cdot (a,b)&\text{by definition of complex numbers}\\
&=&(1\cdot a,1\cdot b)&\text{by definition of scalar multiplication }\\
&=&(a,b)&1\text{ is neutral with respect to the multiplication of real numbers}\\
&=&x&\text{by definition of complex numbers}
\end{array}\]`
