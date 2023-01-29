layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1465
orderid: 50
parentid: bookofproofs$1464
title: 
description:  Proof of MULTIPLICATION OF INTEGERS IS CANCELLATIVE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: integers,multiplication,multiplication of integers,proof,proof
contributors: bookofproofs

---


---

Because the [multiplication of integers is commutative][bookofproofs$1448], it is without loss of generality sufficient to show the right cancellation property, i.e. `\[x\cdot z=y\cdot z\Longleftrightarrow x=y,~~~~~~(x,y,z\in\mathbb Z,~z\neq 0).\]`

By [definition of integers][bookofproofs$844], the integer numbers `\(x,y,z\)` are some equivalence classes of ordered pairs of natural numbers represented by some natural numbers `\(a,b,c,d,e,f\in\mathbb N\)`

`\[\begin{array}{rcl}x&:=&[a,b],\\y&:=&[c,d],\\z&:=&[e,f]\\\end{array}\]`

### `\((1)\)` Proof of "`\(\Rightarrow\)`"

Assume the equation `\(x\cdot z=y\cdot z\)` holds and that `\(z\neq 0\)`. We have to show that `\(x=y\)`. By [definition of multiplying integers][bookofproofs$891], we have 
`\[\begin{array}{rcl}
x\cdot z&=&[ae + bf,~ af + be],\\
y\cdot z&=&[ce + df,~ cf + de].
\end{array}\]`

By assumption, `\(x\cdot z=y\cdot z\)`, i.e. 
`\[\begin{array}{rcl}ae+bf&=&ce+df\quad\quad(i)\\
af+be&=&cf+de\quad\quad(ii)
\end{array}\]`

Also by assumption, `\(z\neq 0\)`, i.e. `\(e\)` and `\(f\)` cannot both be equal `\(0\)`, thus `\(z\)` is either a positive integer, or a negative integer.

If `\(z\)` is a positive integer, then `\([e,f]=[e',0]\)` for some natural number `\(e'\neq 0\)`, and we have 

`\[\begin{array}{rcrcl}(i)&\Longleftrightarrow&ae'&=&ce'\\
(ii)&\Longleftrightarrow&be'&=&de'
\end{array}\]`
Because the [multiplication of natural numbers is cancellative][bookofproofs$1440], it follows `\(a=c\)` and `\(b=d\)`, thus the integer `\(x\)` is equal to the integer `\(y\)`, if `\(z\)` is positive.

Otherwise `\(z\)` is a negative integer, thus `\([e,f]=[0,f']\)` for some natural number `\(f'\neq 0\)`, and it follows 

`\[\begin{array}{rcrcl}(i)&\Longleftrightarrow&bf'&=&df'\\
(ii)&\Longleftrightarrow&af'&=&cf'
\end{array}\]`
Again due to the fact that multiplying natural numbers is cancellative, it follows `\(b=d\)` and `\(a=c\)`, thus the integer `\(x\)` is equal to the integer `\(y\)`, if `\(z\)` is negative.

Altogether, it follows from `\(x\cdot z=y\cdot z\)` that `\(x=y\)` for all integers `\(x,y\)` and any integer `\(z\neq 0\)`. Thus, the multiplication of integers is [cancellative][bookofproofs$837].
### `\((2)\)` Proof of "`\(\Leftarrow\)`"

The reasoning is exactly the same with the cases `\(z\)` is a positive or `\(z\)` is a negative integer.
