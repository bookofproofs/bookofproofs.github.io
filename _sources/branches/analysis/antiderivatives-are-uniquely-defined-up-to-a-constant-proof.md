layout: proof
categories: branches,analysis
nodeid: bookofproofs$2933
orderid: 50
parentid: bookofproofs$6806
title: By Induction
description: Proof of ANTIDERIVATIVES ARE UNIQUELY DEFINED UP TO A CONSTANT ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: antiderivatives are unique up to a constant,proof
contributors: bookofproofs

---


---

By hypothesis Let `$I$` be a [real interval][bookofproofs$1153] and `$f:I\to\mathbb R$` is a [continuous function][bookofproofs$1260].
### "`$\Rightarrow$`"

* Assume, `$F,G:I\to\mathbb R$` are [antiderivatives][bookofproofs$1768] of `$f.$`
* By definition, this means for their [derivatives][bookofproofs$1370] that `$F^\prime(x)=G^\prime(x)=f(x)$` for all `$x\in I.$`
* Therefore, for every `$x\in I,$`  `$(F^\prime(x)-G^\prime(x))=\frac d{dx}(F-G)(x)=0$`
* It follows from the [derivative of a constant][bookofproofs$1372] that `$F$` and `$G$` differ at most by a constant. 

### "`$\Leftarrow$`"

* Assume, `$F(x)-G(x)=c$` is [constant][bookofproofs$1371] for all `$x\in I.$`
* Then, `$G^\prime(x)=\frac d{dx}(F(x)-c)=F^\prime(x)=f(x)$` for all `$x\in I.$`
* It follows that `$G$` and `$F$` are [antiderivatives][bookofproofs$1768] of `$f.$`
