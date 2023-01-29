layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8125
orderid: 50
parentid: bookofproofs$8124
title: 
description:  Proof of LEAST COMMON MULTIPLE OF MORE THAN TWO NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,least,more,multiple,numbers,than,two,proof
contributors: bookofproofs

---


---

* Let `$a,b,c\in\mathbb Z$` be [integers][bookofproofs$844].
* The [commutativity][bookofproofs$672] of `$\operatorname{lcm}$` follows immediatly from the definition of the [least common multiple][bookofproofs$1276] because of the [associativity of conjunction][bookofproofs$1834]; i.e. since `$a\mid m\wedge b\mid m$` if and only if  `$b\mid m\wedge a\mid m,$` the sets `$M_{a,b}$` and `$M_{b,a}$` are equal and have the same [minimum][bookofproofs$7995].
* The [associativity][bookofproofs$668] of `$\operatorname{lcm}$` can be understood as follows:
   * If `$m$` is a [multiple][bookofproofs$700] of both, `$\operatorname{lcm}(a,b)\mid m$` and `$c\mid m,$` then `$\operatorname{lcm}(\operatorname{lcm}(a,b),c))\mid m.$` Moreover, `$a\mid m$` and `$b\mid m.$`
   * Therefore, `$m$` is also a multiple of both, `$a\mid m$` and `$\operatorname{lcm}(b,c)\mid m.$` Thus `$m$` is a multiple of `$\operatorname{lcm}(a,\operatorname{lcm}(b,c)).$`
   * Since this reasoning holds for _any_ common multiple of `$a\mid m,$` `$b\mid m,$` and `$c\mid m,$` it follows `$\operatorname{lcm}(\operatorname{lcm}(a,b),c))=\operatorname{lcm}(a,\operatorname{lcm}(b,c)).$`
* Since `$\operatorname{lcm}$` is both, commutative and associative, the notation `$\operatorname{lcm}(a,b,c)$` makes sense.
* By [induction][bookofproofs$657] over `$k,$` the formula `$\operatorname{lcm}(n_1,\ldots,n_k)=\operatorname{lcm}(\operatorname{lcm}(n_1,\ldots,n_{k-1}),n_k)$` follows.
