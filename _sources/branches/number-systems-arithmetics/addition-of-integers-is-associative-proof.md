layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1444
orderid: 50
parentid: bookofproofs$1443
title: 
description:  Proof of ADDITION OF INTEGERS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,associative,integers,proof
contributors: bookofproofs

---


---

Let `\(x,y,z\in\mathbb Z\)` be integers, which [by definition][bookofproofs$844] means that each integer is an equivalence class of ordered pairs of natural numbers represented by some natural numbers `\(a,b,c,d,e,f\in\mathbb N\)`

`\[\begin{array}{rcl}x&:=&[a,b],\\y&:=&[c,d],\\z&:=&[e,f].\\\end{array}\]`

In order to show the law 
`\[(x+y)+z=x+(y+z)\]`
we replace the symbols `\(x,y,z\)` by their representatives `\([a,b],[c,d],[e,f]\)`, and use the definition of [adding  integers][bookofproofs$890] as well as the [associativity law for adding natural numbers][bookofproofs$1428] to conclude that
`\[\begin{array}{rcll}
(x+y)+z&=&([a,b]+[c,d])+[e,f]&\text{by definition of integers}\\
&=&[a+c,b+d]+[e,f]&\text{by definition of adding integers}\\
&=&[(a+c)+e,(b+d)+f]&\text{by definition of adding integers}\\
&=&[a+(c+e),b+(d+f)]&\text{due to associativity law for adding natural numbers}\\
&=&[a,b]+[c+e,d+f]&\text{by definition of adding integers}\\
&=&[a,b]+([c,d]+[e,f])&\text{by definition of adding integers}\\
&=&x+(y+z)&\text{by definition integers}\\
\end{array}\]`
