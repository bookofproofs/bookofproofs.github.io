layout: proof
categories: branches,number-theory
nodeid: bookofproofs$2945
orderid: 50
parentid: bookofproofs$8155
title: 
description:  Proof of CONGRUENCES AND DIVISION WITH QUOTIENT AND REMAINDER &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8152
keywords: congruences,division,quotient,remainder,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Let `$a=q_am+r_a$` and `$b=q_bm+r_b$` in the [division with quotient and remainder][bookofproofs$818], with `$0\le r_a < m$` and `$0\le r_b < m.$`  
* We can subtract both equations and get `$a-b=(q_a-q_b)m.$`
* It follows `$m\mid (a-b).$` 
* This means, by definition, `$a\equiv b(m)$` (i.e. `$a$` is [congruent][bookofproofs$8153] to `$b$` modulo `$m$`).

### "`$\Leftarrow$`"

* Let `$a\equiv b(m)$` and `$a=q_am+r_a$` with `$0\le r_a < m.$` 
* Since `$m\mid(a-b)$`, there is an integer `$q$` with `$b=a+qm.$` 
* This means that `$b= q_am+r_a+qm=(q_a+q)m+r_a=q_bm+r_a$`
* It follows, that any division with quotient and remainder of `$b$` results in the same remainder `$r_a.$`

Altogether, it follows `$a\equiv b(m)\Longleftrightarrow r_a=r_b.$`
