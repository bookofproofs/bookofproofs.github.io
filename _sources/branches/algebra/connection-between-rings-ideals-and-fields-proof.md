layout: proof
categories: branches,algebra
nodeid: bookofproofs$2894
orderid: 0
parentid: bookofproofs$8289
title: 1594
description: CONNECTION BETWEEN RINGS IDEALS AND FIELDS PROOF ★ history of mathematics ✚ science ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: connection between rings ideals and fields,two ideals,ring with two right ideals,ring with two left ideals,proof
contributors: bookofproofs

---


---

### `$(1)$`

* Let `$I\lhd F$` be an [ideal][bookofproofs$1062] of a [field][bookofproofs$557] `$(F, + ,\cdot).$`
* By definition of ideals, `$I$` is not empty, for all `$a,b\in I$` also `$a-b\in I,$` and for all `$i\in I$` and all `$r\in F$` we have `$ir\in I$` and `$ri\in I.$`
* It is clear from the definition of ideals, that if `$I=\{0\},$` then `$I$` is an ideal.
* Therefore, assume, `$I\neq \{0\}.$`
* Then, we can also choose `$a\in I$` such that `$a\neq 0.$`
* Since `$F$` is a field, there is a [multiplicative inverse][bookofproofs$670]  `$a^{-1}\in F.$`
* Therefore, `$aa^{-1}\in I$` or `$1\in I.$`
* It follows `$I=F.$`

### `$(2)$`

* Assume, [ring][bookofproofs$683]  `$(R, + ,\cdot)$` has exactly two ideals.
* Note that every [zero ring][bookofproofs$879] has only one ideal.
* Therefore, `$R$` is not a zero ring.
* Therefore, the two ideals in question of `$R$` must be `$\{0\}\lhd R$` and `$R\lhd R,$` since these two subsets of `$R$` are trivially ideals, by definition.
* In particular, `$1\neq 0$` holds in `$R$` and there is an `$a\in R$` with `$a\neq 0.$`
* Consider the [principal ideal][bookofproofs$1063] `$(a)\lhd R.$`
* Since `$(a)\neq\{0\}$` then `$1\in(a),$` therefore `$1=a\cdot a^{-1}.$`
* We have just shown that every `$a\in R$` with `$a\neq 0$` has a [multiplicative inverse][bookofproofs$670]  `$a^{-1}\in R.$`
* It follows that `$R$` is a field.
