layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1451
orderid: 50
parentid: bookofproofs$1450
title: 
description:  Proof of MULTIPLICATION OF INTEGERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: integers,multiplication,multiplication of integers,proof,proof
contributors: bookofproofs

---


---

By the [definition of integers][bookofproofs$844], the integers `\(x,y,z \in \mathbb Z\)` are identified by pairs `\(x:=[a,b]\)`, `\(y:=[c,d]\)` and `\(z:=[e,f]\)` of natural numbers `\(a,b,c,d,e,f\in\mathbb N\)`. 

We have to show that `\((x\cdot y)\cdot z=x\cdot (y\cdot z)\)` is valid for all `\(x,y,z\in\mathbb Z\)`. Multiplying the integers `\(x\cdot y\)`, respectively `\(y\cdot z\)` means [by definition][bookofproofs$891].
`\[\begin{array}{ccl}
x\cdot y:=[a,b] \cdot [c,d] &:=& [a\cdot c + b\cdot d,~ a\cdot d + c\cdot b]=[ac + bd,~ ad + bc],\\
y\cdot z:=[c,d] \cdot [e,f] &:=& [c\cdot e + d\cdot f,~ c\cdot f + d\cdot e]=[ce+df,~cf+de],
\end{array}
\]`
with some new integers `\([ac + bd,~ ad + bc]\)` and `\([ce+df,~cf+de]\)`. Because [adding natural numbers is commutative][bookofproofs$1430] and [associative][bookofproofs$1428], and due to the [distributivity law for natural numbers][bookofproofs$1030], we get:
`\[\begin{array}{cclcl}
(x\cdot y)\cdot z&=&([a,b]\cdot [c,d])\cdot [e,f]&&\text{by definition of integers}\\
&=&([ac+bd,~ad+bc])\cdot [e,f]&&\text{by definition of multiplication of integers}\\
&=&[(ac+bd) e+(ad+bc) f,~(ac+bd) f+(ad+bc) e]&&\text{by definition of multiplication of integers}\\
&=&[(ace+bde)+(adf+bcf),~(acf+bdf)+(ade+bce)]&&\text{by distributivity law for natural numbers}\\
&=&[ace+bde+adf+bcf,~acf+bdf+ade+bce]&&\text{by associativity of adding natural numbers}\\
&=&[(ace+adf)+(bcf+bde),~(acf+ade)+(bce+bdf)]&&\text{by commutativity of adding natural numbers}\\
&=&[a(ce+df)+b(cf+de),~a(cf+de)+b(cd+df)]&&\text{by distributivity law for natural numbers}\\
&=&[a,b]\cdot[ce+df,~cf+de]&&\text{by definition of multiplication of integers}\\
&=&[a,b]\cdot([c,d)\cdot[e,f])&&\text{by definition of multiplication of integers}\\
&=&x\cdot (y\cdot z)&&\text{by definition of integers}
\end{array}
\]`
