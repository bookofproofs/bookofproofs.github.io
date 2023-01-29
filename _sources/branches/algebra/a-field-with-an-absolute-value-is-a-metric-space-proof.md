layout: proof
categories: branches,algebra
nodeid: bookofproofs$8663
orderid: 50
parentid: bookofproofs$8662
title: 
description: PROOF OF A FIELD WITH AN ABSOLUTE VALUE IS A METRIC SPACE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: field with absolute value is a metric space,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(F,+,\cdot)$` is a [field][bookofproofs$557] with an [absolute value][bookofproofs$8659] `$|\cdot|:F\to\mathbb R.$`
* Set `$d(x,y):=|x-y|$` for all `$x,y\in F.$`
* We have to verify, that `$d$` is a [metric][bookofproofs$614].
   * If `$d(x,y)=0,$` then `$|x-y|=0,$` and by definition of absolute value `$x=y.$`
   * Vice versa, if `$x=y,$` then `$x-y=0$` and `$d(x,y)=|0|=0.$` 
   * Obviously, `$d(x,y)=d(y,x)$` is symmetric.
   * Also, both, `$d$` fulfills the triangle inequality, because `$|\cdot|$` does.
* It follows that `$(F,d)$` is a [metric space][bookofproofs$617].