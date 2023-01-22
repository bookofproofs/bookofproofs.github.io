layout: proof
categories: branches,algebra
nodeid: bookofproofs$2889
orderid: 0
parentid: bookofproofs$8271
title: 1574
description: Proof of FIRST ISOMORPHISM THEOREM FOR GROUPS ★ history of mathematics ✚ science ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: isomorphism theorem for groups,group isomorphism theorem,group isomorphism theorems,isomorphism theorem,first isomorphism theorem,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(G,\ast)$`, `$(H,\cdot)$` are [groups][bookofproofs$671] and `$f:G\to N$` is a [group homomorphism][bookofproofs$679] with the [kernel][bookofproofs$809] `$\ker(f).$` 
* We demonstrate that `$(G/\ker(f),\circ)$` is a [factor group][bookofproofs$191] `$(G/\ker(f),\circ).$`
   * First of all, `$\ker(f)=\{g\in G\mid f(g)=e_H\}$` is a [subgroup][bookofproofs$554] of `$G$` according to the [corresponding lemma][bookofproofs$833]
   * Moreover, it is even a [normal subgroup][bookofproofs$273] of `$G,$` according to [another previous lemma][bookofproofs$832]
   * By definition of [factor groups][bookofproofs$191], `$(G/\ker(f),\circ)$` is a factor group with the group operation `$"\circ"$` defined by `$$(a_1 \ker(f))\circ(a_2\ker(f)):=(a_1\ast a_2)\ker(f)$$` for all `$a_1,a_2\in G.$` 
* Moreover, the [image][bookofproofs$809] `$\operatorname{im}(f)=\{f(g)\in H\mid g\in G\}$` is a [subgroup][bookofproofs$554] of `$(H,\cdot)$` according to the [corresponding lemma][bookofproofs$833], and in particular a [group][bookofproofs$671] itself.
* Thus, the [algebraic structures][bookofproofs$342] `$(\operatorname{im}(f),\cdot)$` and `$(G/\ker(f),\circ)$` are [groups][bookofproofs$671].
* The [function][bookofproofs$592] `$\phi:G/\ker(f)\to \operatorname{im}(f),$` `$\phi(a\ker(f))=f(a)$` is [well-defined][bookofproofs$558]:
   * Assume, `$a,b\in G$` with `$a\ker(f)=b\ker(f).$`
   * Therefore `$a\ast b^{-1}\in \ker(f).$` 
   * Since `$f$` is a [group homomorphism][bookofproofs$679], it follows from the [properties of group homomorphism][bookofproofs$680] that `$$\begin{array}{rcl}f(a\ast b^{-1})&=&f(a)\cdot f(b^{-1})\\&=&f(e_G)\\&=&e_H.\end{array}$$`
   * Thus, `$f(a)=f(b).$`
* Moreover, `$\phi$` is itself a [group homomorphism][bookofproofs$679].
   * Since for all `$a,b\in G$` we have `$$\begin{array}{rcl}\phi(a\ker(f)\circ b\ker (f))&=&\phi((a\ast b)\ker(f))\\
&=&f(a\ast b)\\
&=&f(a)\cdot f(b)\\
&=&\phi(a\ker(f))\circ \phi(b\ker(f)).\end{array}$$`
* `$\phi$` is [injective][bookofproofs$769]
   * Let `$a\in G$` with `$\phi(a\ker(f))=f(a)=e_H$` be given.
   * Then `$a\in\ker(f).$`
   * Therefore, `$a\ker(f)=e_G\ker(f).$`
   * It follows `$\ker(\phi)=\{e_G\ker(f)\}.$`
* `$\phi$` is [surjective][bookofproofs$770]
   * Let `$b\in \operatorname{im}(f).$` 
   * Then there is an `$a\in G$` with `$f(a)=b.$`
   * It follows `$\phi(a\ker(f))=b.$`
* Altogether, we have shown that `$\phi$` is a [bijective][bookofproofs$771] group homomorphism, in other words `$\phi$` is an [isomorphism][bookofproofs$412]
