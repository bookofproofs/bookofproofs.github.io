layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1032
orderid: 50
parentid: bookofproofs$892
title: 
description:  Proof of ALGEBRAIC STRUCTURE OF INTEGERS TOGETHER WITH ADDITION AND MULTIPLICATION &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$696
keywords: ring of integers,commutative ring of integers,integral domain of integers,proof
contributors: bookofproofs


---


---

We have to show that `\((\mathbb Z, +, \cdot)\)`, i.e. the [set of integers][bookofproofs$844] `\(\mathbb Z\)`, together with the operations [addition][bookofproofs$890] "`\(+\)`" and [multiplication][bookofproofs$891] 
"`\(\cdot\)`" forms an [integral domain][bookofproofs$821]. We will do so by demonstrating, that `\((\mathbb Z, +, \cdot)\)` is a [commutative ring][bookofproofs$880], which is not the [zero ring][bookofproofs$879] and in which the integer `\(0\)` is the only zero divisor.

In order to show that `\((\mathbb Z, +,\cdot)\)` is a [commutative ring][bookofproofs$880], we check the following properties:

* `\((\mathbb Z, + )\)` is a commutative group. This has been shown in [a corresponding proposition][bookofproofs$844]. 
* `\((\mathbb Z, \cdot )\)` is a commutative monoid. This requires the following (sub)properties:
   * We have already shown that the [multiplication of integers is commutative][bookofproofs$1448], thus `\((\mathbb Z,\cdot)\)` is commutative.
   * We have already shown that the [multiplication of integers is associative][bookofproofs$1450], thus `\((\mathbb Z,\cdot)\)` is associative.
   *  `\((\mathbb Z,\cdot)\)` includes the identity `\(1_{\in\mathbb Z}:=[1_{\in\mathbb N},0_{\in\mathbb N}]\)`, which have been shown in the proposition [integers one is neutral with respect to the multiplication of integers][bookofproofs$1454].
* `\((\mathbb Z, +, \cdot)\)` is distributive, which has been shown in the [corresponding proposition][bookofproofs$1466].
We have just shown that `\((\mathbb Z, + ,\cdot)\)` is a commutative ring with `\(1:=[1,0]\)` as the identity of the commutative monoid `\((\mathbb Z,\cdot)\)`. Obviously, `\((\mathbb Z, + ,\cdot)\)` is not the [zero ring][bookofproofs$879], because `\(1\in\mathbb Z\)`. It remains to be shown that `\(0_{\in\mathbb Z}:=[0_{\in\mathbb N},0_{\in\mathbb N}]\)` is the only zero divisor. 

Suppose, there would be other (but `\(0\)`) zero divisors, say `\(x,y\in\mathbb Z\)` with `\(x\neq 0\)`, `\(y\neq 0\)`, and still `\(x\cdot y=0\)`. By definition of integers, suppose `\(x=[a,b],y=[c,d]\)` for some natural numbers `\(a,b,c,d\in\mathbb N\)`. By definition of multiplying integers, we also have that
`\[\begin{array}{ccl}
x\cdot y=[a,b] \cdot [c,d] := [ac + bd, ad + bc].
\end{array}
\]`

Because both `\(x\)` and `\(y\)` are not equal `\(0\)`, we have that `\([a,b]\neq[0,0]\)` and `\([c,d]\neq[0,0]\)`, which means that `\(a\)` and `\(b\)` are not simultaneously equal `\(0\)`, and that `\(c\)` and `\(d\)` are not simultaneously equal `\(0\)`. There are `\(7\)` possibilities for this and we have to check, in which cases the natural numbers `\(ac + bd\)` and `\(ad + bc\)` both equal zero:


`\(a\)` | `\(b\)` | `\(c\)` | `\(d\)` | `\(ac\)` | `\(bd\)` | `\(ad\)` | `\(bc\)` | `\(ac+bd\)` | `\(ad+bc\)`
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`
`\(= 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(=0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`
`\(\neq 0\)`|`\(=0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(=0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(\neq 0\)`
`\(= 0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(=0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(=0\)`|`\(\neq 0\)`|`\(= 0\)`
`\(= 0\)`|`\(\neq 0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(=0\)`|`\(= 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`
`\(\neq 0\)`|`\(= 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(=0\)`|`\(=0\)`|`\(\neq 0\)`|`\(=0\)`|`\(= 0\)`|`\(\neq 0\)`
`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(= 0\)`|`\(\neq 0\)`|`\(=0\)`|`\(=0\)`|`\(=0\)`|`\(\neq 0\)`|`\(= 0\)`

We have seen that in all `\(7\)` cases
`\[\begin{array}{ccl}
[ac + bd, ad + bc]\neq[0,0],
\end{array}
\]`
which demonstrates that the product of integers `\(x\cdot y\)` is never equal (integer) zero. This is a [contradiction][bookofproofs$744] to our hypothesis `\(x\cdot y=0\)`. This completes the proof.
