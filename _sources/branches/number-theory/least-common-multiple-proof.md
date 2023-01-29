layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1277
orderid: 50
parentid: bookofproofs$1276
title: 
description:  Proof of LEAST COMMON MULTIPLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: common,least,multiple,proof
contributors: bookofproofs

---


---

* Assume `\(a,b\in\mathbb Z\)` are [integers][bookofproofs$844] and `\(M_{a,b}\)` is a [set][bookofproofs$550] defined by `$M:=\left\{m\in\mathbb N : a\mid m\wedge b\mid m\right\}.$` 
* `$M_{a,b}$` is not empty, since it contains e.g. the numbers `\(\pm ab, \pm 2ab, \pm 3ab\)` etc. 
* Moreover, the [intersection][bookofproofs$6828] `$M_{a,b}\cap \mathbb N$` with the set `$\mathbb N$` of [natural numbers][bookofproofs$718] is not empty, since it contains, e.g. the numbers  `\(ab, 2ab, 3ab\)` etc.
* From the [well-ordering principle][bookofproofs$698] of natural numbers, it follows that `$M_{a,b}\cap \mathbb N$` contains a unique [minimum][bookofproofs$7995] `\(m_0\)`. 
* We set `$\operatorname{lcm}(a,b):=m_0.$`
* It remains to be shown that `\(\operatorname{lcm}(a,b)\)` is a [divisor][bookofproofs$700] of any `\(m\in M_{a,b}\)`, in particular `$\operatorname{lcm}(a,b)\neq 0.$`
   * According to [division with quotient and remainder][bookofproofs$818], the equation `$m=q\cdot \operatorname{lcm}(a,b)+r$` is uniquely solved by two other natural numbers `\(q,r\)` with `$$0\le r < \operatorname{lcm}(a,b).\quad\quad( * ).$$` 
   * Because `$r = m-q\cdot \operatorname{lcm}(a,b)=m\cdot 1 + \operatorname{lcm}(a,b)(-q)$` and because  `$a\mid m,$` `$a\mid \operatorname{lcm}(a,b),$` `$b\mid m,$` and `$b\mid  \operatorname{lcm}(a,b),$` it follows from the [divisibility laws][bookofproofs$508] that `$a\mid r,$` and `$b\mid r.$`
   * If we assume that `\(r > 0\)`, then `\(r\in M_{a,b}\)`. 
   * However, we defined `\(\operatorname{lcm}(a,b)\)` as the [minimum][bookofproofs$7995] element of `\(M_{a,b}\)`, thus `\(\operatorname{lcm}(a,b)\le r\)`, in [contradiction][bookofproofs$744] to `\( ( * )\)` requiring `\(\operatorname{lcm}(a,b) > r\)`. 
   * Thus, our assumption `\(r > 0\)` must be wrong and we have `\(r=0\)`. This means that `$m=q\cdot \operatorname{lcm}(a,b).$`
* This demonstrates that `$\operatorname{lcm}(a,b)\mid m$` for all `$m\in M_{a,b}.$`
