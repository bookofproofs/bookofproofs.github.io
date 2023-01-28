layout: example
categories: branches,algebra
nodeid: bookofproofs$8651
orderid: 50
parentid: bookofproofs$679
title: Examples of Group Homomorphisms
description: EXAMPLES OF GROUP HOMOMORPHISMS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: examples of group homomorphisms
contributors: bookofproofs

---


---

### Example 1
 `$f:\mathbb Z\to\mathbb Z$` with `$a\to 3a$` is a [group homomorphism][bookofproofs$679] between the [group][bookofproofs$671] `$(\mathbb Z,+)$` and its [subgroup][bookofproofs$554] `$(\{3n\mid n\in\mathbb Z\}, +),$` since `$$f(a+b)=3(a+b)=3a+3b=f(a)+f(b)$$` for all integers `$a,b\in\mathbb Z.$`

### Example 2

For [real numbers][bookofproofs$1105] `$x\in\mathbb R$`, the [exponential function][bookofproofs$281] is a [group homomorphism][bookofproofs$679] between the groups `$(\mathbb R,+)$` and `$(\mathbb R^{ +},\cdot),$` since `$$\exp(x+y)=\exp(x)\cdot\exp(y)$$` for all `$x,y\in\mathbb R.$` This is also known as the [functional equation of the exponential function][bookofproofs$1415]

### Example 3

The rotation matrix map `$$\rho:x\to\pmatrix{\cos(x)&-\sin(x)\\\sin(x)&\cos(x)}$$` is group homomorphism of the group `$(\mathbb R,+)$` and the general linear group `$(\operatorname{GL}(2,\mathbb R),\cdot)$` together with the [matrix multiplication][bookofproofs$1050] `$[\cdot"$`.  This is because of the "additivity theorems for cosine and sine][bookofproofs$6730] `$$\begin{align}\rho(x+y)&=\pmatrix{\cos(x+y)&-\sin(x+y)\\\sin(x+y)&\cos(x+y)}\nonumber\\
&=\pmatrix{\cos(x)\cos(y)-\sin(x)\sin(y)&-\sin(x)\cos(y)-\cos(x)\sin(y)\\\sin(x)\cos(y)+\cos(x)\sin(y)&\cos(x)\cos(y)-\sin(x)\sin(y)}\nonumber\\
&=\pmatrix{\cos(x)&-\sin(x)\\\sin(x)&\cos(x)}\cdot\pmatrix{\cos(y)&-\sin(y)\\\sin(y)&\cos(y)}\nonumber\\
&=\rho(x)\cdot\rho(y).\nonumber\end{align}$$`
