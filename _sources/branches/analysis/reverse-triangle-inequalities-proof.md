layout: proof
categories: branches,analysis
nodeid: bookofproofs$2982
orderid: 50
parentid: bookofproofs$6637
title: 
description: Proof of REVERSE TRIANGLE INEQUALITIES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: reverse triangle inequality,reverse triangle inequalities,proof
contributors: bookofproofs

---


---

By hypothesis, `$x,y\in\mathbb R$` are arbitrary [real numbers][bookofproofs$1105].
### Proof of `$(1)$`

* Let `$u:=x+y$` and `$v:=-y$`
* By the [triangle inequality][bookofproofs$588], we have `$$|u+v|\le |u|+|v|$$`
* By definition `$$|x|\le|x+y|+|-y|=|x+y|+|y|.$$`
* By [rule 3 for calculations with inequalities][bookofproofs$594] we can add `$-|y|$` on both sides to get `$$|x+y|\ge |x|-|y|.$$`

### Proof of `$(2)$`

* From `$(1)$` it follows `$|x-y|=|x+(-y)|\ge |x|-|(-y)|=|x|-|y|.$`
* For the same reason `$|y-x|\ge |y|-|x|.$`
* By definition of [absolute value][bookofproofs$583] `$|x-y|=|y-x|.$`
* Thus, both inequalities hold simultaneously: `$|x-y|\ge |x|-|y|$` and  `$|x-y|\ge |y|-|x|.$`
* The greater of `$|x|-|y|$` and `$|y|-|x|$` equals `$\left||x|-|y|\right|.$`  
* Therefore, `$$|x-y|\ge \left||x|-|y|\right|.$$`
