layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1515
orderid: 50
parentid: bookofproofs$1446
title: 
description:  Proof of ADDITION OF RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: numbers,rational,rational numbers,rational number,definition of rational number,definition of rational numbers,is -1 a rational number,is zero a rational number,define rational number,rational numbers def,rational numbers definition,rational number definition,rational numbers meaning,proof,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [rational numbers][bookofproofs$1485]. By definition, it means that they are represented by some integers `\(x=\frac ab\)`, `\(y=\frac cd\)`, `\(a,c\in \mathbb Z\)`, `\(b,d\in \mathbb Z\setminus\{0\}\)`.

Note that `\(ad\)`, `\(cb\)` and `\(bd\)` are all integers, as they are the [products of the respective integers][bookofproofs$891] `\(a,d\)`, `\(c,d\)` and `\(b,d\)`. Also note that `\(ad + cb\)` is an integer, as it is the [sum of the  integers][bookofproofs$890] `\(ad\)` and `\(cb\)`. Moreover, we have `\(bd\neq 0\)`, since both `\(b\neq 0\)` and `\(d\neq 0\)` and their product cannot equal `\(0\)`, since [integers form an integral domain][bookofproofs$892]. Therefore, the sum `\[\begin{array}{rcl}
x+y=\frac {ad + cb}{bd}.
\end{array}\]`
exists, because it denotes some new rational number, as it is represented by the integers `\(ad + cb\)` and `\(bd\neq 0\)`.

It remains to be shown that the addition of rational numbers does not depend on the specific representatives of the numbers `\(x\)` and `\(y\)`. Suppose, we have different representatives 
`\[\begin{array}{rcl}
x=\frac{a_1}{b_1}=\frac{a_2}{b_2},~y=\frac{c_1}{d_1}=\frac{c_2}{d_2}.&&(*)
\end{array}\]`
It follows from the definition of rational numbers that `\(a_1=\frac{a_2b_1}{b_2}\)` and `\(c_1=\frac{c_2d_1}{d_2}\)`. We have to show that 
`\[x+y=\frac {a_1d_1 + c_1b_1}{b_1d_1}=\frac {a_2d_2 + c_2b_2}{b_2d_2}.\]` 
In the following, we will use the following mathematical definitions and concepts:
* [definition of rational numbers][bookofproofs$1485],
* [definition of adding rational numbers][bookofproofs$1446] (hypothesis),
* [commutativity law of multiplying integers ][bookofproofs$1448], 
* [integer one is neutral with respect to the multiplication of integers][bookofproofs$1454],
* [distributivity law for integers][bookofproofs$1466], and
* [multiplication of rational numbers][bookofproofs$1475]:

`\[\begin{array}{rcll}
x+y&=&\frac{a_1}{b_1}+\frac{c_1}{d_1}&\text{by definition of rational numbers}\\
&=&\frac{a_1d_1+c_1b_1}{b_1d_1}&\text{by hypothesis}\\
&=&\frac{a_1d_1\cdot 1+c_1b_1\cdot 1}{1\cdot b_1d_1}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&\frac{(a_1d_1+c_1b_1)\cdot 1}{1\cdot b_1d_1}&\text{by distributivity law for integers}\\
&=&\frac{a_1d_1+c_1b_1}{1}\cdot \frac 1{b_1d_1}&\text{by definition of multiplying rational numbers}\\
&=&(a_1d_1+c_1b_1)\cdot \frac 1{b_1d_1}&\text{by definition of rational numbers}\\
&=&\left(\frac{a_2b_1}{b_2}d_1+\frac{c_2d_1}{d_2}b_1\right)\cdot \frac 1{b_1d_1}&\text{according to }(*)\\
&=&\left(\frac{a_2b_1\cdot d_1}{b_2\cdot 1}+\frac{c_2d_1\cdot b_1}{d_2\cdot 1}\right)\cdot \frac 1{b_1d_1}&\text{by definition rational numbers and of multiplying them}\\
&=&\left(\frac{a_2b_1d_1}{b_2}+\frac{c_2d_1b_1}{d_2}\right)\cdot \frac 1{b_1d_1}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&\left(\frac{a_2b_1d_1d_2+c_2d_1b_1b_2}{b_2d_2}\right)\cdot \frac 1{b_1d_1}&\text{by hypothesis}\\
&=&\left(\frac{a_2d_2b_1d_1+c_2b_2b_1d_1}{b_2d_2}\right)\cdot \frac 1{b_1d_1}&\text{by commutativity law for multiplying integers}\\
&=&\left(\frac{(a_2d_2+c_2b_2)b_1d_1}{b_2d_2}\right)\cdot \frac 1{b_1d_1}&\text{by distributivity law for integers}\\
&=&\frac{a_2d_2+c_2b_2}{b_2d_2}\cdot \frac {b_1d_1\cdot 1}{b_1d_1}&\text{by definition of multiplying rational numbers}\\
&=&\frac{a_2d_2+c_2b_2}{b_2d_2}\cdot \frac {b_1d_1}{b_1d_1}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&\frac{a_2d_2+c_2b_2}{b_2d_2}\cdot \frac {1}{1}&\text{by definition of rational numbers}\\
&=&\frac{(a_2d_2+c_2b_2)\cdot 1}{b_2d_2\cdot 1}&\text{by definition of multiplying rational numbers}\\
&=&\frac{a_2d_2+c_2b_2}{b_2d_2}&\text{because }1\text{ is neutral with respect to multiplication of integers}\\
&=&\frac{a_2}{b_2}+\frac{c_2}{d_2}&\text{by hypothesis}\\
\end{array}\]`
