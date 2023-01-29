layout: proof
categories: branches,number-theory
nodeid: bookofproofs$819
orderid: 50
parentid: bookofproofs$818
title: 
description:  Proof of DIVISION WITH QUOTIENT AND REMAINDER &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: division with quotient and remainder,division,quotient and remainder,remainder,quotient,remainders,quotients,proof
contributors: bookofproofs

---


---

* Let `$a,b\in\mathbb Z$` be [integers][bookofproofs$844] with `$a > 0.$`
* We first show that there is _at least one_ pair of integers `$q,r$` fulfilling `$$b=qa + r,\quad 0\le r < a.\quad\quad ( * )$$`
   * Among the integers `$b-ua$` there are negative and positive ones for sufficiently large [negative or positive integer][bookofproofs$1075] `$u.$`
   * The [set][bookofproofs$550] `$S:=\{b-ua\mid u\in\mathbb Z\wedge b-ua\ge 0\}$` of non-negetive integers `$b-ua$` is not empty. Since this is a non-empty [subset][bookofproofs$552] of natural numbers `$S\subset \mathbb N$` and the ordered natural numbers `$(N,\le)$` are [well-ordered][bookofproofs$7997], there exists a [minimum][bookofproofs$7995] `$\min(S)$` for some `$u_0\in\mathbb Z.$`
   * We set `$q:=u_0$` and `$r:=b-qa.$` Then we have `$b-qa\ge 0$` and `$r-a=b-(q-1)a < 0.$`
   * This shows that the constructed `$q,r$` solve `$( * ).$`
* We now show that there is _at most one_ pair of integers  `$q,r$` fulfilling `$( * ).$`
   * If we have found some `$q,r$` fulfilling `$( * ),$` then if `$u < q$` then `$u\le q-1$` and `$b-ua\ge b-(q-1)a=r+a\ge a.$`
   * If we have found some `$q,r$` fulfilling `$( * ),$` then if `$u > q$` then `$u\ge q+1$` and `$b-ua\le b-(q+1)a=r-a < 0.$`
   * From this it follows that `$0\le b-ua < a$` can only be fulfilled if `$u=q.$`
