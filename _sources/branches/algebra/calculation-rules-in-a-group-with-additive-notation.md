layout: explanation
categories: branches,algebra
nodeid: bookofproofs$8070
orderid: 2
parentid: bookofproofs$838
title: Calculation Rules in a Group with Additive Notation
description: CALCULATION RULES IN A GROUP WITH ADDITIVE NOTATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: additive,calculation,group,notation,rules,additive notation
contributors: bookofproofs
issues: broken-links

---


---

For someone who is new to [group theory][bookofproofs$137] but is familiar with [arithmetics][bookofproofs$195] it might be surprising, that in a [group][bookofproofs$671] `$(G,\ast)$`, the same calculation rules apply if we exchange the operation `$\ast$` by an addition sign `$(G, +)$` or by a multiplication sign `$(G, \cdot).$` 

For instance, in the additive notation, the above [calculation rules in a group][bookofproofs$555] can be formulated as follows:
 
1. `$-e=e.$`
1. `$-(-x)=x$` for all `\(x\in G\)`.
1. For all `\(a,b\in G\)`, if `\(a + x=b\)` then `\(x=-a+b\)`.
1. For all `\(a,b\in G\)`, if `\(x + a=b\)` then `\(x=b-a\)`.
1. If `$a+x=a+y$` then `$x=y$` and if `$x+a=y+a$` then `$x=y.$`
1. `$-(x+y)=-y+(-x)$` for all `\(x,y\in G\)`.
1. `\(x_1 + x_2 + x_3 + \ldots + x_n:=(\ldots((x_1 + x_2) + x_3) + \ldots + x_n\)` holds for all `\(x_i\in G\)`.
1. `\(x_{k_1} + x_{k_2} + \ldots + x_{k_n}=x_{1} + x_{2} + \ldots + x_{n}\)`

The "corresponding proof":[bookofproofs$555]proof/ of these (seemingly different) rules is exactly the same except for the notation. Please try to write down the proof in the additive notation it as an exercise!

Similarly, while the [exponentiation in a group][bookofproofs$401] is a new operation, which can be defined, if you use the multiplicative notation `$(G,\ast)$`, the same can be done in the additive case `$(G, + ).$` Here, instead of an "exponentiation", we can define a "multiplication" as a new operation and explain it in terms of addition. To be more concrete, for an integer `$n\in \mathbb Z$`, we can define:

`\[n\cdot x :=
\begin{cases}
e  & \text{ if } n=0 \\
x + (n-1)\cdot x & \text{ if } n > 0.
\end{cases}\]`

And for negative integers `$-n$`:

`$$-n\cdot x:=n\cdot (-x).$$`

> But you have to be very cautious! 

Note that the dot sign `$[\cdot"$` in `$n\cdot x$` does not (!) mean that we _multiply_ the integer `$n$` by a group element `$x$`. It only means that we introduce a shorter notation for adding `$n$` times the element `$x\in G$` to each other. That is also the reason why it makes sense to set the result to the "neutral element][bookofproofs$661] `$e\in G$` in the case `$n=0,$` since we add "none" to each other.

For the sake of completeness, we want to reformulate the [exponentiation rules][bookofproofs$676] and translate them into the additive notation for groups:

`\[\begin{array}{cl}
(1)&n\cdot x+ m\cdot x=(n+m)\cdot x,\\
\end{array}
\]`

If the group is [Abelian][bookofproofs$553], then
`\[\begin{array}{cl}
(2)&m\cdot (n\cdot x)=(mn)\cdot x.\\
(3)&n\cdot x+n\cdot y=n\cdot (x + y).
\end{array}
\]`

Again, the "proof":[bookofproofs$676]proof/ would be exactly the same (try it as an exercise!).

Please note that the exponentiation rules - written down in the additive notation - are strongly reminiscent of a kind of a "distributivity rule" for groups. 

> But again, be cautious! 

There is no distributivity rule for groups since in a group only one operation is defined - but for distributivity, we need two: addition and multiplication. Remember, and this is only a repetition of what has been said above: `$n\cdot x$` does _not_ mean that we multiply an integer `$n$` by the group element `$x.$` It only means that we add `$x\in G$`  `$n$` times to each other.

The reason, why we haven't chosen the additive notation for introducing these calculation rules is that if you are a beginning student of group theory, there is a danger of confusing the operation sign `$"\cdot"$` in `$n\cdot x$` with the group operation, which is only the addition `$(G, +).$`
