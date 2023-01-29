layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1453
orderid: 50
parentid: bookofproofs$1452
title: 
description:  Proof of EXISTENCE OF INTEGER ZERO NEUTRAL ELEMENT OF ADDITION OF INTEGERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: addition,element,existence,integer,integers,neutral,zero,proof
contributors: bookofproofs

---


---

By [definition of integers][bookofproofs$844] `\(x\in\mathbb Z\)`, the integer number `\(x\in\mathbb Z\)` can be represented by a pair of natural numbers `\(a,b\in\mathbb N\)`:
`\[x:=[a,b].\]`
Since `\(0\in\mathbb N\)`, i.e. the [natural zero exists][bookofproofs$1455], it is also true that the (integer) zero `\(0\in\mathbb Z\)` exists, because it can be represented by a pair of the same natural numbers
`\[0=0_{\in\mathbb Z}:=[h,h],\quad h\in\mathbb N,\]`
in particular by `\(h=0\in\mathbb N\)`:
`\[0=0_{\in\mathbb Z}=[0_{\in\mathbb N},0_{\in\mathbb N}].\]`

By the [definition of addition of integers][bookofproofs$890] "`\( + \)`", and because the "natural number `\(0\)` is neutral with respect to the definition of addition of natural numbers][bookofproofs$1455] we have 
`\[\begin{array}{rclcl}
x + 0&=&[a,b]+[0,0]&&\text{by definition of integers}\\
&=&[a+0,b+0]&&\text{by definition of addition of integers}\\
&=&[a,b]&&\text{natural 0 is neutral with respect to the addition of natural numbers}\\
&=&x&&\text{by definition of integers}
\end{array}
\]`

It remains to be shown that also the equation `\(0+x=x\)` holds for all `\(x\in\mathbb Z\)`. It follows immediately from the [commutativity of adding integers][bookofproofs$1460].