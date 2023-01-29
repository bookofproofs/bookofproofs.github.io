layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1467
orderid: 50
parentid: bookofproofs$1466
title: 
description:  Proof of DISTRIBUTIVITY LAW FOR INTEGERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: distributivity,integers,law,proof
contributors: bookofproofs

---


---

By the [definition of integers][bookofproofs$844], the integers `\(x,y,z \in \mathbb Z\)` are identified by pairs `\(x:=[a,b]\)`, `\(y:=[c,d]\)` and `\(z:=[e,f]\)` of natural numbers `\(a,b,c,d,e,f\in\mathbb N\)`. Because [multiplying integers is commutative][bookofproofs$1448], it is sufficient to show the left-distributivity law
`\[x\cdot(y+z)=(x\cdot y)+(x\cdot z).\]`

The left-distributivity law can be proven using the following mathematical definitions and concepts:
* [definition of adding integers][bookofproofs$890],
* [definition of multiplying integers][bookofproofs$891],
* [distributivity law for natural numbers][bookofproofs$1030], and
*  [commutativity law for adding natural numbers][bookofproofs$1430].
The proof follows:


`\[\begin{array}{ccll}
x\cdot(y+z)&=&[a,b]\cdot([c,d] + [e,f])&\text{by definition of integers}\\
&=&[a,b]\cdot[c+e,d+f]&\text{by definition of adding integers}\\
&=&[a(c+e)+b(d+f),a(d+f)+b(c+e)]&\text{by definition of multiplying integers}\\
&=&[ac+ae+bd+bf,ad+af+bc+be]&\text{by distributivity law for natural numbers}\\
&=&[ac+bd+ae+bf,ad+bc+af+be]&\text{by commutativity of adding natural numbers}\\
&=&[ac+bd,ad+bc]+[ae+bf,af+be]&\text{by definition of adding integers}\\
&=&([a,b]\cdot[c,d])+([a,b]\cdot[e,f])&\text{by definition of multiplying integers}\\
&=&(x\cdot y)+(x\cdot z)&\text{by definition of integers}
\end{array}
\]`
