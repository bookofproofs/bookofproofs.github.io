layout: proof
categories: branches,algebra
nodeid: bookofproofs$2895
orderid: 0
parentid: bookofproofs$8292
title: By Induction
description: A CRITERION FOR ASSOCIATES PROOF ★ history of mathematics ✚ science ➜ visit BookOfProofs now!
references: bookofproofs$677
keywords: criterion for associates,proof
contributors: bookofproofs

---


---

### `$"\Rightarrow"$`

* Assume, `$a,b\in R$` are [associates][bookofproofs$8260] `$a\sim b.$`
* By definition, `$a\mid b$` and `$b\mid a.$`
* This means that there are `$c,d\in R$` with `$ac=b$` and `$bd=a.$`
* Therefore, `$a=bd=acd$`, which means `$0=a(cd-1)$`
* Since `$(R, + , \cdot)$` is an [integral domain][bookofproofs$821], we have either `$a=0$` or `$cd=1$`
* If `$a=0$` then `$b=0$` and, trivially, `$a=cb$` for some  `$c\in R^\ast,$` ($(R^\ast,\cdot)$ being the [group of units][bookofproofs$8283]).
* If `$a\neq 0$` then `$cd=1$` but then `$c$` is a [unit][bookofproofs$8259], therefore `$c\in R^\ast,$` and again `$a=cb.$`

### `$"\Leftarrow"$`

* Let `$a=cb$` with `$c$` being a unit.
* Therefore, `$b\mid a.$`
* But since `$c$` has an [multiplicative inverse][bookofproofs$670] `$d\in R^\ast$` with `$cd=1$`, it follows that `$b=1\cdot b=(cd)b=(cb)d=ad.$` 
* It follows that `$a\mid b.$`
* By dfinition, the elements `$a,b$` are [associates][bookofproofs$8260] `$a\sim b.$`
