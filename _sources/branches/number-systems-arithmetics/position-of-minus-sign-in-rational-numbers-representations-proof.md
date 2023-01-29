layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1593
orderid: 50
parentid: bookofproofs$1592
title: 
description:  Proof of POSITION OF MINUS SIGN IN RATIONAL NUMBERS REPRESENTATIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1591
keywords: minus,numbers,position,rational,representations,sign,proof
contributors: bookofproofs

---


---

We want to show the equations
`\[\frac{-a}b=\frac a{-b},\quad\quad\frac {-a}{-b}=\frac ab,\quad\quad\frac {0}{-b}=\frac 0b\quad\quad ( * )\]`

By the [definition of rational numbers][bookofproofs$1033], two rational numbers `\(\frac ab\)` and `\(\frac cd\)`, with some integers `\(a,b,c,d\in\mathbb Z\)` and `\(b\neq 0\)`, `\(d\neq 0\)` are equal if and only if the products of their respective nominators and denominators equal each other, formally

`\[\frac ab=\frac cd\Longleftrightarrow ad=cb.\]`

Thus, `\(( * )\)` transforms into 

`\[{-a}({-b})=ab,\quad\quad{-a}b=a({-b}),\quad\quad{0}b=0({-b})\quad\quad ( * * )\]`

Without loss of generality, we can assume the integers `\(a,b\in\mathbb Z\)` to be [positive][bookofproofs$1075]. Thus, `\(-a\)` and `\(-b\)` are [negative integers][bookofproofs$1075]. By [definition of integers][bookofproofs$844], we can represent them by ordered pairs of the natural numbers `\(0,\alpha,\beta\)` in the following way:

`\[\begin{array}{rcl}
0&:=&[0,0],\\
a&:=&[\alpha,0],\\
-a&:=&[0,\alpha],\\
b&:=&[\beta,0],\\
-b&:=&[0,\beta].
\end{array}\]`

We will prove `\(( * * )\)` by verifying that the [products of the respective integers][bookofproofs$891] are indeed equal, making use of the [commutativity of adding natural numbers][bookofproofs$1430]:

`\[\begin{array}{rcll}
{-a}({-b})&=&[0,\alpha]\cdot [0,\beta]&\text{by definition of integers}\\
&=&[0\cdot 0 + \alpha\cdot \beta,~ 0\cdot \beta + \alpha\cdot 0]&\text{by definition of multiplying integers}\\
&=&[\alpha\cdot \beta + 0\cdot 0,~ \alpha\cdot 0 + 0\cdot \beta]&\text{by commutativity of adding natural numbers}\\
&=&[\alpha,0]\cdot [\beta,0]&\text{by definition of multiplying integers}\\
&=&ab&\text{by definition of integers}
\end{array}\]`

`\[\begin{array}{rcll}
{-a}b&=&[0,\alpha]\cdot [\beta,0]&\text{by definition of integers}\\
&=&[0\cdot \beta + \alpha\cdot 0,~ 0\cdot 0 + \alpha\cdot \beta]&\text{by definition of multiplying integers}\\
&=&[\alpha\cdot 0 + 0\cdot \beta,~ \alpha\cdot \beta + 0\cdot 0]&\text{by commutativity of adding natural numbers}\\
&=&[\alpha,0]\cdot [0,\beta]&\text{by definition of multiplying integers}\\
&=&a(-b)&\text{by definition of integers}
\end{array}\]`

`\[\begin{array}{rcll}
{0}b&=&[0,0]\cdot [\beta,0]&\text{by definition of integers}\\
&=&[0\cdot \beta + 0\cdot 0,~ 0\cdot 0 + 0\cdot \beta]&\text{by definition of multiplying integers}\\
&=&[0\cdot 0 + 0\cdot \beta,~ 0\cdot \beta + 0\cdot 0]&\text{by commutativity of adding natural numbers}\\
&=&[0,0]\cdot [0,\beta]&\text{by definition of multiplying integers}\\
&=&0(-b)&\text{by definition of integers}
\end{array}\]`
