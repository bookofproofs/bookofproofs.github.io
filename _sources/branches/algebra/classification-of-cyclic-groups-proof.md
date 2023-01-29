layout: proof
categories: branches,algebra
nodeid: bookofproofs$2890
orderid: 50
parentid: bookofproofs$8272
title: 
description: PROOF OF CLASSIFICATION OF CYCLIC GROUPS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: classification of cyclic groups,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(G,\ast)$` is a [cyclic group][bookofproofs$807] with a generator `$g\in G$` with `$G=\langle g\rangle.$`
* Define the [function][bookofproofs$592] `$f:(\mathbb Z, + )\to (G,\ast),$` by `$f(k):=a^k$` for all `$a\in (G,\ast)$` and all elements `$k$` of the [additive group of integers][bookofproofs$1654] `$k\in (\mathbb Z,+).$` 
* `$f$` is a [group homomorphism][bookofproofs$679], since `$f(k+j)=a^{k+j}=a^k\ast a^j=f(k)\ast f(j).$`
* In particular, the [image][bookofproofs$809] `$\operatorname{im}(f)$` equals the group `$G$`, since `$\operatorname{im}(f)=\{a^k\mid k\in\mathbb Z\}=\langle g\rangle=G.$`
* On the other hand, the [kernel][bookofproofs$809] `$\ker(f)=\{a\in G\mid f(a)=e_G\}$` is a [subgroup of `$(Z,+)$`][bookofproofs$833].
* Let `$G$` have an [infinite order][bookofproofs$8071] `$|G|=\infty.$`
   * Then `$\ker(f)=\{0\}.$`
   * It follows from the [isomorphism theorem for groups][bookofproofs$8271] that `$(G,\ast)$` is [isomorphic][bookofproofs$412] to `$\mathbb Z/\{0\}.$` 
   * But  `$\mathbb Z/\{0\}=\mathbb Z.$`
   * Therefore, `$(G,\ast)$` is [isomorphic][bookofproofs$412] to `$(\mathbb Z, + ).$`
* Let `$G$` have an [finite order][bookofproofs$8071] `$|G|=n$` with `$n > 0.$`
   * Note that all [additive subgroups of integers][bookofproofs$8268] have the form `$(\mathbb Z_n, + )$` for a [natural number][bookofproofs$718] `$n\in\mathbb N.$`
   * In particular, `$\ker(f)$` has this form.
   * It follows from the [isomorphism theorem for groups][bookofproofs$8271] that `$(G,\ast)$` is [isomorphic][bookofproofs$412] to `$(\mathbb Z/\ker(f), + ) = (\mathbb Z_n, + ).$`
