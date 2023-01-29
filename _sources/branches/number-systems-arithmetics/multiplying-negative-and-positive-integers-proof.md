layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1590
orderid: 50
parentid: bookofproofs$1589
title: 
description:  Proof of MULTIPLYING NEGATIVE AND POSITIVE INTEGERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: integers,multiplication,multiplication of integers,proof,proof
contributors: bookofproofs

---


---

According to the [definition of negative and positive integers][bookofproofs$1075], we can represent an integer `\(x\)` by an ordered pair of a natural number `\(a\)` and `\(0\)` in three ways:
`\[x=\begin{cases}[a,0],~a\neq 0&\Longleftrightarrow \text{ if }x\text{ is a positive integer}\\
[0,0],&\Longleftrightarrow \text{ if }x\text{ equals 0}\\
[0,a],~a\neq 0&\Longleftrightarrow \text{ if }x\text{ is a negative integer}\\
\end{cases}\]`

According to the  [definition of multiplying integers][bookofproofs$891], we have for two integers `\(x=[a,b]\)` and `\(y=[c,d]\)`:

`\[\begin{array}{ccl}
x\cdot y:=[a,b] \cdot [c,d] &:=& [a\cdot c + b\cdot d,~ a\cdot d + c\cdot b]=[ac + bd,~ ad + bc],
\end{array}
\]`

Because the [multiplication of integers is commutative][bookofproofs$1448], it is sufficient to prove the following four cases:

### `\((1)\)` A positive integer times a positive integer gives a positive integer

Let `\(x=[a,0]\)` and `\(y=[c,0]\)`. It follows

`\[[a,0] \cdot [c,0] =[a\cdot c + 0\cdot 0,~ a\cdot 0 + c\cdot 0]=[ac,0],\]`
which is a positive integer.

### `\((2)\)` A negative integer times a positive integer gives a negative integer.

Let `\(x=[0,b]\)` and `\(y=[c,0]\)`. It follows

`\[[0,b] \cdot [c,0] =[0\cdot c + b\cdot 0,~ 0\cdot 0 + c\cdot b]=[0,bc],\]` 
which is a negative integer.

### `\((3)\)` A negative integer times a negative integer gives a positive integer.

Let `\(x=[0,b]\)` and `\(y=[0,d]\)`. It follows

`\[[a,0] \cdot [c,0] =[0\cdot 0 + b\cdot d,~ 0\cdot d + 0\cdot b]=[bd,0],\]`

which is a positive integer.

### `\((4)\)` Zero times any integer gives zero.

Let `\(x=[0,0]\)` and `\(y=[c,d]\)`. It follows

`\[[0,0] \cdot [c,d] =[0\cdot c + 0\cdot d,~ 0\cdot d + c\cdot 0]=[0,0],\]`

which is zero.
