layout: proof
categories: branches,algebra
nodeid: bookofproofs$2891
orderid: 0
parentid: bookofproofs$8273
title: 1584
description: Proof of CLASSIFICATION OF FINITE GROUPS WITH THE ORDER OF A PRIME NUMBER ★ history of mathematics ✚ science ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: classification of finite groups, prime order,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(G,\ast)$` is a [finite group][bookofproofs$8071] with a [group order][bookofproofs$8071] `$|G|=p,$` where `$p$` is a [prime number][bookofproofs$473]
* Since [finite order of an element equals group order][bookofproofs$8270], `$\langle a\rangle$` is a [subgroup][bookofproofs$554] of `$G$` with a [finite order][bookofproofs$8071] `$|\langle a\rangle|$` for any `$a\in G.$`  
* According to the [Lagrange's theorem][bookofproofs$831], the `$|\langle a\rangle|$` is a [divisor][bookofproofs$700] of `$p.$`
* By [definition of prime numbers][bookofproofs$473], either `$|\langle a\rangle|=1$` or `$|\langle a\rangle|=p.$` 
* Because `$\langle a\rangle$` contains at least two elements, the [neutral element][bookofproofs$661] `$e$` and `$a,$` we have `$|\langle a\rangle|\neq 1.$`
* Therefore, `$|\langle a\rangle|=p=|G|.$`
* Since all [subgroups of cyclic groups][bookofproofs$817] are cyclic, `$\langle a\rangle$` is a [cyclic group][bookofproofs$807]
* Therefore, `$G$` is a cyclic group.
* By the [classification of cyclic groups][bookofproofs$8272], `$(G,\ast)$` is [isomorphic][bookofproofs$412] to the [additive subgroup of integers][bookofproofs$8268] `$(\mathbb Z_p, + ).$`
