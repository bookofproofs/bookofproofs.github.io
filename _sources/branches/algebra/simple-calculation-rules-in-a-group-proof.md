layout: proof
categories: branches,algebra
nodeid: bookofproofs$556
orderid: 0
parentid: bookofproofs$555
title: 
description:  Proof of SIMPLE CALCULATIONS RULES IN A GROUP &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: calculation,group,rules,simple,proof
contributors: bookofproofs

---


---

### Ad 1) 

* Because of the existence of [inverse][bookofproofs$670] elements it is `\(e=e\ast e^{-1}\)`. 
* On the other hand, because `$e$` is the [unique neutral element][bookofproofs$669], we have `\(e^{-1}=e\ast e^{-1}\)`.
* Comparing both equations leads to `\(e^{-1}=e\)`.

### Ad 2)

* The element `\(x^{-1}\)` has the inverse elements `\((x^{-1})^{-1}\)` and `\(x\)`, respectively.
* Both must be identical, since [inverse element are unique][bookofproofs$359]

### Ad 3)

* `\(a^{-1}\ast b\)` _is_ the solution of `\(a\ast x=b\)`, since `\(a\ast (a^{-1}\ast b)=(a\ast a^{-1})\ast b=e\ast b=b\)` for all `\(a,b\in G\)`. 
* Moreover, it is the _only_ solution. For if an element `$y\in G$` solves `\(a\ast y=b\)`, it follows  
`\[\begin{array}{rcl}
a\ast y&=&b\\
a^{-1}\ast (a\ast y)&=&a^{-1}\ast b\\
(a^{-1}\ast a)\ast y&=&a^{-1}\ast b\\
e\ast y&=&a^{-1}\ast b\\
y&=&a^{-1}\ast b
\end{array}
\]`

### Ad 4) 

Exercise, in analogy to 3)

### Ad 5)

* If `$a\ast x=a\ast y$` then for all `$a\in G$`:
`\[\begin{array}{rcl}
a\ast x&=&a\ast y\\
a^{-1}\ast (a\ast x)&=&a^{-1}\ast (a\ast y)\\
(a^{-1}\ast a)\ast x&=&(a^{-1}\ast a)\ast x\\
e\ast x&=&e\ast y\\
x&=&y
\end{array}
\]`
* A similar [cancellation property][bookofproofs$837] can be concluded for the equation `$x\ast a=y\ast a$`, from which it follows `$x=y$` for all `$a\in G.$`

### Ad 6)

The element `\((x\ast y)\)` has the inverse element `\((x\ast y)^{-1}\)`. It follows for all `\(x,y\in G\)`:
`\[\begin{array}{rcl}
(x\ast y)\ast(x\ast y)^{-1}&=&e\\
y^{-1}\ast x^{-1}\ast (x\ast y)\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\ast e\\
y^{-1}\ast (x^{-1}\ast x)\ast y\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
y^{-1}\ast e\ast y\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
y^{-1}\ast y\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
(y^{-1}\ast y)\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
e\ast(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
(x\ast y)^{-1}&=&y^{-1}\ast x^{-1}\\
\end{array}
\]`

### Ad 7)

* `$[\ast"$` is "associative][bookofproofs$668] by definition of a [group][bookofproofs$671] (a group is a monoid, which is a semigroup, which is associative)
* Therefore, we can apply the [general associative law][bookofproofs$540] we have already proven for any associative algebraic structure.

### Ad 8) 

* If the group `\((G,\ast)\)` is [commutative][bookofproofs$553], then we can apply the [general commutative law][bookofproofs$542] we have already proven for any commutative algebraic structure.
