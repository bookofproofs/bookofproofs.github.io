layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1530
orderid: 50
parentid: bookofproofs$890
title: 
description:  Proof of ADDITION OF INTEGERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,integers,proof
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [integers][bookofproofs$844]. By definition, it means that they are equivalence classes represented by some natural numbers `\(x=\lbrack a,b\rbrack \)`, `\(y=\lbrack c,d\rbrack \)`, `\(a,b,c,d\in \mathbb N\)`.

Note that `\(a+b\)`, `\(c+d\)` are all natural numbers, since they are the [sums of the respective natural numbers][bookofproofs$842] `\(a,c\)` and `\(b,d\)`. Therefore, the sum `$$\begin{array}{rcl}
x+y=\lbrack a+c,b+d\rbrack .
\end{array}$$`
exists, because it denotes some new integer, as it is represented by the natural numbers `\(a+c\)` and `\(b+d\)`.

It remains to be shown that the addition of integers does not depend on the specific representatives of the numbers `\(x\)` and `\(y\)`. Suppose, we have different representatives 
`$$\begin{array}{rcl}
x=\lbrack a_1,b_1\rbrack =\lbrack a_2,b_2\rbrack ,~y=\lbrack c_1,d_1\rbrack  =\lbrack c_2,d_2\rbrack .&&(*)
\end{array}$$`
Without loss of generality, we can assume `\(a_1\ge a_2\)` and `\(c_1\ge c_2\)`. It follows from the definition of integers that there exist some natural numbers `\(i,j\)` with 
`$$\begin{array}{rl}
a_1=a_2+i,&c_1=c_2+j,\\
b_1=b_2+i,&d_1=d_2+j.\\
\end{array}\quad (*)$$`

We have to show that 
`$$x+y=\lbrack a_1+c_1,b_1+d_1\rbrack =\lbrack a_2+c_2,b_2+d_2\rbrack .$$`
In the following, we will use the following mathematical definitions and concepts:
* [definition of integers][bookofproofs$844],
* [definition of adding integers][bookofproofs$890] (hypothesis),
* [commutativity law of adding natural numbers][bookofproofs$1430], 
* [cancellation law of adding natural numbers][bookofproofs$1432], and
* [associativity law of adding natural numbers][bookofproofs$1428]:

`$$\begin{array}{rcll}
x+y&=&\lbrack a_1,b_1\rbrack +\lbrack c_1,d_1\rbrack &\text{by definition of integers}\\
&=&\lbrack a_1+c_1,b_1+d_1\rbrack &\text{by hypothesis}\\
&=&\lbrack (a_2+i)+(c_2+j),(b_2+i)+(d_2+j)\rbrack &\text{according to }(*)\\
&=&\lbrack a_2+i+c_2+j,b_2+i+d_2+j\rbrack &\text{by associativity law for adding natural numbers}\\
&=&\lbrack a_2+c_2+i+j,b_2+d_2+i+j\rbrack &\text{by commutativity law for adding natural numbers}\\
&=&\lbrack a_2+c_2+(i+j),b_2+d_2+(i+j)\rbrack &\text{by associativity law for adding natural numbers}\\
&=&\lbrack a_2+c_2+\cancel{(i+j)},b_2+d_2+\cancel{(i+j)}\rbrack &\text{by cancellation law for adding natural numbers}\\
&=&\lbrack a_2+c_2,b_2+d_2\rbrack &\text{by definition of integers}\\
&=&\lbrack a_2,b_2\rbrack +\lbrack c_2,d_2\rbrack &\text{by hypothesis}\\
\end{array}$$`
