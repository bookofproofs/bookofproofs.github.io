layout: proof
categories: branches,algebra
nodeid: bookofproofs$1099
orderid: 50
parentid: bookofproofs$191
title: 
description: Proof of FACTOR GROUPS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: factor,groups,factor group,factor groups,proof
contributors: bookofproofs

---


---

Let `\( ( G ,\ast) \)` be a [group][bookofproofs$671], `\(N\unlhd G\)` its [normal subgroup][bookofproofs$273] and the operation `$"\circ":=(a_1 N)\circ(a_2N):=(a_1\ast a_2)N$` for all `$a_1,a_2\in G$` be given.
* Ad `\((1)\)`: The operation "`\(\circ\)`" is well-defined, (i.e. it does not depend on the particular choice of representatives `\(a_1,a_2\)`).
   * Let `\(a_1,b_1\)` be two different representatives of the left coset `\(a_1N\)` and `\(a_2,b_2\)` be two different representatives of the left coset `\(a_2N\)`. 
   * If `\(b_1\in a_1N\)` then there exists an `\(c_1\in N\)` with `\(b_1=a_1\ast c_1\)`. 
   * Analogously, there is an `\(c_2\in N\)` with `\(b_2=a_2\ast c_2\)`. 
   * Therefore (using the [associativity][bookofproofs$668] of the operation "`\(\ast\)`"):
`\[\begin{array}{ccl}
(b_1\ast b_2)N&=&((a_1\ast c_1)\ast (a_2\ast c_2))N\\
&=&(a_1\ast c_1\ast a_2)\ast\underbrace{(c_2N)}_{=N\text{ because }c_2\in N}\\
&=&(a_1\ast (c_1\ast a_2))N
\end{array}\]` 
   * Because `\(N\)` is a [normal subgroup][bookofproofs$273] of `\(G\)`, there is a `\(c_3\in N\)` with `\(c_1\ast a_2=a_2\ast c_3\)`. 
   * Therefore, continue the calculation by replacing 
`\[\begin{array}{ccl}
(a_1\ast (c_1\ast a_2))N&=&(a_1\ast (a_2\ast c_3))N\\
&=&(a_1\ast a_2)\ast\underbrace{(c_3N)}_{=N\text{ because }c_3\in N}\\
&=&(a_1\ast a_2)N
\end{array}\]` 
   * This demonstrates that `$(a_1\ast a_2)N=(b_1\ast b_2)N.$`
* Ad `\((2)\)` The operation [`\(\circ\)`" is "associative][bookofproofs$668]. 
   * This follows from the associativity of "`\(\ast\)`", since for all `\(a_1,a_2,a_3\in G\)`:
`\[\begin{array}{ccl}
((a_1 N)\circ(a_2N))\circ(a_3N)&=&(a_1\ast a_2)N\circ (a_3N)\\
&=&((a_1\ast a_2)\ast a_3)N\\
&=&(a_1\ast (a_2\ast a_3))N\\
&=&(a_1N)\circ(a_2\ast a_3)N\\
&=&(a_1N)\circ((a_2N\circ a_3N))\\
\end{array}\]`
* Ad `\((3)\)`: The factor group `\((G/N,\circ)\)` contains at least one element `\(N\)` and this is its [neutral element][bookofproofs$661]
   * The [left coset][bookofproofs$827] `\(e_GN\)` with respect to the neutral element `\(e_G\in G\)` is an element of `\((G/N,\circ)\)`.
   * Thus, `\(N=e_GN\in G/N\)`. 
   * Moreover, for any [coset][bookofproofs$827] `\(aN\in G/N\)` we have
`\[\begin{array}{ccccccc}
N\circ(aN)&=&(e_GN)\circ(aN)&=&(e_G\ast a)N&=&aN\\
(aN)\circ N&=&(aN)\circ(e_GN)&=&(a\ast e_G)N&=&aN\\
\end{array}\]` 
   * Therefore, `\(N\)` is the identity element of `\((G/N,\circ)\)`.
* Ad `\((4)\)`: The [inverse element][bookofproofs$670] of an element `\(aN\)` of `\((G/N,\circ)\)` is `\(a^{-1}N\)`.
   * For any `\(aN\in G/N\)` we have 
`\[\begin{array}{ccccccc}
(a^{-1}N)\circ(aN)&=&(a^{-1}\ast a) N&=&e_GN&=&N\\
(aN)\circ(a^{-1}N)&=&(a\ast a^{-1}) N&=&e_GN&=&N.\\
\end{array}\]`

Altogether, we have shown that the [quotient set][bookofproofs$829] `\(G/N:=\{aN: a\in G\}\)` of all [ (left) cosets][bookofproofs$827], together with the binary operation `$"\circ"$` forms a factor group `$(G/N,\circ ).$` 

* Ad `\((5)\)`: `\((G/N,\circ )\)` is [Abelian][bookofproofs$553], if `$G$` is.
   * This follows immediately from the definition of `$"\circ".$`
